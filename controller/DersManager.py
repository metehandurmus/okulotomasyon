from model.DB import DB

class DersManager():
    def __init__(self):
        pass
    
    def ogrenciDersGetir(self, ogrenci_id):
        db = DB()
        sql = '''
            SELECT ders.ad, ders.aciklama, ogretmen.ad, ogretmen.soyad, ders.ders_id
            FROM ogrenci
            INNER JOIN ders ON ogrenci.sinif_id = ders.sinif_id
            INNER JOIN ogretmen ON ders.ogretmen_id = ogretmen.ogretmen_id
            WHERE ogrenci.ogrenci_id = (?)
        '''
        data = (ogrenci_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchall()
        return data
