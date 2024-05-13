# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aaa.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(362, 534)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMinimumSize(QSize(340, 80))
        self.textBrowser.setMaximumSize(QSize(16777215, 160))
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.textBrowser, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(338, 80, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_10, 0, 3, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1)

        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_0, 3, 0, 1, 1)

        self.pushButton_16 = QPushButton(Form)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_16, 3, 1, 1, 1)

        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_14, 3, 2, 1, 1)

        self.pushButton_13 = QPushButton(Form)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.pushButton_13, 3, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("Form", u"\u7ed3\u679c", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi

