from model.DB import DB

class LoginManager():
    def __init__(self):
        pass

    def loginControl(self, type, no, pw):
        type = int(type)
        db = DB()
        if type == 1:
            sql = '''
                SELECT * FROM ogrenci WHERE ogrenci_no = (?) AND sifre = (?)
            '''
            data = (no, pw)
            db.cur.execute(sql, data)
            data = db.cur.fetchone()
            if data:
                self.id = data[0]
                return True
            else:
                return False
        elif type == 2:
            sql = '''
                SELECT * FROM ogretmen WHERE tcno = (?) AND sifre = (?)
            '''
            data = (no, pw)
            db.cur.execute(sql, data)
            data = db.cur.fetchone()
            if data:
                self.id = data[0]
                return True
            else:
                return False
        else:
            return False