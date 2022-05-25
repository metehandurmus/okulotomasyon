from model.DB import DB

class SonucManager():
    def __init__(self):
        pass

    def tumSonuclar(self, ogr_id):
        db = DB()
        sql = '''
            SELECT *
            FROM ogrenci
            INNER JOIN sonuc ON ogrenci.ogrenci_id = sonuc.ogrenci_id
            INNER JOIN sinav ON sonuc.sinav_id = sinav.sinav_id
            WHERE ogrenci.ogrenci_id = (?) ORDER BY sinav.ad ASC
            '''
        data = (ogr_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchall()
        return data

    def dersSonuclar(self, ogr_id, ders_id):
        db = DB()
        sql = '''
            SELECT *
            FROM sonuc
            INNER JOIN sinav ON sonuc.sinav_id = sinav.sinav_id
            INNER JOIN ders ON sonuc.ders_id = ders.ders_id
            WHERE sonuc.ogrenci_id = (?) AND sonuc.ders_id = (?)
            ORDER BY sinav.ad ASC
            '''
        data = (ogr_id, ders_id)
        db.cur.execute(sql, data)
        data = db.cur.fetchall()
        return data

    def secilenleriGetir(self, ogr_id):
        secilenliste = []
        db = DB()
        sql = '''
            SELECT sinif_id FROM ogrenci WHERE ogrenci_id = (?)
        '''
        data = (ogr_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchone()
        sql = '''
            SELECT ders1_id, ders2_id, ders3_id FROM anasayfaya_secilen_dersler WHERE sinif_id = (?)
        '''
        data = (data[0], )
        db.cur.execute(sql, data)
        data = db.cur.fetchone()
        secilenliste.append(self.dersSonuclar(ogr_id, data[0]))
        secilenliste.append(self.dersSonuclar(ogr_id, data[1]))
        secilenliste.append(self.dersSonuclar(ogr_id, data[2]))
        return secilenliste
    
    def sonucGetir(self, ogr_id):
        db = DB()
        sql = '''
            SELECT ders.ad, sinav.ad, sinav.tarih, sonuc.puan FROM sonuc
            INNER JOIN sinav ON sonuc.sinav_id = sinav.sinav_id
            INNER JOIN ders ON sonuc.ders_id = ders.ders_id
            WHERE sonuc.ogrenci_id = (?)
            ORDER BY sinav.tarih DESC
        '''
        data = (ogr_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchall()
        return data