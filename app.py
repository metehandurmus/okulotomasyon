from flask import Flask, redirect, render_template, session, url_for, request, flash
from controller.DersManager import DersManager
from controller.LoginManager import LoginManager
from controller.SinavManager import SinavManager
from controller.StudentManager import StudentManager
from controller.SonucManager import SonucManager
from controller.YoklamaManager import YoklamaManager

app = Flask(__name__)
app.secret_key = b'okulotomasyonsecretkey'

studentM = StudentManager()
sonucM = SonucManager()
dersM = DersManager()
sinavM = SinavManager()
yoklamaM = YoklamaManager()

@app.route('/')
def home():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        sayilar = studentM.sayilariGetir(session['id'])
        data = sonucM.tumSonuclar(session['id'])
        liste = sonucM.secilenleriGetir(session['id'])
        return render_template('ogrenci/anasayfa.html', student=student, sayilar = sayilar, data = data, liste=liste)
    elif session['perm'] == 2:
        pass
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
def ozlukBilgileri():
    if not session.get("perm"):
        return redirect(url_for('login'))
    if session['perm'] == 1:
        student = studentM.getStudent(session['id'])
        return render_template('ogrenci/ozluk.html',  student=student)
    else:
        return redirect(url_for('home'))

@app.route('/ogrenci/sifredegistir', methods=['GET', 'POST'])
def sifreDegistir():
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
            return(redirect(url_for('sifreDegistir')))
        return render_template('ogrenci/sifredegistir.html',  student=student)
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