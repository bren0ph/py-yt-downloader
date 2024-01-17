# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TelaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Conversor(object):
    def setupUi(self, Conversor):
        if not Conversor.objectName():
            Conversor.setObjectName(u"Conversor")
        Conversor.setEnabled(True)
        Conversor.resize(921, 649)
        Conversor.setMinimumSize(QSize(921, 649))
        Conversor.setMaximumSize(QSize(921, 649))
        self.centralwidget = QWidget(Conversor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Converte = QPushButton(self.centralwidget)
        self.Converte.setObjectName(u"Converte")
        self.Converte.setGeometry(QRect(400, 530, 131, 61))
        self.Converte.setMaximumSize(QSize(530, 130))
        self.Url = QLineEdit(self.centralwidget)
        self.Url.setObjectName(u"Url")
        self.Url.setGeometry(QRect(80, 110, 331, 21))
        self.Url.setMaximumSize(QSize(331, 110))
        self.Nome = QLineEdit(self.centralwidget)
        self.Nome.setObjectName(u"Nome")
        self.Nome.setGeometry(QRect(80, 170, 331, 22))
        self.Nome.setMaximumSize(QSize(331, 110))
        self.Autor = QLineEdit(self.centralwidget)
        self.Autor.setObjectName(u"Autor")
        self.Autor.setGeometry(QRect(80, 230, 331, 22))
        self.Autor.setMaximumSize(QSize(331, 110))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 90, 91, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 140, 161, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 200, 161, 16))
        self.Add = QPushButton(self.centralwidget)
        self.Add.setObjectName(u"Add")
        self.Add.setGeometry(QRect(170, 280, 140, 24))
        self.Add.setMaximumSize(QSize(140, 24))
        self.Lista = QTableWidget(self.centralwidget)
        if (self.Lista.columnCount() < 3):
            self.Lista.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.Lista.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Lista.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Lista.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Lista.setObjectName(u"Lista")
        self.Lista.setGeometry(QRect(460, 30, 440, 430))
        self.Lista.setMaximumSize(QSize(440, 430))
        Conversor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Conversor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 921, 22))
        Conversor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Conversor)
        self.statusbar.setObjectName(u"statusbar")
        Conversor.setStatusBar(self.statusbar)

        self.retranslateUi(Conversor)

        QMetaObject.connectSlotsByName(Conversor)
    # setupUi

    def retranslateUi(self, Conversor):
        Conversor.setWindowTitle(QCoreApplication.translate("Conversor", u"Conversor de video para MP3", None))
#if QT_CONFIG(tooltip)
        self.Converte.setToolTip(QCoreApplication.translate("Conversor", u"<html><head/><body><p>Come\u00e7a o processo de download e convers\u00e3o.</p><p>Pode demorar um pouco, dependendo da quantidade de m\u00fasicas e do n\u00edvel de processamento do seu dispositivo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Converte.setText(QCoreApplication.translate("Conversor", u"Converter", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Conversor", u"O link do v\u00eddeo que vai ser baixado", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Conversor", u"URL do youtube", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Conversor", u"Qual \u00e9 o nome da m\u00fasica", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Conversor", u"Nome da musica:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Conversor", u"Quem fez a m\u00fasica", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Conversor", u"Nome do autor:", None))
        self.Add.setText(QCoreApplication.translate("Conversor", u"Adicionar", None))
        ___qtablewidgetitem = self.Lista.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Conversor", u"URL", None));
        ___qtablewidgetitem1 = self.Lista.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Conversor", u"Autor", None));
        ___qtablewidgetitem2 = self.Lista.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Conversor", u"Nome", None));
    # retranslateUi

