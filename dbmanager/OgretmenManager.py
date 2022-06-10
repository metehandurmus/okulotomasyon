from model.Ogretmen import Ogretmen
from model.DB import DB

class OgretmenManager:
    def __init__(self):
        pass

    def getOgretmen(self, ogr_id):
        db = DB()
        sql = '''
            SELECT * FROM ogretmen WHERE ogretmen_id = (?)
        '''
        data = (ogr_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchone()
        if data:
            ogretmen = Ogretmen(data[1], data[3], data[4], sifre=data[2])
            return ogretmen
        else:
            return False
        
    def getOgretmenDersler(self, ogr_id):
        db = DB()
        sql = '''
            SELECT ders.ad, sinif.value, ders.ders_id FROM ders
            INNER JOIN sinif ON ders.sinif_id = sinif.sinif_id
            WHERE ders.ogretmen_id = (?)
        '''
        data = (ogr_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchall()
        if data:
            return data
        else:
            return False

    def updateOgretmen(self, ogretmen):
        db = DB()
        sql = '''
        UPDATE ogretmen SET tcno = ?, sifre = ?, ad = ?, soyad = ?
        '''
        data = (ogretmen.tcno, ogretmen.sifre, ogretmen.ad, ogretmen.soyad)
        db.cur.execute(sql, data)
        db.conn.commit()
        db.close()