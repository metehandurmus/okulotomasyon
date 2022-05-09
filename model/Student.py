class Student:
    def __init__(self, ogrenci_no, ad, soyad, cinsiyet, sinif, sube, sifre=0, ogrenci_id=0):
        self.ogrenci_id = ogrenci_id
        self.ogrenci_no = ogrenci_no
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad 
        self.cinsiyet = cinsiyet
        self.sinif = sinif
        self.sube = sube

    def __str__(self):
        return '{} {}'.format(self.ad, self.soyad)