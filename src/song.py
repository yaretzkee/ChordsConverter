import sys
sys.path.insert(0, '..')
import re

from collections import namedtuple
from unidecode import unidecode
from bs4 import BeautifulSoup
from bs4.element import ContentMetaAttributeValue, NavigableString, Tag

from string import Template

try: 
    from src.chord import Chord
    from src.examples import Example
    from src.regex_patterns import *

except ModuleNotFoundError:
    from chord import Chord
    from examples import Example
    from regex_patterns import *

class Song:
    ''' class to manipulate (read/convert) various song/chords formats
        accepted input formats:
        0 - Ultimate Guitar
        1 - ChordPro
        2 - LaTeX ('Leadsheets' package, not 'Songs' !!)
        3 - (in future, not yet) - LaTeX (Songs Package)
        4 - .sng (Proprietary format used in Hawiarska Koliba songbook)
    '''
    frets = [None,'I','II','III','IV','V','VI','VII','VIII','IX','X','XI']
    
    def __init__(self, raw_text, input_format) -> None:
        self.raw_text = raw_text.split('\n')
        self.input_format = input_format

        # declare all required properties:
        self.title = ''
        self.band = ''
        self.capo = 0
        self.chords_above = False
        self.category = '' # required in .sng format
        self._process()
    
    def __str__(self):
        return f'{self.artist} - {self.title}'
    
    def _process(self):
        if self.input_format == 0:
            self._read_ug()
        
        elif self.input_format == 1: 
            self._read_chopro()
        
        elif self.input_format == 2: 
            self._read_latex_leadsheets()

        elif self.input_format == 4: 
            self._read_koliba()

        elif self.input_format == 5:
            self._read_wywrota()
        
        else:
            pass

    def _read_ug(self):
        self.song_body = []
        env='default'
        Line = namedtuple('Line', ['mode', 'linemarker', 'lyrics', 'chords', 'pos_crd_pairs','chords_above'], defaults=(None,None,None,None,None,None))
        linedata = Line()
        LineMarker = namedtuple('LineMarker', ['firstline', 'lastline'], defaults=(False, False))
        lm = LineMarker()

        for line in self.raw_text:
            if line.strip():
                if re.match(REGEX_UG_ENVIRONMENTS, line):
                    env = re.match(REGEX_UG_ENVIRONMENTS,line)[1].lower()
                    next_line_is_first_of_env = True

                elif re.findall(REGEX_UG_CHORD, line):
                    matches  = REGEX_UG_CHORD.finditer(line)
                    line_chords = [Chord(txt=crd.group(0), input_mode='english') for crd in matches]
                    #pairs = [(m.start(), Chord(m.group(0),input_mode='english')) for m in re.finditer(REGEX_UG_CHORD, line)]
                    
                    pairs=[]
                    corr_factor = 0
                    for idx, m in enumerate(re.finditer(REGEX_UG_CHORD, line)):
                        pairs.append((m.start()-corr_factor+idx +1,Chord(m.group(0), input_mode='english')))
                        #corr_factor += len(m.group(0))

                else:

                    line_data = {'mode':env, 'lyrics':self.remove_double_spaces(line.lstrip()), 'chords': line_chords, 'pos_crd_pairs': pairs}
                    if next_line_is_first_of_env:
                        line_data['is_first'] = True
                        lm = lm._replace(firstline=True)
                        next_line_is_first_of_env = False
                    else:
                        line_data['is_first'] = False
                        lm = lm._replace(firstline=False)

                    line_data.update(mode=env, lyrics=self.remove_double_spaces(line.lstrip()), chords=line_chords, pos_crd_pairs=pairs, linemarker=lm, chords_above=True)
                    
                    self.song_body.append(line_data)

    def _read_chopro(self):

        self.song_body = []
        LineMarker = namedtuple('LineMarker', ['firstline', 'lastline'], defaults=(False, False))
        Line = namedtuple('Line', ['mode', 'linemarker', 'lyrics', 'chords', 'pos_crd_pairs','chords_above'], defaults=(None,None,None,None,None,None))
        linedata = Line()
        env = 'default'
        chords = []
        lm = LineMarker() # reset line marker

        for line in self.raw_text:
            line_data = dict()
            line = line.strip()
            if line:
                if re.match(REGEX_CHOPRO_META, line):
                    meta = re.match(REGEX_CHOPRO_META, line)
                    
                    setattr(self, meta[1], meta[2])

                    if hasattr(self, 'artist'):
                        setattr(self, 'band', self.artist)
                
                elif re.match(REGEX_CHOPRO_ENVIRONMENTS, line):
                    env_match = re.match(REGEX_CHOPRO_ENVIRONMENTS,line)

                    env_name = 'verse' if env_match[3] == 'v' else env_match[3]
                    env_name = 'chorus' if env_match[3] == 'c' else env_match[3]
                    env_name = 'bridge' if env_match[3] == 'b' else env_match[3]
                    env_name = 'tab' if env_match[3] == 't' else env_match[3]

                    if env_match[2] in ['start', 's']:
                        env = env_name
                        lm = lm._replace(firstline=True)

                    elif  env_match[2] in ['end','e']:
                        env = 'default'
                        lm = lm._replace(lastline=True)

                        if self.song_body[-1].get('linemarker',False).firstline:
                            lm = lm._replace(firstline=True)

                        self.song_body[-1].update(linemarker=lm)

                        lm = lm._replace(firstline=False)
                        lm = lm._replace(lastline=False)

                    else:
                        env = 'default'

                else:

                    pairs = []
                    if re.findall(REGEX_CHOPRO_CHORD, line):
                        corr_factor = 0
                        for idx, m in enumerate(re.finditer(REGEX_CHOPRO_CHORD, line)):
                            pairs.append((m.start() - corr_factor + idx, Chord(txt=m.group(1))))
                            corr_factor += len(m.group(0))

                        chords = re.findall(REGEX_CHOPRO_CHORD, line)
                        chords = [Chord(txt=c) for c in chords]
                   
                    lyrics = re.sub(REGEX_CHOPRO_CHORD, '', line).strip()

                    #chords = ' '.join(chords)

                    # line_data = {'mode': env, 'lyrics': lyrics, 'chords': chords, 'pos_crd_pairs': pairs}
                    # ------------------------------------------------------
                    line_chords_above = False # chords aside static (temp-dev solution)
                    line_data.update(mode=env, lyrics=lyrics, chords=chords, pos_crd_pairs=pairs, linemarker=lm, chords_above=line_chords_above)
                    # ------------------------------------------------------

                    self.song_body.append(line_data)
                    
                    # Reset vars
                    chords, lyrics, pairs = '','',''
                    lm = lm._replace(firstline=False, lastline=False)

                    # chords, lyrics, pairs = '','',''
                    
    def _read_latex_leadsheets(self):
        ''' read LaTeX (leadsheets) formated text and cast 
        self.song_lines'''
        self.song_body = []
        LineMarker = namedtuple('LineMarker', ['firstline', 'lastline'], defaults=(False, False))
        Line = namedtuple('Line', ['mode', 'linemarker', 'lyrics', 'chords', 'pos_crd_pairs','chords_above'], defaults=(None,None,None,None,None,None))
        linedata = Line()
        env = 'default'
        chords = []
        pairs=[]
        lm = LineMarker() # reset line marker

        for i,line in enumerate(self.raw_text):
            line_data = dict()
            line = line.strip()
            cnt = 0 # body line counter
            if line:
                line = self.decode_leadsheets(line)
                if re.match(REGEX_LEADSHEETS_CMD, line):
                    
                    if re.match(REGEX_LEADSHEETS_META_LINE, line):
                        meta = re.findall(REGEX_LEADSHEETS_ALL_META, line)

                        for m in meta:
                            setattr(self,m[0].replace('-', ''), m[1])
                    
                        # backward compatibility with chopro version
                        if hasattr(self, 'band'):
                                setattr(self, 'artist', self.band)

                    if re.match(REGEX_LEADSHEETS_ENVIRONMENTS, line):

                        # skip some envs not required and causing problems. NASTY WORKAROUND !
                        if re.match(REGEX_LEADSHEETS_ENVIRONMENTS,line)[2] not in ['diagrams']:
                            if re.match(REGEX_LEADSHEETS_ENVIRONMENTS, line)[1] == 'begin':
                                env = re.match(REGEX_LEADSHEETS_ENVIRONMENTS, line)[2]
                                lm = lm._replace(firstline=True)

                            elif re.match(REGEX_LEADSHEETS_ENVIRONMENTS, line)[1] == 'end':
                                env = 'default'
                                lm = lm._replace(lastline=True)
                                
                                if self.song_body[-1].get('linemarker',False).firstline:
                                    lm = lm._replace(firstline=True)
                                
                                self.song_body[-1].update(linemarker=lm)

                                lm = lm._replace(firstline=False)
                                lm = lm._replace(lastline=False)
                    

                # process non-command lines (should be text & chords)
                else:
                    
                    # if any of chords starts with ^ song is marked as 'chords above'
                    if re.findall(REGEX_LEADSHEETS_CHORD_ABOVE, line):
                        self.chords_above |= True
                        line_chords_above = True
                    else:
                        line_chords_above = False
                        
                    pairs = []
                    if re.findall(REGEX_LEADSHEETS_CHORD, line):
                        
                        corr_factor = 0
                        
                        for idx, m in enumerate(re.finditer(REGEX_LEADSHEETS_CHORD, line)):
                                pairs.append((m.start() - corr_factor + idx, Chord(txt=m.group(1), input_mode='english')))
                                corr_factor += len(m.group(0))
                        
                        chords = re.findall(REGEX_LEADSHEETS_CHORD, line)
                        chords = [Chord(txt=c, input_mode='english') for c in chords]

                    lyrics = re.sub(REGEX_LEADSHEETS_CHORD, '', line).replace('\\','').strip()
                    lyrics = re.sub(r'\s{2,}', ' ', lyrics)
                    
                    line_data.update(mode=env, lyrics=lyrics, chords=chords, pos_crd_pairs=pairs, linemarker=lm, chords_above=line_chords_above)
                    #linedata = linedata._replace(mode=env, lyrics=lyrics, chords=chords, pos_crd_pairs=pairs, linemarker=lm, chords_above=line_chords_above)
                    # write data to Song Object
                    self.song_body.append(line_data)

                    # Reset vars
                    chords, lyrics, pairs = '','',''
                    lm = lm._replace(firstline=False, lastline=False)

    def _read_koliba(self):
        self.song_body = []

        Line = namedtuple('Line', ['mode', 'linemarker', 'lyrics', 'chords', 'pos_crd_pairs','chords_above'], defaults=(None,None,None,None,None,None))
        linedata = Line()
        LineMarker = namedtuple('LineMarker', ['firstline', 'lastline'], defaults=(False, False))
        lm = LineMarker()
        for line in self.raw_text:
            line = line.strip()
            if line:
                if re.match(REGEX_KOLIBA_META, line):
                    tag = re.match(REGEX_KOLIBA_META, line)[1]
                    value = re.match(REGEX_KOLIBA_META, line)[2].strip()
                    if tag == 'capo':
                        value = self.roman2int(re.sub(r'Capo\s?', '', value).strip())
                    
                    if tag == 'author':
                        setattr(self, 'band', value)
                        setattr(self, 'artist', value)
                    else: 
                        setattr(self, tag, value)
                
                elif  re.match(REGEX_KOLIBA_ENVIRONMENTS, line):
                    env = re.match(REGEX_KOLIBA_ENVIRONMENTS, line)[1].lower()
                    next_line_is_first_of_env = True
                
                else:
                    if re.match(REGEX_KOLIBA_CHORDS,line):
                        chords = re.match(REGEX_KOLIBA_CHORDS,line)[2].strip()
                        lyrics = re.match(REGEX_KOLIBA_CHORDS,line)[1].strip()
                        chords = self.remove_double_spaces(chords).split(' ')
                        lyrics = self.remove_double_spaces(lyrics)
                        
                        #create Chord objects
                        line_chords = [Chord(txt=c, input_mode='german') for c in chords]
                        pairs = [(-1, crd) for crd in line_chords]
                        
                    else: #no chords, only lyrics
                        line_chords = ''
                        pairs = ''
                        lyrics = line.strip()

                    line_data = {'mode':env, 'lyrics':lyrics, 'chords': chords, 'pos_crd_pairs': pairs}

                    if next_line_is_first_of_env:
                        line_data['is_first'] = True
                        lm = lm._replace(firstline=True)
                        next_line_is_first_of_env = False
                    else:
                        line_data['is_first'] = False
                        lm = lm._replace(firstline=False)

                    line_data.update(mode=env, lyrics=lyrics, chords=line_chords, pos_crd_pairs=pairs, linemarker=lm, chords_above=False)
                    
                    self.song_body.append(line_data)
                
    def _read_wywrota(self):
        self.song_body = []

        soup = BeautifulSoup('\n'.join(self.raw_text), 'html5lib')
        self.title, self.band = [meta for meta in soup.find('h1').stripped_strings]
        
        content = soup.find('div', 'interpretation-content').contents

        prev_line_type = None
        lyrics, chords = '',[]

        for line in content:
            if isinstance(line, NavigableString) and line.strip():
                if prev_line_type in (NavigableString, Tag):
                    if line.name != 'br':
                        
                        chords = [Chord(txt=c, input_mode='german') for c in chords]
                        pairs = [(-1, crd) for crd in chords]
                        env = 'verse'
                        line_data = {'mode': env, 'lyrics': lyrics, 'chords': chords, 'pos_crd_pairs': pairs}
                        self.song_body.append(line_data)

                        lyrics, chords = '',[]

                lyrics += line.strip()
                prev_line_type = type(line)

            elif isinstance(line, Tag):
                if line.name == 'code':
                    chords.append(line['data-local'])
                    prev_line_type = type(line)


    @property
    def lyrics_line_max_len(self):
        #return max([len(line['lyrics']) for line in self.song_body if line['mode'] != 'tabs'])
        l = []
        for line in self.song_body:
            if line['mode'] not in ['tabs', 'comment', 'diagrams']:
                l.append(len(line['lyrics']))
        return max(l)

    def align_chords_tabulator(self, line):
        # {'mode':env, 'lyrics':line.lstrip(), 'chords': line_chords, 'pos_crd_pairs': pairs}
        #crds = ' '.join([f'[{c}]' for c in line['chords']])
        #return [line['lyrics'].ljust(self.lyrics_line_max_len + 5) + crds for line in self.song_body]
        pass
    
    def _to_ug(self, chords_above=False):
        return 'convertion to UG format not implemented'

    def _to_chopro(self, chords_above=False):
        TEMPLATE_ENV_BEGIN = Template('{start_of_$env}\n')
        TEMPLATE_ENV_END = Template('{end_of_$env}\n')
        TEMPLATE_HEADER = Template('{artist: $artist}\n{title: $title}\n')
        TEMPLATE_CAPO = Template('{capo: $capo}\n')
        txt = TEMPLATE_HEADER.safe_substitute(artist=self.band, title=self.title)
        if self.capo:
            txt += TEMPLATE_CAPO.safe_substitute(capo=self.capo) if int(self.capo) else ''
        prev_mode = 'default'
        for line in self.song_body:
            line["chords"] = [c._to_chopro() for c in line["chords"]]
            line['pos_crd_pairs'] = [(pcp[0], pcp[1]._to_chopro()) for pcp in line['pos_crd_pairs']]
            
            # chopro does not have interlude, hence:
            line['mode'] = 'bridge' if line['mode'] == 'interlude' else line['mode']
            line['mode'] = 'tab' if line['mode'] == 'tabs' else line['mode']
            line['mode'] = 'grid' if line['mode'] == 'diagrams' else line['mode']
            line['mode'] = 'verse' if line['mode'] == 'intro' else line['mode']

            if line['mode'] != 'default':
                # if prev_mode != line['mode']:
                if line['linemarker'].firstline:
                    if prev_mode != 'default':
                        txt += TEMPLATE_ENV_END.safe_substitute(env=prev_mode)
                    
                    txt += TEMPLATE_ENV_BEGIN.safe_substitute(env=line['mode'])
                    prev_mode = line['mode']
                
                crds = ' '.join([self.wrap_chord(c,'chopro') for c in line['chords']])
                
                if chords_above:
                    txt += self.merge_chords_and_lyrics(lyricsline=line['lyrics'],pairs=line['pos_crd_pairs'], chord_format='chopro')
                    txt += '\n'

                else:
                    txt += f'{line["lyrics"].ljust(self.lyrics_line_max_len + 5)}{crds}\n'
                    
        txt += TEMPLATE_ENV_END.safe_substitute(env=prev_mode)
        
        return txt

    def _to_leadsheets(self, chords_above=False):
        
        TEMPLATE_ENV_BEGIN = Template('\\begin{$env}\n')
        TEMPLATE_ENV_END = Template('\\end{$env}\n')
        TEMPLATE_SONG_BEGIN= Template('\\begin{song}{title={$title},band={$artist}$other_properties}\n')
        
        other_properties = ''
        if hasattr(self, 'capo') and self.capo:
            tmp_property = Template(',capo={$property}')
            other_properties += tmp_property.safe_substitute(property=self.capo)
        elif hasattr(self, 'key') and self.key:
            k = Chord(self.key, input_mode='english')._to_tex()
            tmp_property = Template(',key={$property}')
            other_properties += tmp_property.safe_substitute(property=k)

        txt = '\\newpage\n'
        txt += TEMPLATE_SONG_BEGIN.safe_substitute(title=self.title, artist=self.band, other_properties=other_properties)

        prev_mode = 'default'
        for line in self.song_body:
            line["chords"] = [c._to_tex() for c in line["chords"]]
            line['pos_crd_pairs'] = [(pcp[0], pcp[1]._to_tex()) for pcp in line['pos_crd_pairs']]
            
            line['mode'] = 'tabs' if line['mode'] == 'tab' else line['mode']
            # if prev_mode != line['mode']:
            if line['linemarker'].firstline:
            # if line['is_first']:
                if prev_mode != 'default':
                    txt += TEMPLATE_ENV_END.safe_substitute(env=prev_mode)
                
                txt += TEMPLATE_ENV_BEGIN.safe_substitute(env=line['mode'])
                prev_mode = line['mode']

            f = 'leadsheets_above' if chords_above else 'leadsheets'
            crds = ' '.join([self.wrap_chord(c,f) for c in line['chords']])
            
            if chords_above:
                txt += self.merge_chords_and_lyrics(lyricsline=line['lyrics'],pairs=line['pos_crd_pairs'], chord_format='leadsheets_above')
                txt += ' \\\\\n'
            else:
                
                txt += f'{line["lyrics"]}'
                txt += f' \\tab{crds} \\\\\n' if crds.strip() else f' \\\\\n' 


        txt += TEMPLATE_ENV_END.safe_substitute(env=prev_mode)
        txt += '\\end{song}'
        txt = self.__fix_last_section_line(txt)
        
        return txt

    def _to_songs(self, chords_above=False):
        TEMPLATE_ENV_BEGIN = Template('\\begin$env\n')
        TEMPLATE_ENV_END = Template('\\end$env\n')
        TEMPLATE_SONG_BEGIN= Template('\\beginsong{title=$title}[by=$artist]\n')
        
        txt = TEMPLATE_SONG_BEGIN.safe_substitute(title=self.title, artist=self.band)
        if hasattr(self, 'capo') and self.capo:
            txt += '\capo{' + self.capo + '}\n'

        
        prev_mode = 'default'
        for line in self.song_body:
            line["chords"] = [c._to_tex_songs() for c in line["chords"]]
            line['pos_crd_pairs'] = [(pcp[0], pcp[1]._to_tex_songs()) for pcp in line['pos_crd_pairs']]
            
            line['mode'] = 'tabs' if line['mode'] == 'tab' else line['mode']
            if prev_mode != line['mode']:
                if prev_mode != 'default':
                    txt += TEMPLATE_ENV_END.safe_substitute(env=prev_mode)
                
                txt += TEMPLATE_ENV_BEGIN.safe_substitute(env=line['mode'])
                prev_mode = line['mode']

            
            crds = ' '.join([self.wrap_chord(c,'songs') for c in line['chords']])
            
            if chords_above:
                txt += self.merge_chords_and_lyrics(lyricsline=line['lyrics'],pairs=line['pos_crd_pairs'], chord_format='songs')
                txt += '\n'
            else:
                txt += f'{line["lyrics"]} \\tab{crds}\n'

        txt += TEMPLATE_ENV_END.safe_substitute(env=prev_mode)
        txt += '\\endsong'

        return txt

    def _to_koliba(self, *args, **kwargs):

        skip_envs = ['tab', 'tabs', 'diagrams', 'info']
        sng = f'#title {self.title}\n#author {self.band}\n#category Piosenki różne\n'
        if self.capo and int(self.capo) != 0:
            sng += f'#capo Capo {self.number2roman(int(self.capo))}\n'
        
        prev_mode='default'
        for line in self.song_body:
            line["chords"] = [c._to_hk() for c in line["chords"]]
            if line['mode'] != 'default':
                if prev_mode != line['mode']:
                    if line['mode'] not in skip_envs:
                        mode = 'chorus' if line['mode'] in ['chorus','bridge','interlude'] else 'verse'
                        
                        sng += f'\n#{mode}\n'
                        
                        chords = f'~ {" ".join(line["chords"])}' if line["chords"] else '' 
                        sng += f'{line["lyrics"]} {chords}\n'
                        
                        prev_mode = line['mode']
                else:
                    chords = f'~ {" ".join(line["chords"])}' if line["chords"] else '' 
                    sng += f'{line["lyrics"]} {chords}\n'

                chords = ''        

        return sng

    def number2roman(self, num):
        return self.frets[num]

    def roman2int(self, roman):
        return self.frets.index(roman)
    
    @staticmethod
    def remove_double_spaces(txt):
        return re.sub(r'\s{2,}',' ',txt)

    @staticmethod
    def decode_leadsheets(txt):
        '''converts leadsheets specific typesetting macros to plain text'''
        
        txt = re.sub(r'\\ldots','...' ,txt)
        txt = re.sub(r'\$\\times\s+(\d)\$','x\g<1>' ,txt)
        txt = re.sub(r'\\say\{(.*?)\}', '"\g<1>"', txt)
        txt = re.sub(r'\\normalbar','|',txt)
        txt = re.sub(r'\\stopbar','||',txt)
        
        txt = re.sub(r'\\tabto\{.*?\}|\\tab','',txt)
        txt = re.sub(r'\\hfill','',txt)
        txt = re.sub(r'\\remark\{(.*?)\}','\g<1>',txt)
        txt = re.sub(r'\s*?\\\\$','',txt) # excess spaces
        txt = re.sub(r'^\s*?%.*$','',txt) # commented lines
        return txt

    @staticmethod
    def __fix_last_section_line(txt):
        '''remove double slashes from each last line of section'''
        t_list = txt.split('\n')
        pattern = re.compile(r'\s*[\\\\]{2}\s*$')
        for line in enumerate(t_list):
            if re.match(REGEX_LEADSHEETS_ENVIRONMENTS, line[1]):
                t_list[line[0]-1] = re.sub(pattern,'',t_list[line[0] -1 ])

        return '\n'.join(t_list)

    def convert(self, to_format, chords_above=False):
        '''
        0 - Ultimate Guitar
        1 - ChordPro
        2 - LaTeX ('Leadsheets' package, not 'Songs' !!)
        3 - (in future, not yet) - LaTeX (Songs Package)
        4 - .sng (Proprietary format used in Hawiarska Koliba songbook)
        '''
        
        if to_format == 0: 
            output = self._to_ug(chords_above=chords_above)
        
        elif to_format == 1: 
            output = self._to_chopro(chords_above=chords_above)
        
        elif to_format == 2: 
            output = self._to_leadsheets(chords_above=chords_above)

        elif to_format == 3: 
            output = self._to_songs(chords_above=chords_above)
        
        elif to_format == 4: 
            output = self._to_koliba(chords_above=chords_above)
        
        else: 
            output = 'ERROR! unknown option'

        return output

    def wrap_chord(self, crd, f):
        '''simple wrapper for chords in various formats'''

        if f=='leadsheets':
            crd = '_{' + crd + '}'

        elif f=='leadsheets_above':
            crd = '^{' + crd + '}'

        elif f=='chopro':
            crd = f'[{crd}]'

        elif f=='songs':
            crd = f'\[{crd}]'

        else:
            pass

        return crd

    def merge_chords_and_lyrics(self, lyricsline, pairs, chord_format):
        ll = list(lyricsline)
        for crd in pairs:
            ll.insert(crd[0], self.wrap_chord(crd=crd[1], f=chord_format))
        
        return ''.join(ll)

    @property
    def save_as(self):
        ''' returns filename cast from bandname and artist w/o extention'''
        fname = f'{self.band} {self.title}'.lower().strip()
        fname = re.sub(r'\s{2,}|\s-\s',' ',fname)
        fname = re.sub(r'\s+','-',fname)
        fname = re.sub(r'|^-$','',fname)
        fname = re.sub(r'\.|\,|\'|\?','',fname)
        fname = unidecode(fname)

        return fname

