# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/net/homes/hierola/scripts/python/OfflineMaker_TEST_DONTUSE/ffmpegOfflineGui_v07.ui'
#
# Created: Fri Feb 23 09:52:16 2018
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 881)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabOptions = QtGui.QTabWidget(self.centralwidget)
        self.tabOptions.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabOptions.setIconSize(QtCore.QSize(16, 16))
        self.tabOptions.setObjectName("tabOptions")
        self.OfflineMakerTab = QtGui.QWidget()
        self.OfflineMakerTab.setObjectName("OfflineMakerTab")
        self.gridLayout_3 = QtGui.QGridLayout(self.OfflineMakerTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.OfflineMakerTab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.frameSpeed = QtGui.QLabel(self.OfflineMakerTab)
        self.frameSpeed.setObjectName("frameSpeed")
        self.gridLayout_2.addWidget(self.frameSpeed, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.OfflineMakerTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.v1_t1 = QtGui.QLineEdit(self.OfflineMakerTab)
        self.v1_t1.setObjectName("v1_t1")
        self.gridLayout_2.addWidget(self.v1_t1, 2, 1, 1, 1)
        self.fps1_t1 = QtGui.QComboBox(self.OfflineMakerTab)
        self.fps1_t1.setObjectName("fps1_t1")
        self.fps1_t1.addItem("")
        self.fps1_t1.addItem("")
        self.fps1_t1.addItem("")
        self.fps1_t1.addItem("")
        self.fps1_t1.addItem("")
        self.fps1_t1.addItem("")
        self.fps1_t1.addItem("")
        self.gridLayout_2.addWidget(self.fps1_t1, 3, 1, 1, 1)
        self.o1_t1 = QtGui.QLineEdit(self.OfflineMakerTab)
        self.o1_t1.setObjectName("o1_t1")
        self.gridLayout_2.addWidget(self.o1_t1, 4, 1, 1, 1)
        self.v1_t1_btn = QtGui.QPushButton(self.OfflineMakerTab)
        self.v1_t1_btn.setObjectName("v1_t1_btn")
        self.gridLayout_2.addWidget(self.v1_t1_btn, 2, 2, 1, 1)
        self.o1_t1_btn = QtGui.QPushButton(self.OfflineMakerTab)
        self.o1_t1_btn.setObjectName("o1_t1_btn")
        self.gridLayout_2.addWidget(self.o1_t1_btn, 4, 2, 1, 1)
        self.mkdir_t1 = QtGui.QCheckBox(self.OfflineMakerTab)
        self.mkdir_t1.setChecked(True)
        self.mkdir_t1.setObjectName("mkdir_t1")
        self.gridLayout_2.addWidget(self.mkdir_t1, 0, 1, 1, 1)
        self.transcode1_t1 = QtGui.QPushButton(self.OfflineMakerTab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/net/homes/hierola/scripts/python/OfflineMaker/icons/icons8-jpg-filled-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.transcode1_t1.setIcon(icon)
        self.transcode1_t1.setIconSize(QtCore.QSize(48, 48))
        self.transcode1_t1.setObjectName("transcode1_t1")
        self.gridLayout_2.addWidget(self.transcode1_t1, 5, 1, 1, 1)
        self.cb1_t1 = QtGui.QCheckBox(self.OfflineMakerTab)
        self.cb1_t1.setObjectName("cb1_t1")
        self.gridLayout_2.addWidget(self.cb1_t1, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabOptions.addTab(self.OfflineMakerTab, icon, "")
        self.mergeAudioTab = QtGui.QWidget()
        self.mergeAudioTab.setObjectName("mergeAudioTab")
        self.gridLayout_5 = QtGui.QGridLayout(self.mergeAudioTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.a1_t2 = QtGui.QLineEdit(self.mergeAudioTab)
        self.a1_t2.setObjectName("a1_t2")
        self.gridLayout_4.addWidget(self.a1_t2, 1, 4, 1, 1)
        self.v1_t2 = QtGui.QLineEdit(self.mergeAudioTab)
        self.v1_t2.setObjectName("v1_t2")
        self.gridLayout_4.addWidget(self.v1_t2, 0, 4, 1, 1)
        self.audioInput = QtGui.QLabel(self.mergeAudioTab)
        self.audioInput.setObjectName("audioInput")
        self.gridLayout_4.addWidget(self.audioInput, 1, 2, 1, 1)
        self.videoInput = QtGui.QLabel(self.mergeAudioTab)
        self.videoInput.setObjectName("videoInput")
        self.gridLayout_4.addWidget(self.videoInput, 0, 2, 1, 1)
        self.fps1_t2 = QtGui.QComboBox(self.mergeAudioTab)
        self.fps1_t2.setEditable(False)
        self.fps1_t2.setFrame(True)
        self.fps1_t2.setObjectName("fps1_t2")
        self.fps1_t2.addItem("")
        self.fps1_t2.addItem("")
        self.fps1_t2.addItem("")
        self.fps1_t2.addItem("")
        self.fps1_t2.addItem("")
        self.fps1_t2.addItem("")
        self.fps1_t2.addItem("")
        self.gridLayout_4.addWidget(self.fps1_t2, 2, 4, 1, 1)
        self.frameSpeed_2 = QtGui.QLabel(self.mergeAudioTab)
        self.frameSpeed_2.setObjectName("frameSpeed_2")
        self.gridLayout_4.addWidget(self.frameSpeed_2, 2, 2, 1, 1)
        self.v1_t2_btn = QtGui.QPushButton(self.mergeAudioTab)
        self.v1_t2_btn.setObjectName("v1_t2_btn")
        self.gridLayout_4.addWidget(self.v1_t2_btn, 0, 5, 1, 1)
        self.a1_t2_btn = QtGui.QPushButton(self.mergeAudioTab)
        self.a1_t2_btn.setObjectName("a1_t2_btn")
        self.gridLayout_4.addWidget(self.a1_t2_btn, 1, 5, 1, 1)
        self.transcode1_t2 = QtGui.QPushButton(self.mergeAudioTab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/net/homes/hierola/scripts/python/OfflineMaker/icons/icons8-merge-filled-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.transcode1_t2.setIcon(icon1)
        self.transcode1_t2.setIconSize(QtCore.QSize(48, 48))
        self.transcode1_t2.setObjectName("transcode1_t2")
        self.gridLayout_4.addWidget(self.transcode1_t2, 4, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.mergeAudioTab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 2, 1, 1)
        self.o1_t2 = QtGui.QLineEdit(self.mergeAudioTab)
        self.o1_t2.setObjectName("o1_t2")
        self.gridLayout_4.addWidget(self.o1_t2, 3, 4, 1, 1)
        self.o1_t2_btn = QtGui.QPushButton(self.mergeAudioTab)
        self.o1_t2_btn.setObjectName("o1_t2_btn")
        self.gridLayout_4.addWidget(self.o1_t2_btn, 3, 5, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabOptions.addTab(self.mergeAudioTab, icon1, "")
        self.ExtractAudio = QtGui.QWidget()
        self.ExtractAudio.setObjectName("ExtractAudio")
        self.gridLayout_9 = QtGui.QGridLayout(self.ExtractAudio)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.v1_t4 = QtGui.QLineEdit(self.ExtractAudio)
        self.v1_t4.setObjectName("v1_t4")
        self.gridLayout_8.addWidget(self.v1_t4, 0, 4, 1, 1)
        self.videoInput_3 = QtGui.QLabel(self.ExtractAudio)
        self.videoInput_3.setObjectName("videoInput_3")
        self.gridLayout_8.addWidget(self.videoInput_3, 0, 2, 1, 1)
        self.v1_t4_btn = QtGui.QPushButton(self.ExtractAudio)
        self.v1_t4_btn.setObjectName("v1_t4_btn")
        self.gridLayout_8.addWidget(self.v1_t4_btn, 0, 5, 1, 1)
        self.extract_t4 = QtGui.QPushButton(self.ExtractAudio)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/net/homes/hierola/scripts/python/OfflineMaker/icons/icons8-audio-wave-filled-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extract_t4.setIcon(icon2)
        self.extract_t4.setIconSize(QtCore.QSize(48, 48))
        self.extract_t4.setObjectName("extract_t4")
        self.gridLayout_8.addWidget(self.extract_t4, 2, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.ExtractAudio)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 1, 2, 1, 1)
        self.o1_t4 = QtGui.QLineEdit(self.ExtractAudio)
        self.o1_t4.setObjectName("o1_t4")
        self.gridLayout_8.addWidget(self.o1_t4, 1, 4, 1, 1)
        self.o1_t4_btn = QtGui.QPushButton(self.ExtractAudio)
        self.o1_t4_btn.setObjectName("o1_t4_btn")
        self.gridLayout_8.addWidget(self.o1_t4_btn, 1, 5, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabOptions.addTab(self.ExtractAudio, icon2, "")
        self.RemoveAudio = QtGui.QWidget()
        self.RemoveAudio.setObjectName("RemoveAudio")
        self.gridLayout_7 = QtGui.QGridLayout(self.RemoveAudio)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.v1_t3 = QtGui.QLineEdit(self.RemoveAudio)
        self.v1_t3.setObjectName("v1_t3")
        self.gridLayout_6.addWidget(self.v1_t3, 0, 4, 1, 1)
        self.videoInput_2 = QtGui.QLabel(self.RemoveAudio)
        self.videoInput_2.setObjectName("videoInput_2")
        self.gridLayout_6.addWidget(self.videoInput_2, 0, 2, 1, 1)
        self.v1_t3_btn = QtGui.QPushButton(self.RemoveAudio)
        self.v1_t3_btn.setObjectName("v1_t3_btn")
        self.gridLayout_6.addWidget(self.v1_t3_btn, 0, 5, 1, 1)
        self.remove1_t3 = QtGui.QPushButton(self.RemoveAudio)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/net/homes/hierola/scripts/python/OfflineMaker/icons/icons8-no-audio-filled-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove1_t3.setIcon(icon3)
        self.remove1_t3.setIconSize(QtCore.QSize(48, 48))
        self.remove1_t3.setObjectName("remove1_t3")
        self.gridLayout_6.addWidget(self.remove1_t3, 2, 4, 1, 1)
        self.Output = QtGui.QLabel(self.RemoveAudio)
        self.Output.setObjectName("Output")
        self.gridLayout_6.addWidget(self.Output, 1, 2, 1, 1)
        self.o1_t3 = QtGui.QLineEdit(self.RemoveAudio)
        self.o1_t3.setObjectName("o1_t3")
        self.gridLayout_6.addWidget(self.o1_t3, 1, 4, 1, 1)
        self.o1_t3_btn = QtGui.QPushButton(self.RemoveAudio)
        self.o1_t3_btn.setObjectName("o1_t3_btn")
        self.gridLayout_6.addWidget(self.o1_t3_btn, 1, 5, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabOptions.addTab(self.RemoveAudio, icon3, "")
        self.widget = QtGui.QWidget()
        self.widget.setEnabled(True)
        self.widget.setObjectName("widget")
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 981, 781))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_11 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 3, 0, 1, 1)
        self.frameSpeed_3 = QtGui.QLabel(self.layoutWidget)
        self.frameSpeed_3.setObjectName("frameSpeed_3")
        self.gridLayout_11.addWidget(self.frameSpeed_3, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_11.addWidget(self.label_6, 5, 0, 1, 1)
        self.a1_t5 = QtGui.QLineEdit(self.layoutWidget)
        self.a1_t5.setObjectName("a1_t5")
        self.gridLayout_11.addWidget(self.a1_t5, 3, 3, 1, 1)
        self.o1_t5 = QtGui.QLineEdit(self.layoutWidget)
        self.o1_t5.setObjectName("o1_t5")
        self.gridLayout_11.addWidget(self.o1_t5, 5, 3, 1, 1)
        self.a1_t5_btn = QtGui.QPushButton(self.layoutWidget)
        self.a1_t5_btn.setObjectName("a1_t5_btn")
        self.gridLayout_11.addWidget(self.a1_t5_btn, 3, 4, 1, 1)
        self.o1_t5_btn = QtGui.QPushButton(self.layoutWidget)
        self.o1_t5_btn.setObjectName("o1_t5_btn")
        self.gridLayout_11.addWidget(self.o1_t5_btn, 5, 4, 1, 1)
        self.transcode1_t5_btn = QtGui.QPushButton(self.layoutWidget)
        self.transcode1_t5_btn.setIcon(icon)
        self.transcode1_t5_btn.setIconSize(QtCore.QSize(48, 48))
        self.transcode1_t5_btn.setObjectName("transcode1_t5_btn")
        self.gridLayout_11.addWidget(self.transcode1_t5_btn, 6, 3, 1, 1)
        self.v1_t5 = QtGui.QLineEdit(self.layoutWidget)
        self.v1_t5.setObjectName("v1_t5")
        self.gridLayout_11.addWidget(self.v1_t5, 0, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 1)
        self.v1_t5_btn = QtGui.QPushButton(self.layoutWidget)
        self.v1_t5_btn.setObjectName("v1_t5_btn")
        self.gridLayout_11.addWidget(self.v1_t5_btn, 0, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_11.addWidget(self.label_8, 1, 0, 1, 1)
        self.pad1_t5 = QtGui.QComboBox(self.layoutWidget)
        self.pad1_t5.setObjectName("pad1_t5")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.pad1_t5.addItem("")
        self.gridLayout_11.addWidget(self.pad1_t5, 1, 3, 1, 1)
        self.sf1_t5 = QtGui.QLineEdit(self.layoutWidget)
        self.sf1_t5.setObjectName("sf1_t5")
        self.gridLayout_11.addWidget(self.sf1_t5, 2, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_11.addWidget(self.label_9, 2, 0, 1, 1)
        self.mo1_t5 = QtGui.QLabel(self.layoutWidget)
        self.mo1_t5.setObjectName("mo1_t5")
        self.gridLayout_11.addWidget(self.mo1_t5, 7, 3, 1, 1)
        self.fps1_t5 = QtGui.QComboBox(self.layoutWidget)
        self.fps1_t5.setObjectName("fps1_t5")
        self.fps1_t5.addItem("")
        self.fps1_t5.addItem("")
        self.fps1_t5.addItem("")
        self.fps1_t5.addItem("")
        self.fps1_t5.addItem("")
        self.fps1_t5.addItem("")
        self.fps1_t5.addItem("")
        self.gridLayout_11.addWidget(self.fps1_t5, 4, 3, 1, 1)
        self.tabOptions.addTab(self.widget, "")
        self.gridLayout.addWidget(self.tabOptions, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 23))
        self.menubar.setObjectName("menubar")
        self.menuUseless = QtGui.QMenu(self.menubar)
        self.menuUseless.setObjectName("menuUseless")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuUseless.menuAction())

        self.retranslateUi(MainWindow)
        self.tabOptions.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Offline Transcoder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Offline", None, QtGui.QApplication.UnicodeUTF8))
        self.frameSpeed.setText(QtGui.QApplication.translate("MainWindow", "Fps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t1.setItemText(0, QtGui.QApplication.translate("MainWindow", "23.976", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t1.setItemText(1, QtGui.QApplication.translate("MainWindow", "24", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t1.setItemText(2, QtGui.QApplication.translate("MainWindow", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t1.setItemText(3, QtGui.QApplication.translate("MainWindow", "29.97", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t1.setItemText(4, QtGui.QApplication.translate("MainWindow", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t1.setItemText(5, QtGui.QApplication.translate("MainWindow", "59.94", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t1.setItemText(6, QtGui.QApplication.translate("MainWindow", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.v1_t1_btn.setText(QtGui.QApplication.translate("MainWindow", "Open  File", None, QtGui.QApplication.UnicodeUTF8))
        self.o1_t1_btn.setText(QtGui.QApplication.translate("MainWindow", "Open Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.mkdir_t1.setText(QtGui.QApplication.translate("MainWindow", "Auto make folder", None, QtGui.QApplication.UnicodeUTF8))
        self.transcode1_t1.setText(QtGui.QApplication.translate("MainWindow", "Transcode", None, QtGui.QApplication.UnicodeUTF8))
        self.cb1_t1.setText(QtGui.QApplication.translate("MainWindow", "Have audio?", None, QtGui.QApplication.UnicodeUTF8))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.OfflineMakerTab), QtGui.QApplication.translate("MainWindow", "To Jpg Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.audioInput.setText(QtGui.QApplication.translate("MainWindow", "Audio Input", None, QtGui.QApplication.UnicodeUTF8))
        self.videoInput.setText(QtGui.QApplication.translate("MainWindow", "Video Input", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t2.setItemText(0, QtGui.QApplication.translate("MainWindow", "23.976", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t2.setItemText(1, QtGui.QApplication.translate("MainWindow", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t2.setItemText(2, QtGui.QApplication.translate("MainWindow", "24", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t2.setItemText(3, QtGui.QApplication.translate("MainWindow", "29.97", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t2.setItemText(4, QtGui.QApplication.translate("MainWindow", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t2.setItemText(5, QtGui.QApplication.translate("MainWindow", "59.94", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t2.setItemText(6, QtGui.QApplication.translate("MainWindow", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.frameSpeed_2.setText(QtGui.QApplication.translate("MainWindow", "Fps", None, QtGui.QApplication.UnicodeUTF8))
        self.v1_t2_btn.setText(QtGui.QApplication.translate("MainWindow", "Open Video", None, QtGui.QApplication.UnicodeUTF8))
        self.a1_t2_btn.setText(QtGui.QApplication.translate("MainWindow", "Choose Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.transcode1_t2.setText(QtGui.QApplication.translate("MainWindow", "Transcode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.o1_t2_btn.setText(QtGui.QApplication.translate("MainWindow", "Save Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.mergeAudioTab), QtGui.QApplication.translate("MainWindow", "Inject  Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.videoInput_3.setText(QtGui.QApplication.translate("MainWindow", "Video Input", None, QtGui.QApplication.UnicodeUTF8))
        self.v1_t4_btn.setText(QtGui.QApplication.translate("MainWindow", "Open Video", None, QtGui.QApplication.UnicodeUTF8))
        self.extract_t4.setText(QtGui.QApplication.translate("MainWindow", "Extract  Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Output Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.o1_t4_btn.setText(QtGui.QApplication.translate("MainWindow", "Save Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.ExtractAudio), QtGui.QApplication.translate("MainWindow", "Extract Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.videoInput_2.setText(QtGui.QApplication.translate("MainWindow", "Video Input", None, QtGui.QApplication.UnicodeUTF8))
        self.v1_t3_btn.setText(QtGui.QApplication.translate("MainWindow", "Open Video", None, QtGui.QApplication.UnicodeUTF8))
        self.remove1_t3.setText(QtGui.QApplication.translate("MainWindow", "Remove Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.Output.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.o1_t3_btn.setText(QtGui.QApplication.translate("MainWindow", "Save Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.RemoveAudio), QtGui.QApplication.translate("MainWindow", "Remove Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.frameSpeed_3.setText(QtGui.QApplication.translate("MainWindow", "Image Sequence Fps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.a1_t5_btn.setText(QtGui.QApplication.translate("MainWindow", "Open  File", None, QtGui.QApplication.UnicodeUTF8))
        self.o1_t5_btn.setText(QtGui.QApplication.translate("MainWindow", "Open Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.transcode1_t5_btn.setText(QtGui.QApplication.translate("MainWindow", "Transcode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Image Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.v1_t5_btn.setText(QtGui.QApplication.translate("MainWindow", "Open Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Number Format", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(0, QtGui.QApplication.translate("MainWindow", "%01d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(1, QtGui.QApplication.translate("MainWindow", "%02d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(2, QtGui.QApplication.translate("MainWindow", "%03d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(3, QtGui.QApplication.translate("MainWindow", "%04d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(4, QtGui.QApplication.translate("MainWindow", "%05d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(5, QtGui.QApplication.translate("MainWindow", "%06d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(6, QtGui.QApplication.translate("MainWindow", "%07d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(7, QtGui.QApplication.translate("MainWindow", "%08d", None, QtGui.QApplication.UnicodeUTF8))
        self.pad1_t5.setItemText(8, QtGui.QApplication.translate("MainWindow", "%09d", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Start Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.mo1_t5.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t5.setItemText(0, QtGui.QApplication.translate("MainWindow", "23.976", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t5.setItemText(1, QtGui.QApplication.translate("MainWindow", "24", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t5.setItemText(2, QtGui.QApplication.translate("MainWindow", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t5.setItemText(3, QtGui.QApplication.translate("MainWindow", "29.97", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t5.setItemText(4, QtGui.QApplication.translate("MainWindow", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t5.setItemText(5, QtGui.QApplication.translate("MainWindow", "59.94", None, QtGui.QApplication.UnicodeUTF8))
        self.fps1_t5.setItemText(6, QtGui.QApplication.translate("MainWindow", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.widget), QtGui.QApplication.translate("MainWindow", "Prores", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUseless.setTitle(QtGui.QApplication.translate("MainWindow", "Useless", None, QtGui.QApplication.UnicodeUTF8))

