# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 660)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/logos/app_icon.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"    background:rgba(65,66,66, 0);\n"
"} \n"
"QPushButton::checked{\n"
"    background:rgba(255, 0, 0, 0);\n"
"}")
        MainWindow.setIconSize(QSize(30, 32))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/actions/folder_open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/actions/media-floppy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/actions/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionUltimate_Guitar = QAction(MainWindow)
        self.actionUltimate_Guitar.setObjectName(u"actionUltimate_Guitar")
        icon4 = QIcon()
        icon4.addFile(u":/examples/application-ug.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUltimate_Guitar.setIcon(icon4)
        self.actionChordPro = QAction(MainWindow)
        self.actionChordPro.setObjectName(u"actionChordPro")
        icon5 = QIcon()
        icon5.addFile(u":/examples/application-chopro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionChordPro.setIcon(icon5)
        self.actionLaTeX_leadsheets = QAction(MainWindow)
        self.actionLaTeX_leadsheets.setObjectName(u"actionLaTeX_leadsheets")
        icon6 = QIcon()
        icon6.addFile(u":/examples/application-x-tex.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLaTeX_leadsheets.setIcon(icon6)
        self.actionLaTeX_songs = QAction(MainWindow)
        self.actionLaTeX_songs.setObjectName(u"actionLaTeX_songs")
        self.actionLaTeX_songs.setEnabled(False)
        self.actionLaTeX_songs.setIcon(icon6)
        self.actionHK = QAction(MainWindow)
        self.actionHK.setObjectName(u"actionHK")
        icon7 = QIcon()
        icon7.addFile(u":/examples/application-hk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHK.setIcon(icon7)
        self.actionConvert = QAction(MainWindow)
        self.actionConvert.setObjectName(u"actionConvert")
        icon8 = QIcon()
        icon8.addFile(u":/actions/media-playback-start.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u"C:/Users/yara/.designer/img/icon-convert.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionConvert.setIcon(icon8)
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        icon9 = QIcon()
        icon9.addFile(u":/actions/icon-quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Quit.setIcon(icon9)
        self.actionActions = QAction(MainWindow)
        self.actionActions.setObjectName(u"actionActions")
        self.actionActions.setCheckable(True)
        self.actionActions.setChecked(True)
        self.actionExaples = QAction(MainWindow)
        self.actionExaples.setObjectName(u"actionExaples")
        self.actionExaples.setCheckable(True)
        self.actionExaples.setChecked(True)
        self.actionWywrota = QAction(MainWindow)
        self.actionWywrota.setObjectName(u"actionWywrota")
        icon10 = QIcon()
        icon10.addFile(u":/examples/application-wywrota.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWywrota.setIcon(icon10)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cbx_input_format = QComboBox(self.centralwidget)
        icon11 = QIcon()
        icon11.addFile(u":/examples/application-ug.png", QSize(), QIcon.Normal, QIcon.On)
        self.cbx_input_format.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/examples/application-chopro.png", QSize(), QIcon.Normal, QIcon.On)
        self.cbx_input_format.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/examples/application-x-tex.png", QSize(), QIcon.Normal, QIcon.On)
        self.cbx_input_format.addItem(icon13, "")
        self.cbx_input_format.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/examples/application-hk.png", QSize(), QIcon.Normal, QIcon.On)
        self.cbx_input_format.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/examples/application-wywrota.png", QSize(), QIcon.Normal, QIcon.On)
        self.cbx_input_format.addItem(icon15, "")
        self.cbx_input_format.setObjectName(u"cbx_input_format")
        font = QFont()
        font.setPointSize(14)
        self.cbx_input_format.setFont(font)
        self.cbx_input_format.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.cbx_input_format, 1, 0, 1, 1)

        self.text_in = QPlainTextEdit(self.centralwidget)
        self.text_in.setObjectName(u"text_in")
        sizePolicy1.setHeightForWidth(self.text_in.sizePolicy().hasHeightForWidth())
        self.text_in.setSizePolicy(sizePolicy1)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(127, 127, 127, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(170, 170, 170, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(255, 251, 221, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush6 = QBrush(QColor(85, 170, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush7 = QBrush(QColor(0, 0, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush7)
        brush8 = QBrush(QColor(255, 0, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Active, QPalette.NoRole, brush)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush11 = QBrush(QColor(240, 240, 240, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        brush12 = QBrush(QColor(227, 227, 227, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        brush13 = QBrush(QColor(160, 160, 160, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        brush14 = QBrush(QColor(105, 105, 105, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        brush15 = QBrush(QColor(245, 245, 245, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.NoRole, brush16)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush17 = QBrush(QColor(0, 120, 215, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.NoRole, brush18)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.text_in.setPalette(palette1)
        font1 = QFont()
        self.text_in.setFont(font1)

        self.gridLayout_3.addWidget(self.text_in, 5, 0, 1, 1)

        self.text_out = QPlainTextEdit(self.centralwidget)
        self.text_out.setObjectName(u"text_out")
        sizePolicy1.setHeightForWidth(self.text_out.sizePolicy().hasHeightForWidth())
        self.text_out.setSizePolicy(sizePolicy1)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Link, brush7)
        palette2.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette2.setBrush(QPalette.Active, QPalette.NoRole, brush)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.NoRole, brush19)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush17)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.NoRole, brush20)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.text_out.setPalette(palette2)
        self.text_out.setReadOnly(True)

        self.gridLayout_3.addWidget(self.text_out, 5, 2, 1, 1)

        self.btn_chords_above = QPushButton(self.centralwidget)
        self.btn_chords_above.setObjectName(u"btn_chords_above")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush21 = QBrush(QColor(65, 66, 66, 0))
        brush21.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush21)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush21)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush21)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush14)
        brush22 = QBrush(QColor(255, 0, 0, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Highlight, brush22)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Link, brush7)
        palette3.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush15)
        brush23 = QBrush(QColor(0, 0, 0, 255))
        brush23.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.NoRole, brush23)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush21)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush21)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Highlight, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        brush24 = QBrush(QColor(0, 0, 0, 255))
        brush24.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.NoRole, brush24)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        brush25 = QBrush(QColor(247, 247, 247, 255))
        brush25.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush25)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Highlight, brush17)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        brush26 = QBrush(QColor(0, 0, 0, 255))
        brush26.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.NoRole, brush26)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.btn_chords_above.setPalette(palette3)
        self.btn_chords_above.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chords_above.setAutoFillBackground(False)
        icon16 = QIcon()
        icon16.addFile(u":/states/switch_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/states/switch_on.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_chords_above.setIcon(icon16)
        self.btn_chords_above.setIconSize(QSize(40, 18))
        self.btn_chords_above.setCheckable(True)
        self.btn_chords_above.setChecked(False)
        self.btn_chords_above.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_chords_above, 2, 2, 1, 1, Qt.AlignLeft)

        self.cbx_output_format = QComboBox(self.centralwidget)
        self.cbx_output_format.addItem(icon11, "")
        self.cbx_output_format.addItem(icon12, "")
        self.cbx_output_format.addItem(icon13, "")
        self.cbx_output_format.addItem(icon13, "")
        self.cbx_output_format.addItem(icon14, "")
        self.cbx_output_format.setObjectName(u"cbx_output_format")
        self.cbx_output_format.setFont(font)
        self.cbx_output_format.setIconSize(QSize(32, 32))
        self.cbx_output_format.setFrame(True)

        self.gridLayout_3.addWidget(self.cbx_output_format, 1, 2, 1, 1)

        self.le_URL = QLineEdit(self.centralwidget)
        self.le_URL.setObjectName(u"le_URL")
        self.le_URL.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.le_URL, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        palette4 = QPalette()
        self.menubar.setPalette(palette4)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExamples = QMenu(self.menuFile)
        self.menuExamples.setObjectName(u"menuExamples")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuConvert = QMenu(self.menubar)
        self.menuConvert.setObjectName(u"menuConvert")
        self.menuToolbars = QMenu(self.menubar)
        self.menuToolbars.setObjectName(u"menuToolbars")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush2)
        brush27 = QBrush(QColor(81, 93, 111, 255))
        brush27.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush27)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Highlight, brush17)
        palette5.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Link, brush7)
        palette5.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush15)
        palette5.setBrush(QPalette.Active, QPalette.NoRole, brush)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Highlight, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        brush28 = QBrush(QColor(0, 0, 0, 255))
        brush28.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Inactive, QPalette.NoRole, brush28)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush25)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Highlight, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        brush29 = QBrush(QColor(0, 0, 0, 255))
        brush29.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Disabled, QPalette.NoRole, brush29)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.statusbar.setPalette(palette5)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_actions = QToolBar(MainWindow)
        self.toolBar_actions.setObjectName(u"toolBar_actions")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBar_actions.sizePolicy().hasHeightForWidth())
        self.toolBar_actions.setSizePolicy(sizePolicy2)
        self.toolBar_actions.setMinimumSize(QSize(0, 0))
        self.toolBar_actions.setMovable(False)
        self.toolBar_actions.setIconSize(QSize(48, 48))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_actions)
        self.toolBar_examples = QToolBar(MainWindow)
        self.toolBar_examples.setObjectName(u"toolBar_examples")
        self.toolBar_examples.setIconSize(QSize(48, 48))
        self.toolBar_examples.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_examples)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())
        self.menubar.addAction(self.menuToolbars.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExamples.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuExamples.addAction(self.actionUltimate_Guitar)
        self.menuExamples.addAction(self.actionChordPro)
        self.menuExamples.addAction(self.actionLaTeX_leadsheets)
        self.menuExamples.addAction(self.actionLaTeX_songs)
        self.menuExamples.addAction(self.actionHK)
        self.menuExamples.addAction(self.actionWywrota)
        self.menuHelp.addAction(self.actionAbout)
        self.menuConvert.addAction(self.actionConvert)
        self.menuToolbars.addAction(self.actionActions)
        self.menuToolbars.addAction(self.actionExaples)
        self.toolBar_actions.addAction(self.actionConvert)
        self.toolBar_examples.addAction(self.actionUltimate_Guitar)
        self.toolBar_examples.addAction(self.actionChordPro)
        self.toolBar_examples.addAction(self.actionLaTeX_leadsheets)
        self.toolBar_examples.addAction(self.actionHK)
        self.toolBar_examples.addAction(self.actionWywrota)

        self.retranslateUi(MainWindow)
        self.action_Quit.triggered.connect(MainWindow.close)
        self.actionExaples.toggled.connect(self.toolBar_examples.setVisible)
        self.actionActions.toggled.connect(self.toolBar_actions.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Songs formats converter v0.1", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionUltimate_Guitar.setText(QCoreApplication.translate("MainWindow", u"Ultimate Guitar", None))
        self.actionChordPro.setText(QCoreApplication.translate("MainWindow", u"ChordPro", None))
        self.actionLaTeX_leadsheets.setText(QCoreApplication.translate("MainWindow", u"LaTeX (leadsheets)", None))
        self.actionLaTeX_songs.setText(QCoreApplication.translate("MainWindow", u"LaTeX (songs)", None))
        self.actionHK.setText(QCoreApplication.translate("MainWindow", u"\"Koliba\"", None))
        self.actionConvert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
#if QT_CONFIG(shortcut)
        self.actionConvert.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.actionActions.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.actionExaples.setText(QCoreApplication.translate("MainWindow", u"Exaples", None))
        self.actionWywrota.setText(QCoreApplication.translate("MainWindow", u"Wywrota", None))
        self.cbx_input_format.setItemText(0, QCoreApplication.translate("MainWindow", u"Ultimate Tabs", None))
        self.cbx_input_format.setItemText(1, QCoreApplication.translate("MainWindow", u"ChordPro", None))
        self.cbx_input_format.setItemText(2, QCoreApplication.translate("MainWindow", u"LaTeX (leadsheets)", None))
        self.cbx_input_format.setItemText(3, QCoreApplication.translate("MainWindow", u"LaTeX (sOngs)", None))
        self.cbx_input_format.setItemText(4, QCoreApplication.translate("MainWindow", u"\"Koliba\"", None))
        self.cbx_input_format.setItemText(5, QCoreApplication.translate("MainWindow", u"Wywrota", None))

        self.btn_chords_above.setText(QCoreApplication.translate("MainWindow", u" Chords above lyrics", None))
        self.cbx_output_format.setItemText(0, QCoreApplication.translate("MainWindow", u"Ultimate Guitars", None))
        self.cbx_output_format.setItemText(1, QCoreApplication.translate("MainWindow", u"ChordPro", None))
        self.cbx_output_format.setItemText(2, QCoreApplication.translate("MainWindow", u"LaTeX (leadsheets)", None))
        self.cbx_output_format.setItemText(3, QCoreApplication.translate("MainWindow", u"LaTeX (sOngs)", None))
        self.cbx_output_format.setItemText(4, QCoreApplication.translate("MainWindow", u"\"Koliba\"", None))

        self.le_URL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://spiewnik.wywrota.pl/", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExamples.setTitle(QCoreApplication.translate("MainWindow", u"Examples", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuConvert.setTitle(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.menuToolbars.setTitle(QCoreApplication.translate("MainWindow", u"Toolbars", None))
        self.toolBar_actions.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_examples.setWindowTitle(QCoreApplication.translate("MainWindow", u"Load Examples", None))
    # retranslateUi

