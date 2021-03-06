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
A je??li dom b??d?? mia??  ~ A h7 cis7 A7
to b??dzie bukowy koniecznie ~ D E9 A A7+
Pachn??cy i s??oneczny  ~ h7 E9 cis7 A7/4
wieczorem usi??d?? wiatr gra ~ D E4 E
A zegar na ??cianie gwarzy ~ A (A7) D E
Dobrze si?? idzie panie zegarze ~ A h7 cis7 a0
Tik tak tik tak tik tak ~ h7 E7 cis7 A7/4
??wieca skwierczy i mruga przewrotnie ~ D E7/4 E7
Wi??c puszczam oko do niej ~ A h7 cis7 a0
Dobry humor dzi?? pani ma ~ h7 E7 cis7 a0
Dobry humor dzi?? pani ma ~ h7 E7 A A4

#chorus
Szukam szukania mi trzeba ~ A E
Domu gitar?? i pi??rem ~ G D A
A g??ry nade mn?? jak niebo ~ A E
A niebo nade mn?? jak g??ry ~ G D d A A4 A

#verse
Gdy g??osy us??ysz?? u drzwi  ~ A h7 cis7 A7
czyjekolwiek wejd??cie poprosz?? ~ D E9 A A7+
Jestem zbieraczem g??os??w  ~ h7 E9 cis7 A7/4
a dom m??j bardzo lubi gdy ~ D E4 E
??miech ??ciany mu rozja??nia ~ A (A7) D E
I g??d??by lubi, pie??ni ~ A h7 cis7 a0
Wpadnijcie na par?? chwil ~ h7 E7 cis7 A7/4
Kiedy los was zawiedzie w te strony ~ D E7/4 E7
Bo dom m??j otworem stoi  ~ A h7 cis7 a0
Dla takich jak wy ~ h7 E7 cis7 a0
Dla takich jak wy ~ h7 E7 A A4

#chorus
Szukam szukania mi trzeba...

#verse
Zaprosz?? dzie?? i noc  ~ A h7 cis7 A7
zaprosz?? cztery wiatry ~ D E9 A A7+
Dla wszystkich drzwi otwarte,  ~ h7 E9 cis7 A7/4
kto?? poda pierwszy ton ~ D E4 E
Zagramy na g??ry koncert ~ A (A7) D E
Buk??w por?? pachn??c?? ~ A h7 cis7 a0
Nasi??kn?? ??ciany gr?? ~ h7 E7 cis7 A7/4
A zm??czonym w??drownikom ~ D E7/4 E7
Odpocz???? pozwol?? muzyk??  ~ A h7 cis7 a0
Bo taki b??dzie m??j dom ~ h7 E7 cis7 a0
Bo taki b??dzie m??j dom ~ h7 E7 A A4

#chorus
Szukam szukania mi trzeba...

'''

        self.chopro = r'''{artist: ChoPro 2 LaTeX Leadsheets}
{title: Python Converter - Chords Above}
{composer: Felipe & Co.}
{lyricist: Felipe - $ka} # must be sanitized. _ not allowed in leadsheets
{capo: 4}
{key: Bb}
{chords_above: True}
[C] [Cmaj7] [Am]

{start_of_verse}
[C]Ju?? wyros??em z [Bb]tych podchod??w [F]nastoletnich, [C]niedojrza??ych [G/B] [Am]       
[Am]Z romantycznych za[Em]chod??w i z uda[F]wania nie??[G]mia??ych
[F]Nie si??gam gdzie wzrok nie si??ga 
Bo od [C]wzroku kr??tsza [Am]r??ka
Co wie[Em]czorem i nad [Fmaj7]ranem si??gn???? [C]chce   [G] 
Po dobrze [F]znane [C]
{end_of_verse}
{start_of_chorus}
Si??gnij [F]po mnie jak si?? si??ga [C]po papieros
Si??gnij [F]po mnie tak jak ju?? si??gn????a?? [C]nieraz
Si??gnij [Am]po mnie i zaspok??j sw??j nie[Em7]pok??j
Si??gnij [F]po mnie po nie??wi??ty, ale [G]spok??j
Si??gnij [F]po mnie naturalnym przecie?? [C]gestem
Si??gnij [F]po mnie [Bdim]... bo pod [G]r??k??
Po to [F]jestem...[C] [Cmaj7] [G] [C]
{end_of_chorus}
{start_of_verse}
Te?? wyro??nij z udawania niedost??pnej i niewinnej
Do udawania Ci?? sk??ania co?? g??upiego niew??tpliwie
Si??gnij tam, gdzie wzrok ju?? dosi??g??
To jest nadzwyczajnie, to si??
W??a??nie po to tak sko??czy??o, ??eby mo??na
Nazwa?? to mi??o????
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