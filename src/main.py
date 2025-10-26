import logging as log
import pathlib
import sys, os
sys.path.insert(0, '..')

from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QRegularExpression, QRegularExpressionMatch, Qt, QFile, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest

try:
    from src.gui import Designer
    from src.examples import Example
    from src.song import Song
    from src.config import Config
except ModuleNotFoundError:
    from gui import Designer
    from examples import Example
    from song import Song
    from config import Config

os.chdir(pathlib.Path(__file__).parent)

config = Config().config

designer = Designer()
if config.runtime.compile_ui:
    is_uic = designer.build('uic','main_window.ui', 'ui_mainwindow.py')

if config.runtime.compile_qrc:
    is_rcc = designer.build('rcc', '../img/icons.qrc', 'icons_rc.py')

try:
    from src.ui_mainwindow import Ui_MainWindow
except ModuleNotFoundError:
    from ui_mainwindow import Ui_MainWindow

from config import Config
log.basicConfig(
    level=log.DEBUG,
    format='%(levelname)s: %(module)s.%(funcName)s(); Message: %(message)s')


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication) -> None:
        super(MainWindow, self).__init__()
        self.app = app
        self.is_init_completed = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.example = Example()
        self.last_used_filepath = None
        self.config = Config().config
        # ------ EVENT Connections --------------------------------------------
        self._connect_events()
        # --------------------------------------------------------------------
        
        # ------- SET VALIDATORS ----------------------------------------------
        self.url_validator = QRegularExpressionValidator()
        self.url_validator.setRegularExpression(r'(https://)?(spiewnik\.wywrota\.pl/)(.*)')
        self.ui.le_URL.setValidator(self.url_validator)
        # ---------------------------------------------------------------------
        self.network_manager = QNetworkAccessManager()

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
        self.ui.le_URL.returnPressed.connect(self.__read_URL)
        
        # Theme menu connections
        self.ui.actionTheme_Light.triggered.connect(self.onThemeLight)
        self.ui.actionTheme_Dark.triggered.connect(self.onThemeDark)
        self.ui.actionTheme_OS.triggered.connect(self.onThemeOS)
        
        # Synchronize scroll bars between input and output text boxes
        self.ui.text_in.verticalScrollBar().valueChanged.connect(self._sync_scroll_to_output)
        self.ui.text_out.verticalScrollBar().valueChanged.connect(self._sync_scroll_to_input)
        self._is_syncing_scroll = False  # Flag to prevent infinite loop

    def _init_states(self):
        self.input_format = 0
        self.ui.cbx_input_format.setCurrentIndex(0)
        self.ui.cbx_output_format.setCurrentIndex(2)
        self.ui.btn_chords_above.setChecked(False)
        self.chords_above = 0
        self.ui.le_URL.hide()
        self.ui.actionExaples.setChecked(self.config.gui.examples_toolbar)
        
        # Set all splitters to 50/50 split
        window_width = self.width()
        half_width = window_width // 2
        self.ui.splitter_comboboxes.setSizes([half_width, half_width])
        self.ui.splitter_row2.setSizes([half_width, half_width])
        self.ui.splitter.setSizes([half_width, half_width])
        
        # Connect splitter movements to synchronize them
        self.ui.splitter_comboboxes.splitterMoved.connect(self._sync_splitters_from_comboboxes)
        self.ui.splitter_row2.splitterMoved.connect(self._sync_splitters_from_row2)
        self.ui.splitter.splitterMoved.connect(self._sync_splitters_from_main)

    def _sync_splitters_from_comboboxes(self, pos, index):
        sizes = self.ui.splitter_comboboxes.sizes()
        self.ui.splitter_row2.setSizes(sizes)
        self.ui.splitter.setSizes(sizes)
    
    def _sync_splitters_from_row2(self, pos, index):
        sizes = self.ui.splitter_row2.sizes()
        self.ui.splitter_comboboxes.setSizes(sizes)
        self.ui.splitter.setSizes(sizes)
    
    def _sync_splitters_from_main(self, pos, index):
        sizes = self.ui.splitter.sizes()
        self.ui.splitter_comboboxes.setSizes(sizes)
        self.ui.splitter_row2.setSizes(sizes)

    def openFile(self):
        if not self.last_used_filepath:
            self.last_used_filepath = pathlib.Path(self.config.folders.default_folder)
            if not self.last_used_filepath.exists():
                self.last_used_filepath = pathlib.Path('..')

        fname = QFileDialog.getOpenFileName(self, 
            caption="Open song file",
            dir=self.last_used_filepath.as_posix(),
            filter=("Songs (*.chopro *.crd *.tex *.sng *.txt)"))

        self.last_used_filepath = pathlib.PurePath(fname[0]).parent
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
        if not self.last_used_filepath:
            self.last_used_filepath = pathlib.Path(self.config.folders.default_folder)
            if not self.last_used_filepath.exists():
                self.last_used_filepath = pathlib.Path('..')

        formats = ['Ultimate Guitar (*.txt)', 'ChoPro (*.chopro', 'LaTeX (*.tex)','LaTeX sOngs (*.tex)','HK (*.sng)']
        saveDialog = QFileDialog(self)
        
        saveDialog.FileName =  self.saveas_fname if hasattr(self, 'saveas_fname') else ''
        
        fname = saveDialog.getSaveFileName(
            caption='Save as...',
            dir=self.last_used_filepath.joinpath(self.saveas_fname).as_posix(),
            filter=formats[self.output_format])
        self.last_used_filepath = pathlib.PurePath(fname[0]).parent
        try:
            with open(file=fname[0], mode='w', encoding='utf-8') as f:
                data = self.ui.text_out.toPlainText()
                f.write(data)
        
        except FileNotFoundError:
            log.warning('File save failed.')
        
        finally:
            log.debug(f'attempt to save file as: {fname}')
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
    
    def __read_URL(self):
        url = QUrl(self.ui.le_URL.text())
        self.__fetch_wywrota_html(url) # writes html to in_text window
        #self.convert()
        
        log.debug(self.url_validator.State())
        log.debug(url.isValid())
        log.debug(url.url())
    
    def __fetch_wywrota_html(self, url):
        def __finishedCallback():
            with open('..\dev\wywrota_parser_dev\dump.html', mode='w', encoding='utf-8') as f:
                html = str(resp.readAll(), 'utf-8')
                f.write(html)
            self.ui.text_in.setPlainText(html)
        
        req = QNetworkRequest(url)
        resp = self.network_manager.get(req)
        resp.finished.connect(__finishedCallback)

    def __read_input_format(self, idx):
        self.input_format = idx
        # if wywrota.pl do not convert immediately - wait for url input
        if self.input_format == 5: 
            self.ui.le_URL.show()
            self.ui.btn_chords_above.setDisabled(True)
            self.ui.btn_chords_above.setChecked(False)
        
        else:
            self.ui.le_URL.hide()
            self.ui.btn_chords_above.setDisabled(False)

            self.convert()

        log.debug(f'self.input_format= {self.input_format}')

    def __read_output_format(self, idx):
        # use Combobox to set format
        self.output_format = idx

        if self.output_format in (4,5):
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
                    self.saveas_fname = s.save_as

                except (UnboundLocalError, AttributeError) as err:
                    log.error(err)
                    out_txt = 'ERROR!'
                    self.ui.statusbar.showMessage('ERROR!', timeout=3000)
                
                else:
                    pass
                
                finally:
                    self.ui.text_out.setPlainText(out_txt)

    def onThemeLight(self):
        """Set Light theme"""
        self.ui.actionTheme_Light.setChecked(True)
        self.ui.actionTheme_Dark.setChecked(False)
        self.ui.actionTheme_OS.setChecked(False)
        
        # Apply light theme stylesheet
        light_style = """
        QMainWindow, QWidget {
            background-color: #ffffff;
            color: #000000;
        }
        QPlainTextEdit {
            background-color: #fffbdd;
            color: #000000;
            font-family: "Roboto Mono";
        }
        QMenuBar {
            background-color: #f0f0f0;
            color: #000000;
        }
        QMenuBar::item:selected {
            background-color: #e0e0e0;
        }
        QMenu {
            background-color: #ffffff;
            color: #000000;
        }
        QMenu::item:selected {
            background-color: #0078d4;
            color: #ffffff;
        }
        QComboBox {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #cccccc;
        }
        QLineEdit {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #cccccc;
        }
        QStatusBar {
            background-color: #f0f0f0;
            color: #000000;
        }
        QPushButton {
            background: rgba(65, 66, 66, 0);
        }
        QPushButton::checked {
            background: rgba(255, 0, 0, 0);
        }
        """
        self.app.setStyleSheet(light_style)
        log.info('Theme set to: Light')
    
    def onThemeDark(self):
        """Set Dark theme"""
        self.ui.actionTheme_Light.setChecked(False)
        self.ui.actionTheme_Dark.setChecked(True)
        self.ui.actionTheme_OS.setChecked(False)
        
        # Apply dark theme stylesheet
        dark_style = """
        QMainWindow, QWidget {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        QPlainTextEdit {
            background-color: #252526;
            color: #d4d4d4;
            font-family: "Roboto Mono";
        }
        QMenuBar {
            background-color: #2d2d30;
            color: #ffffff;
        }
        QMenuBar::item:selected {
            background-color: #3e3e42;
        }
        QMenu {
            background-color: #252526;
            color: #ffffff;
            border: 1px solid #3e3e42;
        }
        QMenu::item:selected {
            background-color: #094771;
            color: #ffffff;
        }
        QComboBox {
            background-color: #3c3c3c;
            color: #ffffff;
            border: 1px solid #555555;
        }
        QComboBox QAbstractItemView {
            background-color: #252526;
            color: #ffffff;
            selection-background-color: #094771;
        }
        QLineEdit {
            background-color: #3c3c3c;
            color: #ffffff;
            border: 1px solid #555555;
        }
        QStatusBar {
            background-color: #007acc;
            color: #ffffff;
        }
        QPushButton {
            background: rgba(65, 66, 66, 0);
            color: #ffffff;
        }
        QPushButton::checked {
            background: rgba(255, 0, 0, 0);
        }
        QToolBar {
            background-color: #2d2d30;
            border: none;
        }
        QSplitter::handle {
            background-color: #3e3e42;
        }
        """
        self.app.setStyleSheet(dark_style)
        log.info('Theme set to: Dark')
    
    def onThemeOS(self):
        """Set OS Preferred theme"""
        self.ui.actionTheme_Light.setChecked(False)
        self.ui.actionTheme_Dark.setChecked(False)
        self.ui.actionTheme_OS.setChecked(True)
        
        # Apply default/OS theme - load from style.qss file
        res = pathlib.Path('../res/style.qss')
        if res.exists():
            with open(res, "r") as f:
                _style = f.read()
                self.app.setStyleSheet(_style)
        else:
            # Fallback to minimal style
            minimal_style = """
            QPlainTextEdit {
                font-family: "Roboto Mono";
            }
            QPushButton {
                background: rgba(65, 66, 66, 0);
            }
            QPushButton::checked {
                background: rgba(255, 0, 0, 0);
            }
            """
            self.app.setStyleSheet(minimal_style)
        log.info('Theme set to: OS Preferred')

    def _sync_scroll_to_output(self, value):
        """Synchronize scrolling from input to output text box"""
        if self._is_syncing_scroll:
            return
        
        self._is_syncing_scroll = True
        try:
            # Get scroll bars
            input_scrollbar = self.ui.text_in.verticalScrollBar()
            output_scrollbar = self.ui.text_out.verticalScrollBar()
            
            # Calculate percentage of scroll position
            if input_scrollbar.maximum() > 0:
                scroll_percentage = value / input_scrollbar.maximum()
                # Apply same percentage to output
                new_value = int(scroll_percentage * output_scrollbar.maximum())
                output_scrollbar.setValue(new_value)
        finally:
            self._is_syncing_scroll = False
    
    def _sync_scroll_to_input(self, value):
        """Synchronize scrolling from output to input text box"""
        if self._is_syncing_scroll:
            return
        
        self._is_syncing_scroll = True
        try:
            # Get scroll bars
            input_scrollbar = self.ui.text_in.verticalScrollBar()
            output_scrollbar = self.ui.text_out.verticalScrollBar()
            
            # Calculate percentage of scroll position
            if output_scrollbar.maximum() > 0:
                scroll_percentage = value / output_scrollbar.maximum()
                # Apply same percentage to input
                new_value = int(scroll_percentage * input_scrollbar.maximum())
                input_scrollbar.setValue(new_value)
        finally:
            self._is_syncing_scroll = False


