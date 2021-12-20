import logging as log
import pathlib
import sys, os
sys.path.insert(0, '..')

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt, QFile

from src.gui import Designer
from src.examples import Example
from src.song import Song

os.chdir(pathlib.Path(__file__).parent)

designer = Designer()
is_uic = designer.build('uic','../src/main_window.ui', '../src/ui_mainwindow.py')
is_rcc = designer.build('rcc', '../img/icons.qrc', '../src/icons_rc.py')
from src.ui_mainwindow import Ui_MainWindow

log.basicConfig(
    level=log.WARNING,
    format='%(levelname)s: %(module)s.%(funcName)s(); Message: %(message)s')


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.is_init_completed = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.example = Example()

        # ------ EVENT Connections --------------------------------------------
        self._connect_events()
        # --------------------------------------------------------------------
        self._init_states()
        self.is_init_completed = True
        log.info('App __init__ COMPLETED!')

    def _connect_events(self):
        self.ui.text_in.textChanged.connect(self.onChange_text_in)

        self.ui.actionConvert.triggered.connect(self.onClickMenuConvert)
        self.ui.actionUltimate_Guitar.triggered.connect(self.menuExamples_ug)
        self.ui.actionChordPro.triggered.connect(self.menuExamples_chopro)
        self.ui.actionLaTeX_leadsheets.triggered.connect(self.menuExamples_latex_leadsheets)
        self.ui.actionLaTeX_songs.triggered.connect(self.menuExamples_latex_songs)
        self.ui.actionHK.triggered.connect(self.menuExamples_hk)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveAsFile)
        self.ui.chb_chords_above.stateChanged.connect(self.onChangeChordsAbove)

        self.ui.rb_in_ug.clicked.connect(self.__read_input_format)
        self.ui.rb_in_chopro.clicked.connect(self.__read_input_format)
        self.ui.rb_in_latex_leadsheets.clicked.connect(self.__read_input_format)
        self.ui.rb_in_latex_songs.clicked.connect(self.__read_input_format)
        self.ui.rb_in_hk.clicked.connect(self.__read_input_format)

        self.ui.rb_out_ug.clicked.connect(self.__read_output_format)
        self.ui.rb_out_chopro.clicked.connect(self.__read_output_format)
        self.ui.rb_out_latex_leadsheets.clicked.connect(self.__read_output_format)
        self.ui.rb_out_latex_songs.clicked.connect(self.__read_output_format)
        self.ui.rb_out_hk.clicked.connect(self.__read_output_format)

    def _init_states(self):
        self.input_format = 0
        self.ui.rb_in_ug.animateClick()
        self.ui.rb_out_latex_leadsheets.animateClick()
        self.ui.chb_chords_above.setChecked(False)
        self.chords_above = 0

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, "Open Image", ".", ("Songs (*.chopro *.crd *.tex *.sng, *.txt)"))
        ext = pathlib.PurePath(fname[0]).suffix
        with open(file=fname[0], mode='r', encoding='utf-8') as f:
            data = f.read()
        
        self.ui.text_in.setPlainText(data)

        if ext == '.tex':
            self.__selectInputRadioByIndex(2)
        elif ext == '.chopro':
            self.__selectInputRadioByIndex(1)
        elif ext == '.sng':
            self.__selectInputRadioByIndex(4)
        else:
            self.__selectInputRadioByIndex(0)

        log.debug(f'openinig file: {fname[0]}')

    def saveAsFile(self):
        formats = ['Ultimate Guitar (*.txt)', 'ChoPro (*.chopro', 'LaTeX (*.tex)','LaTeX sOngs (*.tex)' 'HK (*.sng)']

        fname = QFileDialog.getSaveFileName('Save as...', 'capotion', '.', formats[self.output_format])
        log.debug(f'Save as... {fname}')

    def __selectInputRadioByIndex(self, idx):
        if idx == 0:
            self.ui.rb_in_ug.animateClick()
        elif idx == 1:
            self.ui.rb_in_chopro.animateClick()
        elif idx == 2:
            self.ui.rb_in_latex_leadsheets.animateClick()
        elif idx == 3:
            self.ui.rb_in_latex_songs.animateClick()
        elif idx == 4:
            self.ui.rb_in_hk.animateClick()

    def menuExamples_ug(self):
        self.ui.rb_in_ug.animateClick()
        self.load_example(0)

    def menuExamples_chopro(self):
        self.ui.rb_in_chopro.animateClick()
        self.load_example(1)

    def menuExamples_latex_leadsheets(self):
        self.ui.rb_in_latex_leadsheets.animateClick()
        self.load_example(2)

    def menuExamples_latex_songs(self):
        self.ui.rb_in_latex_songs.animateClick()
        self.load_example(3)

    def menuExamples_hk(self):
        self.ui.rb_in_hk.animateClick()
        self.load_example(4)

    def load_example(self, song_format=None):
        if song_format != None:
            self.ui.text_in.setPlainText(self.example.frm(song_format))

            log.debug('')

    def _check_in_out(self):
        pass

    def __read_input_format(self, state):
        if self.ui.rb_in_ug.isChecked():
            self.input_format = 0
        elif self.ui.rb_in_chopro.isChecked():
            self.input_format = 1
        elif self.ui.rb_in_latex_leadsheets.isChecked():
            self.input_format = 2
        elif self.ui.rb_in_latex_songs.isChecked():
            self.input_format = 3
        elif self.ui.rb_in_hk.isChecked():
            self.input_format = 4
            

        rbs = [self.ui.rb_out_ug,self.ui.rb_out_chopro,self.ui.rb_out_latex_leadsheets,self.ui.rb_out_latex_songs,self.ui.rb_out_hk]
        rbs_states = [1,1,1,0,1]
        rbs_states[self.input_format] = False
        
        ''' THIS SHOULD BE REDESIGNED. SAMEOUTPUTS POSSIBLE FOR ABOVE/INLINE conversion eg. 
        # disable same output...
        for rb in rbs:
            idx = rbs.index(rb)
            rb.setEnabled(rbs_states[idx])

        # ...and select next one
        next_idx = ((self.input_format+1 -len(rbs)) % len(rbs))
        rbs[next_idx].setChecked(True) 
        '''

        self.convert()

        log.debug(f'self.input_format= {self.input_format}')

    def __read_output_format(self, state):
        if self.ui.rb_out_ug.isChecked():
            self.output_format = 0
        elif self.ui.rb_out_chopro.isChecked():
            self.output_format = 1
        elif self.ui.rb_out_latex_leadsheets.isChecked():
            self.output_format = 2
        elif self.ui.rb_out_latex_songs.isChecked():
            self.output_format = 3
        elif self.ui.rb_out_hk.isChecked():
            self.output_format = 4

        if self.output_format == 4:
            self.ui.chb_chords_above.setDisabled(True)
            self.ui.chb_chords_above.setChecked(False)
        else:
            self.ui.chb_chords_above.setDisabled(False)

        self.convert()

        log.debug(f'self.output_format= {self.output_format}')

    def onChangeChordsAbove(self, state):
        self.chords_above = state
        self.convert()
        log.debug(f'self.chords_above= {self.chords_above}')

    def onChange_text_in(self):
        pass

    def onClickMenuConvert(self, status):
        self.convert()

    def convert(self):
        if self.is_init_completed:
            log.debug(
                f'Convert triggered with options: IF: {self.input_format}   OF: {self.output_format}')
            self.ui.statusbar.showMessage('converting', timeout=3000)
            in_txt = self.ui.text_in.toPlainText()
            if len(in_txt) > 3:

                try:
                    s = Song(raw_text=in_txt, input_format=self.input_format)
                    out_txt = s.convert(to_format=self.output_format, chords_above=self.chords_above)
                except (UnboundLocalError, AttributeError):
                    out_txt = 'ERROR!'
                    self.ui.statusbar.showMessage('ERROR!', timeout=3000)
                else:
                    pass
                finally:
                    self.ui.text_out.setPlainText(out_txt)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    QtGui.QFontDatabase.addApplicationFont("RobotoMono-VariableFont_wght.ttf")

    res = pathlib.Path('../res/style.qss')
    with open(res, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
