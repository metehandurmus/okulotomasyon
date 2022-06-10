from model.Student import Student
from model.DB import DB

class StudentManager:
    def __init__(self):
        pass

    def getStudent(self, student_id):
        db = DB()
        sql = '''
        SELECT ogrenci.ogrenci_no, ogrenci.ad, ogrenci.soyad, ogrenci.cinsiyet, sinif.value, sube.value, ogrenci.ogrenci_id, ogrenci.sifre, ogrenci.sinif_id, ogrenci.sube_id
        FROM ogrenci
        INNER JOIN sinif ON ogrenci.sinif_id = sinif.sinif_id
        INNER JOIN sube ON ogrenci.sube_id = sube.sube_id WHERE ogrenci.ogrenci_id = (?)
        '''
        data = (student_id, )
        db.cur.execute(sql, data)
        data = db.cur.fetchone()
        db.close()
        if data:
            student = Student(data[0], data[1], data[2], data[3], data[4], data[5], ogrenci_id=data[6], sifre=data[7], sinif_id=data[8], sube_id=data[9])
            return student
        else:
            return False
    
    def getStudents(self):
        studentList = []
        db = DB()
        sql = '''
        SELECT ogrenci.ogrenci_no, ogrenci.ad, ogrenci.soyad, ogrenci.cinsiyet, sinif.value, sube.value
        FROM ogrenci
        INNER JOIN sinif ON ogrenci.sinif_id = sinif.sinif_id
        INNER JOIN sube ON ogrenci.sube_id = sube.sube_id
        '''
        db.cur.execute(sql)
        datas = db.cur.fetchall()
        db.close()
        if datas:
            for data in datas:
                student = Student(data[0], data[1], data[2], data[3], data[4], data[5])
                studentList.append(student)
            return studentList
        else:
            return False

    def addStudent(self, student):
        db = DB()
        sql = '''
            INSERT INTO ogrenci (ogrenci_no, sifre, ad, soyad, cinsiyet, sinif_id, sube_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        data = (student.ogrenci_no, student.sifre, student.ad, student.soyad, student.cinsiyet, student.sinif, student.sube)
        db.cur.execute(sql, data)
        db.conn.commit()
        db.close()

    def deleteStudent(self, student_id):
        db = DB()
        sql = '''
        DELETE FROM ogrenci WHERE ogrenci_id = (?)
        '''
        data = (student_id,)
        db.cur.execute(sql, data)
        db.conn.commit()
        db.close()

    def updateStudent(self, student):
        db = DB()
        sql = '''
        UPDATE ogrenci SET ogrenci_no = ?, sifre = ?, ad = ?, soyad = ?, cinsiyet = ?, sinif_id = ?, sube_id = ? WHERE ogrenci_id = ?
        '''
        data = (student.ogrenci_no, student.sifre, student.ad, student.soyad, student.cinsiyet, student.sinif_id, student.sube_id, student.ogrenci_id)
        db.cur.execute(sql, data)
        db.conn.commit()
        db.close()
    
    def sayilariGetir(self, student_id):
        db = DB()

        sql = '''
            SELECT *
            FROM ogrenci
            INNER JOIN ders ON ogrenci.sinif_id = ders.sinif_id
            WHERE ogrenci.ogrenci_id = (?)
        '''
        data= (student_id, )
        db.cur.execute(sql, data)
        derssayisi = db.cur.fetchall()
        derssayisi = len(derssayisi)

        sql = '''
            SELECT *
            FROM ogrenci
            INNER JOIN ders ON ogrenci.sinif_id = ders.sinif_id
            INNER JOIN sinav ON ders.ders_id = sinav.ders_id
            WHERE ogrenci.ogrenci_id = (?)
        '''
        data= (student_id, )
        db.cur.execute(sql, data)
        sinavsayisi = db.cur.fetchall()
        sinavsayisi = len(sinavsayisi)

        sql = '''
            SELECT *
            FROM ogrenci
            INNER JOIN sonuc ON sonuc.ogrenci_id = ogrenci.ogrenci_id
            WHERE ogrenci.ogrenci_id = (?)
        '''
        data= (student_id, )
        db.cur.execute(sql, data)
        sonucsayisi = db.cur.fetchall()
        sonucsayisi = len(sonucsayisi)

        sql = '''
            SELECT *
            FROM ogrenci
            INNER JOIN yoklama ON ogrenci.ogrenci_id = yoklama.ogrenci_id
            WHERE ogrenci.ogrenci_id = (?) AND yoklama.varMi = 0
        '''
        data= (student_id, )
        db.cur.execute(sql, data)
        yoklamasayisi = db.cur.fetchall()
        yoklamasayisi = len(yoklamasayisi)


        return derssayisi, sinavsayisi, sonucsayisi, yoklamasayisi