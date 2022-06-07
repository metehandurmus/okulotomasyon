from flask import Flask, redirect, render_template, session, url_for, request, flash
from controller.DersManager import DersManager
from controller.LoginManager import LoginManager
from controller.SinavManager import SinavManager
from controller.StudentManager import StudentManager
from controller.SonucManager import SonucManager
from controller.YoklamaManager import YoklamaManager
from controller.OgretmenManager import OgretmenManager

app = Flask(__name__)
app.secret_key = b'okulotomasyonsecretkey'

studentM = StudentManager()
sonucM = SonucManager()
dersM = DersManager()
sinavM = SinavManager()
yoklamaM = YoklamaManager()
ogretmenM = OgretmenManager()

@app.route('/')
def home():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        sayilar = studentM.sayilariGetir(session['id'])
        data = sonucM.tumSonuclar(session['id'])
        print(data)
        liste = sonucM.secilenleriGetir(session['id'])
        return render_template('ogrenci/anasayfa.html', student=student, sayilar = sayilar, data = data, liste=liste)
    elif session['perm'] == 2:
        ogretmen = ogretmenM.getOgretmen(session['id'])
        dersler = ogretmenM.getOgretmenDersler(session['id'])
        return render_template('ogretmen/anasayfa.html', ogretmen=ogretmen, dersler=dersler)
    elif session['perm'] == 3:
        pass

@app.route('/ogrenci/dersler')
def dersler():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        dersler = dersM.ogrenciDersGetir(session['id'])
        return render_template('ogrenci/dersler.html', student=student, dersler=dersler)
    else:
        return redirect(url_for('home'))

@app.route('/ogrenci/sinavlar')
def sinavlar():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        sinavlar = sinavM.aciklananSinavlar(session['id'])
        return render_template('ogrenci/sinavlar.html', student=student, sinavlar=sinavlar)
    else:
        return redirect(url_for('home'))

@app.route('/ogrenci/sonuclar')
def sonuclar():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        sonuclar = sonucM.sonucGetir(session['id'])
        print(sonuclar)
        return render_template('ogrenci/sonuc.html',  student=student, sonuclar=sonuclar)
    else:
        return redirect(url_for('home'))

@app.route('/ogrenci/yoklama')
def yoklama():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        yoklama = yoklamaM.yoklamaGetir(session['id'])
        return render_template('ogrenci/yoklama.html',  student=student, yoklama=yoklama)
    else:
        return redirect(url_for('home'))

@app.route('/ogrenci/ozlukbilgileri')
def ogrenciOzlukBilgileri():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        return render_template('ogrenci/ozluk.html',  student=student)
    else:
        return redirect(url_for('home'))

@app.route('/ogrenci/sifredegistir', methods=['GET', 'POST'])
def ogrenciSifreDegistir():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        if request.method == 'POST':
            oldp = request.form.get('oldp')
            newp = request.form.get('newp')
            newp2 = request.form.get('newp2')
            if oldp == student.sifre:
                if newp == newp2 and newp != "":
                    student.sifre = newp
                    studentM.updateStudent(student)
                    flash("<div class='my-4 text-success'>Şifreniz başarı ile değiştirildi.</div>")
                else:
                    flash("<div class='my-4 text-danger'>Yeni şifreleriniz uyuşmuyor.</div>")
            else:
                flash("<div class='my-4 text-danger'>Eski şifreniz yanlış.</div>")
            return(redirect(url_for('ogrenciSifreDegistir')))
        return render_template('ogrenci/sifredegistir.html',  student=student)
    else:
        return redirect(url_for('home'))

@app.route('/ogretmen/sinav/ekle', methods=['GET', 'POST'])
def ogretmenSinavEkle():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 2:
        ogretmen = ogretmenM.getOgretmen(session['id'])
        dersler = ogretmenM.getOgretmenDersler(session['id'])
        if request.method == 'POST':
            ad = request.form.get('sinavadi')
            tarih = request.form.get('sinavtarihi')
            if ad.replace(" ", "") == "" or not tarih:
                flash("Boş alan bırakmayın.")
            else:
                sinav = 1
                if sinavM.sinavEkle(sinav):
                    flash("Başarıyla eklendi.")
                else:
                    flash("Bir sorunla karşılaşıldı.")
        return render_template('ogretmen/sinavekle.html', ogretmen=ogretmen, dersler=dersler)
    else:
        return redirect(url_for('home'))

@app.route('/ogretmen/sinav/<int:id>/gor')
def ogretmenSinavGor(id):
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 2:
        return "1"
    else:
        return redirect(url_for('home'))

@app.route('/ogretmen/ozlukbilgileri')
def ogretmenOzlukBilgileri():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 2:
        ogretmen = ogretmenM.getOgretmen(session['id'])
        return render_template('ogretmen/ozluk.html',  ogretmen=ogretmen)
    else:
        return redirect(url_for('home'))

@app.route('/ogretmen/sifredegistir', methods=['GET', 'POST'])
def ogretmenSifreDegistir():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 2:
        ogretmen = ogretmenM.getOgretmen(session['id'])
        if request.method == 'POST':
            oldp = request.form.get('oldp')
            newp = request.form.get('newp')
            newp2 = request.form.get('newp2')
            if oldp == ogretmen.sifre:
                if newp == newp2 and newp != "":
                    ogretmen.sifre = newp
                    ogretmenM.updateOgretmen(ogretmen)
                    flash("<div class='my-4 text-success'>Şifreniz başarı ile değiştirildi.</div>")
                else:
                    flash("<div class='my-4 text-danger'>Yeni şifreleriniz uyuşmuyor.</div>")
            else:
                flash("<div class='my-4 text-danger'>Eski şifreniz yanlış.</div>")
            return(redirect(url_for('ogretmenSifreDegistir')))
        return render_template('ogretmen/sifredegistir.html',  ogretmen=ogretmen)
    else:
        return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        type = request.form.get('perm')
        no = request.form.get('okulno')
        pw = request.form.get('sifre')
        lm = LoginManager()
        control = lm.loginControl(type, no, pw)
        if control:
            session['id'] = lm.id
            session['perm'] = int(type)
            return redirect(url_for('home'))
        else:
            flash("Numaranızı veya şifrenizi yanlış yazdınız.")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['perm'] = None
    flash("Başarıyla çıkış yaptınız.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=80)