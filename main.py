import os
from flask import Flask, render_template, request, redirect
from data import db_session
from data import otzyv

app = Flask(__name__)
global list

@app.route('/')
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/action')
def action():
    return render_template("action.html")

@app.route('/galery')
def galery():
    return render_template("galery.html")

@app.route('/group')
def group():
    return render_template("group.html")

@app.route('/personal')
def personal():
    return render_template("personal.html")

@app.route('/uslugi')
def uslugi():
    return render_template("uslugi.html")


@app.route('/posesh', methods=['POST', 'GET'])
def posesh():
    if request.method == 'GET':
        return render_template("posesh.html", flag=0)
    elif request.method == 'POST':
        print("Заявка на пробное посещение")
        print("Имя: "+request.form['name'])
        print("Телефон: "+request.form['telefon'])
        print("Email: "+request.form['email'])
        print("Дата: "+request.form['data'])
        print("Примечание: "+request.form['text'])
        return render_template("posesh.html", flag=1)


@app.route('/kard', methods=['POST', 'GET'])
def kard():
    if request.method == 'GET':
        return render_template("kard.html", flag=0)
    elif request.method == 'POST':
        print("Заявка на получение клубной карты")
        print("Имя: "+request.form['name'])
        print("Телефон: "+request.form['telefon'])
        print("Email: "+request.form['email'])
        print("Примечание: "+request.form['text'])
        return render_template("kard.html", flag=1)


@app.route('/letter', methods=['POST', 'GET'])
def letter():
    if request.method == 'GET':
        return render_template("letter.html", flag=0)
    elif request.method == 'POST':
        Name1 = request.form['name']
        Text1 = request.form['text']
        otz = otzyv.Otzyv()
        otz.Name = Name1
        otz.Text = Text1
        db_session.global_init("db/data_base.sqlite")
        session = db_session.create_session()
        session.add(otz)
        session.commit()
        return render_template("letter.html", flag=1)


@app.route('/comments')
def comments():
    db_session.global_init("db/data_base.sqlite")
    session = db_session.create_session()
    object = session.query(otzyv.Otzyv)
    session.commit()
    return render_template("comments.html", obj=object)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
