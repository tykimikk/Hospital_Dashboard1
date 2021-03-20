from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, send_file
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import requests
import datetime
import json
from docx2pdf import convert
from collections import defaultdict
import docarchive as dc
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
# CREATE TABLE


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


searchinarch = []


def parseSearch(info):
    searchinarch.clear()
    if info.isnumeric():

        if len(info) == 4:
            year = int(info)
            for i in infos:
                if int(getYear(i["date_E"])) == year:
                    searchinarch.append(i)

        elif len(info) == 5:
            for i in data:
                try:
                    searchinarch.append(i[info])
                except:
                    print("Not found")

    else:
        if len(info.split(" ")) == 1:

            for i in infos:
                if i["nom"].lower() == info.lower() or i["prenom"].lower() == info.lower():
                    searchinarch.append(i)

        elif len(info.split(" ")) == 2:
            name = info.split(" ")[0]
            surname = info.split(" ")[1]
            for i in infos:
                if i["nom"].lower() == name.lower() or i["prenom"].lower() == surname.lower():
                    searchinarch.append(i)
    return searchinarch


def month(dt):
    dtl = dt.split("/")
    d = int(dtl[1])
    m = int(dtl[0])
    y = int(dtl[2])+2000
    x = datetime.datetime(y, m, d).strftime("%b")

    return x


def getYear(dt):
    dtl = dt.split("/")
    d = int(dtl[1])
    m = int(dtl[0])
    y = int(dtl[2])+2000
    x = datetime.datetime(y, m, d).strftime("%Y")

    return x


infos = []
malenb = 0
dlrtypique = 0
evol = 0
vom = 0
fievre = 0
asthenie = 0
aeg = 1
with open("data.json", "r") as d:
    data = json.load(d)
for i in data:
    numd = list(i.keys())[0]
    info = i[numd]
    infos.append(info)
for i in infos:
    if i["sex"]:
        malenb = malenb + 1
for i in infos:
    if i["dlr"]:
        dlrtypique = dlrtypique + 1
for i in infos:
    if i["suites"]:
        evol = evol + 1
    if i["vom"]:
        vom = vom + 1
    if i["fievre"]:
        fievre = fievre + 1
    if i["asthenie"]:
        asthenie = asthenie + 1
    if i["aeg"]:
        aeg = aeg + 1
cases = len(data)
ratio = int((malenb / cases)*100)
dlrt = int((dlrtypique/cases)*100)
evolfav = int((evol/cases)*100)
vom = int((vom/cases)*100)
aeg = int((aeg/cases)*100)
asthenie = int((asthenie/cases)*100)
fievre = int((fievre/cases)*100)


casesMonth19 = defaultdict(list)
casesMonth20 = defaultdict(list)
casesMonth21 = defaultdict(list)

months = ['Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec']
for i in months:
    casesMonth19[i] = []
    casesMonth20[i] = []
    casesMonth21[i] = []

for i in infos:
    if getYear(i["date_E"]) == "2019":
        casesMonth19[str(month(i["date_E"]))].append(i["nom"])
    elif getYear(i["date_E"]) == "2020":
        casesMonth20[str(month(i["date_E"]))].append(i["nom"])
    elif getYear(i["date_E"]) == "2021":
        casesMonth21[str(month(i["date_E"]))].append(i["nom"])
casesAge = defaultdict(list)
casesAge["ttf"] = []
casesAge["fts"] = []
casesAge["six"] = []
casesAge["tw"] = []
for i in infos:
    if i["age"] < 20:
        casesAge["tw"].append(i["nom"])
    elif i["age"] > 20 and i["age"] < 40:
        casesAge["ttf"].append(i["nom"])
    elif i["age"] > 40 and i["age"] < 60:
        casesAge["fts"].append(i["nom"])
    elif i["age"] > 60:
        casesAge["six"].append(i["nom"])
casesBalt = defaultdict(list)
for i in infos:
    if i["balt"] == "A":
        casesBalt["A"].append(i["nom"])
    elif i["balt"] == "B":
        casesBalt["B"].append(i["nom"])
    elif i["balt"] == "C":
        casesBalt["C"].append(i["nom"])
    elif i["balt"] == "D":
        casesBalt["D"].append(i["nom"])
    elif i["balt"] == "E":
        casesBalt["E"].append(i["nom"])
casesBio = defaultdict(list)
for i in infos:
    if int(i["hb"]) < 12:
        casesBio["hb"].append(i["nom"])
    if int(i["gb"]) > 10:
        casesBio["gb"].append(i["nom"])
    if not i["bio_autres"] == []:
        for u in i["bio_autres"]:
            if u == "perturbation de bilan h\u00e9patique":
                casesBio["hep"].append(i["nom"])
            if u == "hyperglyc\u00e9mie":
                casesBio["glyc"].append(i["nom"])
            if u == "Hyponatr\u00e9mie":
                casesBio["ion"].append(i["nom"])

casesTrt = defaultdict(list)
for i in infos:
    if i["trtchir"]:
        casesTrt["chir"].append(i["nom"])
    else:
        casesTrt["med"].append(i["nom"])
sirs = defaultdict(list)
for i in infos:
    if i["sirs"]:
        sirs["pos"].append(i["nom"])
    else:
        sirs["neg"].append(i["nom"])

'''
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        print(request.form.get('name'))
        new_user = User(

            name=request.form.get('name'),
            password=hash_and_salted_password,
        )

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for("archive"))

    return render_template("register.html")
'''


@ app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')

        # Find user by email entered.
        user = User.query.filter_by(name=name).first()

        # Check stored password hash against entered password hashed.
        try:

            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
        except:
            pass

    return render_template("login.html")


@ app.route('/')
def index():
    return render_template("index.html", cases=cases, ratio=ratio, dlrt=dlrt, evolfav=evolfav, casesMonth19=casesMonth19, casesMonth20=casesMonth20, casesMonth21=casesMonth21, casesAge=casesAge, casesTrt=casesTrt, sirs=sirs, vom=vom, aeg=aeg, asthenie=asthenie, fievre=fievre)


@ app.route('/charts')
def charts():
    return render_template("charts.html", casesMonth19=casesMonth19, casesMonth20=casesMonth20, casesMonth21=casesMonth21, casesAge=casesAge, casesBalt=casesBalt, casesBio=casesBio,  casesTrt=casesTrt, sirs=sirs)


@ app.route('/tables')
def tables():
    return render_template("tables.html", data=infos)


@ app.route('/theorie')
def theorie():
    return render_template("theory.html")


@ app.route('/pratique')
def pratique():
    return render_template("pratique.html")


@ app.route('/archive')
@login_required
def archive():
    return render_template("archive.html", data=infos)


@ app.route('/add')
@login_required
def add():
    return render_template("add.html")


@ app.route('/archive/<name>')
@login_required
def download(name):
    try:
        files = os.listdir(os.getcwd()+"/docx")
        for i in files:
            print(i)
            os.remove(os.getcwd()+"/docx/"+i)
    except:
        os.mkdir("docx")
    dc.wordmaker(name)
    return send_file(os.getcwd() + "/docx/"+name + ".docx", as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@ app.route('/search', methods=['GET', 'POST', 'DELETE'])
@login_required
def search():
    name = request.form.get('searchbox')
    parseSearch(name)

    return render_template("search.html", data=searchinarch)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return render_template('noaccess.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
