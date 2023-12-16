from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ürün():

    def __init__(self,isim,alış_fiyat,satış_fiyat,tarih):
        self.isim = isim
        self.alış_fiyat = alış_fiyat
        self.satış_fiyat = satış_fiyat
        self.tarih = tarih

    def __str__(self):
        return """Ürün: {}\nAlış Fiyatı: {}\nSatış Fiyatı: {}\nAlış Tarihi: {}""".format(self.isim,self.alış_fiyat,self.satış_fiyat,self.tarih)

class Dükkan():

    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):

        self.bağlantı = sqlite3.connect("Dükkan_bilgiler.db")

        self.cursor = self.bağlantı.cursor()

        sorgu = "Create Table IF NOT EXISTS ürünler (isim TEXT,alış_fiyat tEXT,satış_fiyat TEXT,tarih TEXT)"

        self.cursor.execute(sorgu)

        self.bağlantı.commit()

    def bağlantı_kes(self):
        self.bağlantı.close()

    def ürünleri_göster(self):
        sorgu = "SELECT * FROM ürünler"

        with self.bağlantı:
            self.cursor.execute(sorgu)
            ürünler = self.cursor.fetchall()

            if not ürünler:
                print("Herhangi bir ürün bulunmuyor.")
            else:
                ürünlerin_hepsi = [Ürün(i[0], i[1], i[2], i[3]) for i in ürünler]
                return ürünlerin_hepsi

    def ürün_sorgula(self,isim):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if ( len(ürünler)== 0 ):
            pass
        else:
            ürün = Ürün(ürünler[0][0],ürünler[0][1],ürünler[0][2],ürünler[0][3])
            return ürün

    def ürün_ekle(self, ürün):
        mevcut_ürün = self.ürün_sorgula(ürün.isim)

        if mevcut_ürün:
            sorgu = "Update ürünler Set alış_fiyat=?, satış_fiyat=?, tarih=? Where isim=?"
            self.cursor.execute(sorgu, (ürün.alış_fiyat, ürün.satış_fiyat, ürün.tarih, ürün.isim))
        else:
            sorgu = "Insert into ürünler Values(?,?,?,?)"
            self.cursor.execute(sorgu, (ürün.isim, ürün.alış_fiyat, ürün.satış_fiyat, ürün.tarih))

        self.bağlantı.commit()

    def alış_fiyat_değiştir(self,isim,fiyat):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            alış_fiyat = ürünler[0][2]

            alış_fiyat = fiyat

            sorgu2 = "Update ürünler set alış_fiyat = ? where isim = ?"

            self.cursor.execute(sorgu2, (alış_fiyat, isim))

            print("alış fiyatı", alış_fiyat, "olarak güncellendi.")

            self.bağlantı.commit()

    def satış_fiyat_değiştir(self,isim,fiyat):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            satış_fiyat = ürünler[0][3]

            satış_fiyat = fiyat

            sorgu2 = "Update ürünler set satış_fiyat = ? where isim = ?"

            self.cursor.execute(sorgu2, (satış_fiyat, isim))

            print("satış fiyatı", satış_fiyat, "olarak güncellendi.")

            self.bağlantı.commit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(100, -1, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ara_butonu = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ara_butonu.setFont(font)
        self.ara_butonu.setObjectName("ara_butonu")
        self.gridLayout_3.addWidget(self.ara_butonu, 1, 1, 1, 1)
        self.urun_alis_goster = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_alis_goster.setFont(font)
        self.urun_alis_goster.setPlainText("")
        self.urun_alis_goster.setObjectName("urun_alis_goster")
        self.gridLayout_3.addWidget(self.urun_alis_goster, 2, 1, 1, 1)
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_10.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.textBrowser_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_10.setAutoFillBackground(False)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.gridLayout_3.addWidget(self.textBrowser_10, 0, 0, 1, 1)
        self.urun_adi_ara = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_adi_ara.setFont(font)
        self.urun_adi_ara.setPlainText("")
        self.urun_adi_ara.setObjectName("urun_adi_ara")
        self.gridLayout_3.addWidget(self.urun_adi_ara, 0, 1, 1, 1)
        self.temizle_sag = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temizle_sag.setFont(font)
        self.temizle_sag.setObjectName("temizle_sag")
        self.gridLayout_3.addWidget(self.temizle_sag, 1, 0, 1, 1)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.textBrowser_9.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.gridLayout_3.addWidget(self.textBrowser_9, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.urun_satis_fiyat = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_satis_fiyat.setFont(font)
        self.urun_satis_fiyat.setObjectName("urun_satis_fiyat")
        self.gridLayout.addWidget(self.urun_satis_fiyat, 2, 1, 1, 1)
        self.urun_adi_kayit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_adi_kayit.setFont(font)
        self.urun_adi_kayit.setObjectName("urun_adi_kayit")
        self.gridLayout.addWidget(self.urun_adi_kayit, 0, 1, 1, 1)
        self.urun_alis_fiyat = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_alis_fiyat.setFont(font)
        self.urun_alis_fiyat.setPlainText("")
        self.urun_alis_fiyat.setObjectName("urun_alis_fiyat")
        self.gridLayout.addWidget(self.urun_alis_fiyat, 1, 1, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.urun_alis_tarihi = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_alis_tarihi.setFont(font)
        self.urun_alis_tarihi.setObjectName("urun_alis_tarihi")
        self.gridLayout.addWidget(self.urun_alis_tarihi, 3, 1, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 2, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 3, 0, 1, 1)
        self.kaydet_buton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kaydet_buton.setFont(font)
        self.kaydet_buton.setObjectName("kaydet_buton")
        self.gridLayout.addWidget(self.kaydet_buton, 5, 1, 1, 1)
        self.temizle_sol = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temizle_sol.setFont(font)
        self.temizle_sol.setObjectName("temizle_sol")
        self.gridLayout.addWidget(self.temizle_sol, 5, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAra = QtWidgets.QAction(MainWindow)
        self.actionAra.setObjectName("actionAra")

        self.kaydet_buton.clicked.connect(self.kayit)
        self.ara_butonu.clicked.connect(self.arama)
        self.temizle_sol.clicked.connect(self.temizle_kaydet)
        self.temizle_sag.clicked.connect(self.temizle_ara)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ara_butonu.setText(_translate("MainWindow", "Ara"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">Aranan Ürünün Adı</span></p></body></html>"))
        self.temizle_sag.setText(_translate("MainWindow", "temizle"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ürünün Bilgileri:</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">Ürünün Alış Fiyatı</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">Kaydedilecek Ürünün Adı</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">Ürünün Satış Fiyatı</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">Ürünün Alış Tarihi</span></p></body></html>"))
        self.kaydet_buton.setText(_translate("MainWindow", "Ürünü Kaydet"))
        self.temizle_sol.setText(_translate("MainWindow", "Temizle"))
        self.actionAra.setText(_translate("MainWindow", "Ara"))

    def kayit(self):
        isim = self.urun_adi_kayit.toPlainText().lower()
        alis_fiyat = self.urun_alis_fiyat.toPlainText()
        satis_fiyat = self.urun_satis_fiyat.toPlainText()
        tarih = self.urun_alis_tarihi.toPlainText().upper()

        try:
            yeni_urun = Ürün(isim,alis_fiyat,satis_fiyat,tarih)
            dükkan.ürün_ekle(yeni_urun)
            self.urun_alis_goster.setPlainText("Ürün Başarıyla kaydedildi.")
        except:
            print("Bir Hata Oluştu.")


    def arama(self):
        isim = self.urun_adi_ara.toPlainText().lower().strip()
        if (isim == ""):
            sonuc = []
            ürünler = dükkan.ürünleri_göster()
            for i in ürünler:
                sonuc.append(str(i))
            self.urun_alis_goster.setPlainText("\n".join(sonuc) + "\n")
        else:
            sonuç = str(dükkan.ürün_sorgula(isim))
            self.urun_alis_goster.setPlainText(sonuç)
    def temizle_kaydet(self):
        self.urun_adi_kayit.clear()
        self.urun_alis_fiyat.clear()
        self.urun_alis_tarihi.clear()
        self.urun_satis_fiyat.clear()
    def temizle_ara(self):
        self.urun_adi_ara.clear()
        self.urun_alis_goster.clear()



if __name__ == "__main__":
    import sys
    dükkan = Dükkan()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())