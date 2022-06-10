from model.DB import DB

class YoklamaManager():
    def __init__(self):
        pass
    
    def yoklamaGetir(self, ogrenci_id):
        db = DB()
        sql = '''
            SELECT tarih FROM yoklama WHERE ogrenci_id = (?) AND varMi = 0
        '''
        data = (ogrenci_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchall()
        return data
