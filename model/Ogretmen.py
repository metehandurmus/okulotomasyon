class Ogretmen:
    def __init__(self, tcno, ad, soyad, sifre=""):
        self.tcno = tcno
        self.ad = ad
        self.soyad = soyad
        self.sifre = sifre
    
    def __str__(self):
        return '{} {}'.format(self.ad, self.soyad)