def main():
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    
    QtGui.QFontDatabase.addApplicationFont("RobotoMono-VariableFont_wght.ttf")

    res = pathlib.Path('../res/style.qss')
    with open(res, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())

def convSingleFile(song_path):
    with open(file=song_path, mode='r', encoding='utf-8') as f:
        raw_txt = f.read()
        s = Song(raw_text=raw_txt, input_format=2)
        k = s.convert(to_format=4)
    return k

if __name__ == '__main__':
    dropbox = pathlib.Path(os.getenv('dropbox'))
    fname = dropbox.joinpath('99.TEMP_non_public/PROGRAMMING/python/projects/SONGBOOK-LaTex/data/songs/songs-filip-all/08_Z_PRZYMRUŻENIEM_OKA/tomek-lewandowski-ale-leje.tex')
    with open(file=fname, mode='r', encoding='utf-8') as f:
        raw_txt = f.read()
    s = Song(raw_text=raw_txt, input_format=2)
    print(s._to_chopro())
    
    
    in_folder = dropbox.joinpath('99.TEMP_non_public/PROGRAMMING/python/projects/SONGBOOK-LaTex/data/songs')
    out_folder = pathlib.Path('../dev/output_koliba') 
    
    # for dname in sorted(in_folder.iterdir()):
    #     target_path = out_folder.joinpath(dname.stem)
    #     if not target_path.exists():
    #         target_path.mkdir(parents=True)

    #     for fname in dname.iterdir():
    #         with open(file=fname, mode='r', encoding='utf-8') as f:
    #             raw_txt = f.read()

    #         s = Song(raw_text=raw_txt, input_format=2)
    #         target_fname = f'{s.save_as}.sng'
    #         print(target_path.joinpath(target_fname))
    #         with open(file=target_path.joinpath(target_fname), mode='w', encoding='utf-8') as f:
    #             f.write(s.convert(to_format=4))