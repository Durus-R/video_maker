# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 651)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 971, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lstImages = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstImages.sizePolicy().hasHeightForWidth())
        self.lstImages.setSizePolicy(sizePolicy)
        self.lstImages.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.lstImages.setDragEnabled(True)
        self.lstImages.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstImages.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lstImages.setObjectName("lstImages")
        self.horizontalLayout.addWidget(self.lstImages)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnLoadImage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLoadImage.setObjectName("btnLoadImage")
        self.verticalLayout.addWidget(self.btnLoadImage)
        self.btnLoadFolder = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLoadFolder.setObjectName("btnLoadFolder")
        self.verticalLayout.addWidget(self.btnLoadFolder)
        self.btnRemoveImage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnRemoveImage.setEnabled(False)
        self.btnRemoveImage.setObjectName("btnRemoveImage")
        self.verticalLayout.addWidget(self.btnRemoveImage)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.dialImageDuration = QtWidgets.QDial(self.horizontalLayoutWidget)
        self.dialImageDuration.setMaximum(24)
        self.dialImageDuration.setProperty("value", 12)
        self.dialImageDuration.setObjectName("dialImageDuration")
        self.verticalLayout_2.addWidget(self.dialImageDuration)
        self.lblImageDuration = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImageDuration.sizePolicy().hasHeightForWidth())
        self.lblImageDuration.setSizePolicy(sizePolicy)
        self.lblImageDuration.setObjectName("lblImageDuration")
        self.verticalLayout_2.addWidget(self.lblImageDuration)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.preview = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setFrameShape(QtWidgets.QFrame.Box)
        self.preview.setObjectName("preview")
        self.verticalLayout_3.addWidget(self.preview)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnPreviousImage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreviousImage.sizePolicy().hasHeightForWidth())
        self.btnPreviousImage.setSizePolicy(sizePolicy)
        self.btnPreviousImage.setObjectName("btnPreviousImage")
        self.horizontalLayout_2.addWidget(self.btnPreviousImage)
        self.btnRender = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRender.sizePolicy().hasHeightForWidth())
        self.btnRender.setSizePolicy(sizePolicy)
        self.btnRender.setObjectName("btnRender")
        self.horizontalLayout_2.addWidget(self.btnRender)
        self.btnNextImage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNextImage.sizePolicy().hasHeightForWidth())
        self.btnNextImage.setSizePolicy(sizePolicy)
        self.btnNextImage.setObjectName("btnNextImage")
        self.horizontalLayout_2.addWidget(self.btnNextImage)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edtOutputPath = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edtOutputPath.setObjectName("edtOutputPath")
        self.horizontalLayout_3.addWidget(self.edtOutputPath)
        self.btnBrowseOutput = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnBrowseOutput.setObjectName("btnBrowseOutput")
        self.horizontalLayout_3.addWidget(self.btnBrowseOutput)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionRendern = QtWidgets.QAction(MainWindow)
        self.actionRendern.setObjectName("actionRendern")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")

        self.retranslateUi(MainWindow)
        self.actionBeenden.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Creator"))
        self.lstImages.setSortingEnabled(False)
        self.btnLoadImage.setText(_translate("MainWindow", "🖼️ Bild laden"))
        self.btnLoadFolder.setText(_translate("MainWindow", "📁 Ordner laden"))
        self.btnRemoveImage.setText(_translate("MainWindow", "🚫 Entfernen"))
        self.lblImageDuration.setText(_translate("MainWindow", "Dauer pro Folie: 12s"))
        self.preview.setText(_translate("MainWindow", "Kein Bild geladen."))
        self.btnPreviousImage.setText(_translate("MainWindow", "<"))
        self.btnRender.setText(_translate("MainWindow", "🔴 Rendern"))
        self.btnNextImage.setText(_translate("MainWindow", ">"))
        self.btnBrowseOutput.setText(_translate("MainWindow", "📁 Durchsuchen"))
        self.actionRendern.setText(_translate("MainWindow", "Rendern"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))