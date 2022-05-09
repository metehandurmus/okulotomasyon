from flask import Flask, render_template
from controller.StudentManager import StudentManager
from controller.SonucManager import SonucManager
from model.Student import Student

app = Flask(__name__)
app.secret_key = b'okulotomasyonsecretkey'
    

@app.route('/')
def home():
    sm = SonucManager()
    data = sm.tumSonuclar(1)
    data2 = sm.dersSonuclar(1, 3)
    data3 = sm.dersSonuclar(1, 4)
    data4 = sm.dersSonuclar(1, 5)
    return render_template('ogrenci-anasayfa.html', data = data, data2 = data2, data3=data3, data4=data4)
    

if __name__ == '__main__':
    app.run(debug=True, port=80)