import logging as log
import re
import sys
sys.path.insert(0, '..')

from src.regex_patterns import *

# this class needs to be updated to new version (the one from flask App)
class Chord:
    '''class decodes chord from txt format and '''
    def __init__(self, txt, **kwargs):
        self.txt = txt
        if 'input_mode' in kwargs:
            self.input_mode = kwargs['input_mode']
        self._decode()


    def __str__(self):
        return self._merge_fractions()
    def __repr__(self):
        return self._merge_fractions()
    def _merge_fractions(self):
        self.chord_fractions = [self.root, self.semitone, self.minor, self.ext1, self.ext2, self.ext3, self.ext4, self.ext5]
        s = [f for f in self.chord_fractions if f]
        return ''.join([str(g) for g in s])
    
    def guess_input_mode(self):
        g_conditions = [self.root.islower(), self.root.upper() == 'H', self.semitone in ['is', 'es'], self.ext1 in ['0', '2', '4'], self.ext3=='+']
        e_conditions = [self.minor == 'm', self.ext3 in ['maj', 'dim', 'aug', 'sus', 'add'], self.semitone in ['b', '#']]
        if not hasattr(self, 'input_mode'):
            if any(g_conditions):
                return 'german'
            elif any(e_conditions):
                return 'english'
            else:
                return 'unknown'
        else:
            return self.input_mode

    def _decode(self):
        '''decodes chord based on txt.  '''
        c = re.match(REGEX_CHORD, self.txt)
        self.root, self.semitone, self.minor, self.ext1, self.ext2, self.ext3, self.ext4, self.ext5 = c.groups()
    
        self.input_mode = self.guess_input_mode() # 'german'|'english'|'unknown'

        if self.minor:
            self.minor = 'm' if self.minor == 'mi' else self.minor
        else:
            if self.root.islower():
                self.root = self.root.upper()
                self.minor = 'm'
    
        if self.ext1 in ['2', '4']:
            self.root = self.root.upper()
            self.minor = ''
            self.ext3, self.ext4 = 'sus', self.ext1
            self.ext1 = ''
        
        # handle diminished & half-deminished
        elif self.ext1 == '0':
            if self.minor: 
                self.ext1 = '7'
                self.ext2 = 'b5'
            else:
                self.ext1 = ''
                self.ext3 = f'dim'

        if self.ext1:
            if self.ext1.isnumeric() and self.ext3 == '+':
                self.ext3 = 'maj'
                self.ext4, self.ext1 = self.ext1, ''

        # handle 7sus
        if self.ext2:
            if re.match(r'\/(\d)',self.ext2):
                n = re.match(r'\/(\d)',self.ext2)[1]  
                self.ext3 = f"sus{n}"
                self.ext2 = ''

        # handle semitones/enharmonics
        if self.semitone in ['is']:
            self.semitone = '#'
        elif self.semitone in ['es', 's']:
            self.semitone = 'b'

        if self.input_mode == 'german':
            if self.root == 'H':
                self.root = 'B'
            elif self.root == 'B':
                self.semitone = 'b'
        
        elif self.root == 'B':
            if self.input_mode == 'unknown':
                log.warning('cannot define input notation. Chord might be "B" or "Bb"')

    def _to_tex(self):
        '''converts Xm -> Xmi'''
        self.minor = 'mi' if self.minor == 'm' else ''
        return self._merge_fractions()

    def _to_tex_songs(self):
        if self.semitone == 'b':
            self.semitone = '&'
        
        return self._merge_fractions()

    def _to_chopro(self):
        '''once self._decode is deployed, chord elements are stored in .chopro format (w/o brackets)'''
        return self._merge_fractions()

    def _to_hk(self):
        '''converts "english" notation to "german"
        (lowercase minor, is/es -> #/b, h->b, maj -> "+" etc.'''
        if self.root == 'B':
            if self.semitone == 'b':
                self.root, self.semitone = 'B', None
            elif not self.semitone:
                self.root = 'H'
        
        if self.semitone:
            if self.root == 'A':
                self.semitone = self.semitone.replace('b','s')
            self.semitone = self.semitone.replace('#','is').replace('b','es')

        if self.minor:
            self.root, self.minor = self.root.lower(), ''

        if self.ext3 == 'sus':
            self.ext3 = ''
            self.ext1, self.ext4 = self.ext4, ''

        elif self.ext3 == 'maj':
            self.ext3 = '+'
            self.ext1, self.ext4 = self.ext4, ''   
        
        elif self.ext3 == 'dim':
            self.ext3 = ''
            self.ext1 = '0'

        elif self.ext2 == 'b5' and self.ext1 == '7':
            self.root.lower()
            self.ext2 = ''
            self.ext1 = '0'
        return self._merge_fractions()     

def test():
    chords = ['H7', 'h7', 'B6','Fis7', 'Cm', 'Am7', 'D4', 'a2', 'G0', 'Fmaj7','Cadd9','E7+', 'a', 'Bbm', 'F#m']
    chords = ['a0', 'G0', 'Am7b5', 'A7/4','(Am)', 'Emadd9', 'Cmaj7(#11)']

    for crd in chords:
        c = Chord(crd)
        print(f'{crd}\t-->\t{c}\t{c.input_mode}\t{c._to_hk()}\t{c.semitone}')

if __name__ == '__main__':
    test()

    