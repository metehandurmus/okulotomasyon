from model.DB import DB

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