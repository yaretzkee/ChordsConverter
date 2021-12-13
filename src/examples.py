class Example:
    def __init__(self):

        self.latex_songs = ''
        self.ug = '''[Verse 1]
C
Silent night! Holy night!
G7           C
All is calm, all is bright


[Chorus]
F                 C
'Round yon virgin Mother and Child
F              C
Holy infant so tender and mild
G7                C
Sleep in heavenly peace
            G       C
Sleep in heavenly peace


[Verse 2]
C
Silent night, holy night!
G7              C
Shepherds quake at the sight!


[Chorus]
F                   C
Glories stream from heaven afar
F                   C
Heavenly hosts sing Alleluia!
G7                   C
Christ the Savior is born!
        G         C
Christ the Savior is born!


[Verse 3]
C
Silent night, holy night
G7          C
Son of God, love's pure light'''

        self.latex_leadsheets = r'''\newpage
\begin{song}{title={Sample Title of the song}, band={Band/artist Name}, music={music ComposerName}, lyrics={Lyrics AutrNamhoe},capo={2}}
\begin{intro}
\remark{scale}\\
_{A} _{Bmi} _{C#mi} _{D} _{E} _{F#mi} _{G#dim}
\end{intro}
\begin{multicols}{2}
    \begin{verse}
    ^{Fmaj7}Seen my share of^{C#sus2} bro^{Gbmi7(b5)}ken halos \\
    ^{Em7}Fold ^{Gdim}ed wings that ^{Csus2}used to ^{Csus4}fly \\
    ^{A7sus4}They've all gone ^{Csus2} wherever ^{G}they go \\
    ^{Emi7}Bro ^{G}ken halos that^{Csus2} used to s^{G#}hine 
\end{verse}
\begin{chorus}
    Text \chord{E7}text \chord{B7}lon ger text1 \\
    And some c^{fis7}hords beside text _{Esus4} _{E7} _{E#mi6} _{Ebmi9}
\end{chorus}
\columnbreak\vfill
\begin{verse} 
So this dummy  verse does containt all envs \\
Verse, chorus, gridge, interlude intro, solo \\
tabs, diagrams and even multicols \\
next verse will show more 
\end{verse}
\begin{solo}
and some SOLO env with chorsd _{Emi} \\
\end{solo}
\begin{bridge} 
    not a verse, just bridge \\
    some ldots \ldots - yes please \\
    time to loop than time $\times 3$ \\
    and quote wise words \say{well, seriiously?} 
\end{bridge}

\begin{interlude} 
    Seen my share of broken halos \\
    Folded wings that used to fly \\
    They've all gone  wherever they go \\
    Broken halos that used to shine 
\end{interlude}
\end{multicols}

\begin{tabs}
    E\normalbar---------------\normalbar---------------\normalbar----------------\normalbar----------------\stopbar \\      
    B\normalbar-----2--3--2---\normalbar-----2--3--2---\normalbar------2--3--2---\normalbar--------0--2--3-\stopbar \\
    G\normalbar-------------2-\normalbar-------------2-\normalbar--------------2-\normalbar----------------\stopbar \\
    D\normalbar---2-----------\normalbar---------------\normalbar----------------\normalbar----------------\stopbar \\
    A\normalbar-0-------------\normalbar---0-----------\normalbar---0------------\normalbar---0------------\stopbar \\
    E\normalbar---------------\normalbar-3-------------\normalbar-2--------------\normalbar-1----1---------\stopbar
\end{tabs}
\begin{diagrams}
    \gchord{t}{x,3,0,p0,p3,p3}{\chordname{Csus2}}
    \gchord{t}{x,3,0,p0,p3,p3}{\chordname{Csus2}}
\end{diagrams}

\end{song}
\begin{comment}
    E|---------------|---------------|----------------|----------------|| \\      
    B|-----2--3--2---|-----2--3--2---|------2--3--2---|--------0--2--3-|| \\
    G|-------------2-|-------------2-|--------------2-|----------------|| \\
    D|---2-----------|---------------|----------------|----------------|| \\
    A|-0-------------|---0-----------|---0------------|---0------------|| \\
    E|---------------|-3-------------|-2--------------|-1----1---------||
\end{comment}'''

        self.hk = '''#title Sielanka o domu
#author Wolna Grupa Bukowina
#category WGB
#capo Capo II
#verse
~ A A4 A A4

#verse
A jeśli dom będę miał  ~ A h7 cis7 A7
to będzie bukowy koniecznie ~ D E9 A A7+
Pachnący i słoneczny  ~ h7 E9 cis7 A7/4
wieczorem usiądę wiatr gra ~ D E4 E
A zegar na ścianie gwarzy ~ A (A7) D E
Dobrze się idzie panie zegarze ~ A h7 cis7 a0
Tik tak tik tak tik tak ~ h7 E7 cis7 A7/4
Świeca skwierczy i mruga przewrotnie ~ D E7/4 E7
Więc puszczam oko do niej ~ A h7 cis7 a0
Dobry humor dziś pani ma ~ h7 E7 cis7 a0
Dobry humor dziś pani ma ~ h7 E7 A A4

#chorus
Szukam szukania mi trzeba ~ A E
Domu gitarą i piórem ~ G D A
A góry nade mną jak niebo ~ A E
A niebo nade mną jak góry ~ G D d A A4 A

#verse
Gdy głosy usłyszę u drzwi  ~ A h7 cis7 A7
czyjekolwiek wejdźcie poproszę ~ D E9 A A7+
Jestem zbieraczem głosów  ~ h7 E9 cis7 A7/4
a dom mój bardzo lubi gdy ~ D E4 E
Śmiech ściany mu rozjaśnia ~ A (A7) D E
I gędźby lubi, pieśni ~ A h7 cis7 a0
Wpadnijcie na parę chwil ~ h7 E7 cis7 A7/4
Kiedy los was zawiedzie w te strony ~ D E7/4 E7
Bo dom mój otworem stoi  ~ A h7 cis7 a0
Dla takich jak wy ~ h7 E7 cis7 a0
Dla takich jak wy ~ h7 E7 A A4

#chorus
Szukam szukania mi trzeba...

#verse
Zaproszę dzień i noc  ~ A h7 cis7 A7
zaproszę cztery wiatry ~ D E9 A A7+
Dla wszystkich drzwi otwarte,  ~ h7 E9 cis7 A7/4
ktoś poda pierwszy ton ~ D E4 E
Zagramy na góry koncert ~ A (A7) D E
Buków porą pachnącą ~ A h7 cis7 a0
Nasiąkną ściany grą ~ h7 E7 cis7 A7/4
A zmęczonym wędrownikom ~ D E7/4 E7
Odpocząć pozwolą muzyką  ~ A h7 cis7 a0
Bo taki będzie mój dom ~ h7 E7 cis7 a0
Bo taki będzie mój dom ~ h7 E7 A A4

#chorus
Szukam szukania mi trzeba...

'''

        self.chopro = r'''{artist: ChoPro 2 LaTeX Leadsheets}
{title: Python Converter - Chords Above}
{composer: YARA & Co.}
{lyricist: Felipe - $ka} # must be sanitized. _ not allowed in leadsheets
{capo: 4}
{key: Bb}
{chords_above: True}
[C] [Cmaj7] [Am]

{start_of_verse}
[C]Już wyrosłem z tych podchodów [F]nastoletnich, [C]niedojrzałych [G/B] [Am]       
[Am]Z romantycznych za[Em]chodów i z uda[F]wania nieś[G]miałych
[F]Nie sięgam gdzie wzrok nie sięga 
Bo od [C]wzroku krótsza [Am]ręka
Co wie[Em]czorem i nad [Fmaj7]ranem sięgnąć [C]chce   [G] 
Po dobrze [F]znane [C]
{end_of_verse}
{start_of_chorus}
Sięgnij [F]po mnie jak się sięga [C]po papieros
Sięgnij [F]po mnie tak jak już sięgnęłaś [C]nieraz
Sięgnij [Am]po mnie i zaspokój swój nie[Em7]pokój
Sięgnij [F]po mnie po nieświęty, ale [G]spokój
Sięgnij [F]po mnie naturalnym przecież [C]gestem
Sięgnij [F]po mnie [Bdim]... bo pod [G]ręką
Po to [F]jestem...[C] [Cmaj7] [G] [C]
{end_of_chorus}
{start_of_verse}
Też wyrośnij z udawania niedostępnej i niewinnej
Do udawania Cię skłania coś głupiego niewątpliwie
Sięgnij tam, gdzie wzrok już dosięgł
To jest nadzwyczajnie, to się
Właśnie po to tak skończyło, żeby można
Nazwać to miłość
{end_of_verse}
{sot}
#        [A]             [G]             [F#]              [F]
E|---------------|---------------|----------------|----------------||
B|-----2-h3-p2---|-----2--3--2---|------2--3--2---|--------0\2---3-||
G|-------------2-|-------------2-|--------------2-|----------------||
D|---2-----------|---------------|----------------|----------------||
A|-0-------------|---0-----------|---0------------|---0------------||
E|---------------|-3-------------|-2--------------|-1----1---------||
{eot}
'''

    def frm(self, idx):
        return [self.ug, self.chopro, self.latex_leadsheets, self.latex_songs, self.hk][idx]