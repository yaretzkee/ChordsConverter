import re
REGEX_UG_ENVIRONMENTS = re.compile(r'^\[(Whistle|Intro|Verse|Chorus|Pre-Chorus|Intro|Solo|Outro|Bridge|Interlude|Break)\s?(\d)?\]$', re.IGNORECASE)
REGEX_UG_CHORD = re.compile(r'(?<!\S)(([A-G]){1}(#|b)?(m?)?(?!aj)(\d)?(\/\d\-?)?(\+\-|sus|add|aug|maj|dim)?((#|b)?\d{1,2})?([\\\/][A-G]{1}(#|b)?)?)(?!\S)')
REGEX_UG_LYRICS = re.compile(r'\w')

DIRECTIVES = [
        'title', 'subtitle', 'artist', 'composer', 'lyricist', 'arranger',
        'copyright', 'album', 'year', 'key', 'time', 'tempo', 'duration',
        'capo', 'sortartist', 'chords_above']
COMMANDS_SUB_PATTERN = '|'.join(DIRECTIVES)
REGEX_CHOPRO_META = re.compile(r'(?:{)+(%s):?\s*(.*)(?:})' % COMMANDS_SUB_PATTERN, re.IGNORECASE)
REGEX_CHOPRO_ENVIRONMENTS = re.compile(r'(?:{)((start|end|s|e)_?of?_?(verse|chorus|bridge|tab|v|c|b|t))(?:})')
REGEX_CHOPRO_CHORD = re.compile(r'\[(.*?)\]')

REGEX_LEADSHEETS_CMD = re.compile(r'^\s*?\\.*$')
REGEX_LEADSHEETS_META_LINE = re.compile(r'(?:\\begin\{song\})')
REGEX_LEADSHEETS_ALL_META = re.compile(r'([a-z\-]+)=\{(.*?)\}')
REGEX_LEADSHEETS_ENVIRONMENTS = re.compile(r'^\s*?\\(begin|end)\{(verse|chorus|interlude|bridge|solo|intro|tabs|diagrams|info|comment)\}')
REGEX_LEADSHEETS_CHORD_ABOVE = re.compile(r'(\^)(\{.*?\})')
REGEX_LEADSHEETS_CHORD_INLINE = re.compile(r'\_\{(.*?)\}')
REGEX_LEADSHEETS_CHORD = re.compile(r'(?:\^|_|\\chord|\\writechord)\{(.*?)(?:\})')

REGEX_KOLIBA_META = re.compile(r'^#(title|author|category|capo)+(.*)$')
REGEX_KOLIBA_ENVIRONMENTS = re.compile(r'#(verse|chorus)')
REGEX_KOLIBA_CHORDS = re.compile(r'^(.*?)~(.*?)$')

# used in  Chord class to decompose chord for further processing
REGEX_CHORD = re.compile(r'\(?([a-hA-H]{1})([ie]?s|\#|b)?(?!us)(mi?)?(?!aj)(\d)?(\/\d\-?)?(\+|\-|sus|aug|maj|dim|add)?(\d)?([\\\/][A-H]{1})?\)?')
