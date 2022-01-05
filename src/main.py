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
is_uic = designer.build('uic','main_window.ui', 'ui_mainwindow.py')
is_rcc = designer.build('rcc', '../img/icons.qrc', 'icons_rc.py')
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
        self.last_used_filepath = None

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
        self.ui.btn_chords_above.toggled.connect(self.onChangeChordsAbove)
        self.ui.cbx_input_format.currentIndexChanged.connect(self.__read_input_format)
        self.ui.cbx_output_format.currentIndexChanged.connect(self.__read_output_format)

    def _init_states(self):
        self.input_format = 0
        self.ui.cbx_input_format.setCurrentIndex(0)
        self.ui.cbx_output_format.setCurrentIndex(2)
        self.ui.btn_chords_above.setChecked(False)
        self.chords_above = 0

    def openFile(self):
        if not self.last_used_filepath:
            self.last_used_filepath ='..'

        fname = QFileDialog.getOpenFileName(self, 
            caption="Open song file",
            dir=self.last_used_filepath,
            filter=("Songs (*.chopro *.crd *.tex *.sng *.txt)"))

        self.last_used_filepath = pathlib.PurePath(fname[0]).parent.as_posix()
        ext = pathlib.PurePath(fname[0]).suffix
        try:
            with open(file=fname[0], mode='r', encoding='utf-8') as f:
                data = f.read()
        
        except FileNotFoundError:
            log.warning('File opening failed.')
        
        else:
            self.ui.text_in.setPlainText(data)

            if ext == '.tex':
                self.ui.cbx_input_format.setCurrentIndex(2)

            elif ext == '.chopro':
                self.ui.cbx_input_format.setCurrentIndex(1)

            elif ext == '.sng':
                self.ui.cbx_input_format.setCurrentIndex(4)

            else:
                self.ui.cbx_input_format.setCurrentIndex(0)

            log.debug(f'openinig file: {fname[0]}')

    def saveAsFile(self):
        formats = ['Ultimate Guitar (*.txt)', 'ChoPro (*.chopro', 'LaTeX (*.tex)','LaTeX sOngs (*.tex)' 'HK (*.sng)']

        fname = QFileDialog.getSaveFileName('Save as...', 'capotion', '.', formats[self.output_format])
        log.debug(f'Save as... {fname}')
# ------------------------------------------------------------------------------
    def menuExamples_ug(self):
        self.load_example(0)

    def menuExamples_chopro(self):
        self.load_example(1)

    def menuExamples_latex_leadsheets(self):
        self.load_example(2)

    def menuExamples_latex_songs(self):
        self.load_example(3)

    def menuExamples_hk(self):
        self.load_example(4)
# ------------------------------------------------------------------------------
    def load_example(self, song_format=None):
        if song_format != None:
            self.ui.text_in.setPlainText(self.example.frm(song_format))
            self.ui.cbx_input_format.setCurrentIndex(song_format)
            self.convert()
            log.debug('')

    def _check_in_out(self):
        pass

    def __read_input_format(self, idx):
        self.input_format = idx
        self.convert()

        log.debug(f'self.input_format= {self.input_format}')

    def __read_output_format(self, idx):
        # use Combobox to set format
        self.output_format = idx

        if self.output_format == 4:
            self.ui.btn_chords_above.setDisabled(True)
            self.ui.btn_chords_above.setChecked(False)

        else:
            self.ui.btn_chords_above.setDisabled(False)

        self.convert()

        log.debug(f'self.output_format= {self.output_format}')
    
    def onChangeChordsAbove(self, checked):
        self.chords_above = checked
        log.debug(f'self.chords_above= {self.chords_above}')
        self.convert()

    def onChange_text_in(self):
        pass

    def onClickMenuConvert(self, status):
        self.convert()

    def convert(self):
        if self.is_init_completed:
            log.debug(f'Convert triggered with options: IF: {self.input_format}   OF: {self.output_format}')
            self.ui.statusbar.showMessage('converting', timeout=3000)
            in_txt = self.ui.text_in.toPlainText()
            if len(in_txt) > 3:
                try:
                    s = Song(raw_text=in_txt, input_format=self.input_format)
                    out_txt = s.convert(to_format=self.output_format, chords_above=self.chords_above)
                
                except (UnboundLocalError, AttributeError) as err:
                    log.error(err)
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
