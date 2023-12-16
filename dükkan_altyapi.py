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


