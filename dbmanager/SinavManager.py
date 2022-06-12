from model.DB import DB
from model.Sinav import Sinav

class SinavManager:
    def __init__(self):
        pass
    
    def aciklananSinavlar(self, ogr_id):
        db = DB()
        sql = '''
            SELECT sinav.ad, sinav.tarih, ders.ad, sinif.value
            FROM sinav
            INNER JOIN ders ON ders.ders_id = sinav.ders_id
            INNER JOIN sinif ON ders.sinif_id = sinif.sinif_id
            INNER JOIN ogrenci ON ogrenci.sinif_id = sinif.sinif_id
            WHERE ogrenci.ogrenci_id = (?) ORDER BY sinav.tarih DESC
        '''
        data = (ogr_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchall()
        return data
    
    def sinavEkle(self, sinav):
        try:
            db = DB()
            sql = '''
                INSERT INTO sinav (ad, tarih, ders_id) VALUES (?, ?, ?)
            '''
            data = (sinav.ad, sinav.tarih, sinav.ders_id)
            db.cur.execute(sql, data)
            db.conn.commit()
            return True
        except:
            return False

    def sinavOlustur(self, ad, tarih, ders_id):
        sinav = Sinav(ad, tarih, ders_id)
        return sinav