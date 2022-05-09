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