def TEST_WYWROTA():
    with open(file='..\dev\wywrota_parser_dev\dump.html', mode='r', encoding='utf-8') as f:
        html = f.read()

    from pprint import pprint
    song = Song(raw_text=html, input_format=5)
    pprint(song._to_chopro())

def dev_slashes():
    with open(file='d:/00_CLOUD/Dropbox/99.TEMP_non_public/PROGRAMMING/python/projects/SONGBOOK-LaTex/data/songs-dev/99_TEST/.sng/Cień w dolinie mgieł.sng', mode='r', encoding='utf-8') as f:
        data = f.read()
    song=Song(raw_text=data, input_format=4)
    txt = song.convert(to_format=2)

def test_ug():
    with open(file='D:/00_CLOUD/Dropbox/99.TEMP_non_public/PROGRAMMING/python/projects/ChordsConverter/dev/do_lata_ug.txt') as f:
        data = f.read()
        song = Song(raw_text=data, input_format=0)
        from pprint import pprint
        pprint(song.song_body)

if __name__ == '__main__':
    import os
    # print(os.getcwd())
    #test_ug()
    e = Example().chopro_test
    s = Song(raw_text=e, input_format=1)
    converted = s._to_leadsheets()
    print(converted)
# --------- TO DO/FIX -----------------------
    # _read_wywrota(self) - does not conider last line
    # _read_wywrota(self) - 
    # _read_wywrota(self) - add example
    # add _sanitize_input to remove all multi-spaces