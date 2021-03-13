from flask import Flask
from flask import render_template, send_file
from flask import request
import requests
import datetime
import json
from docx2pdf import convert
from collections import defaultdict
import docarchive as dc
import os
app = Flask(__name__)

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
                if i["nom"] == info or i["prenom"] == info:
                    searchinarch.append(i)

        elif len(info.split(" ")) == 2:
            name = info.split(" ")[0]
            surname = info.split(" ")[1]
            for i in infos:
                if i["nom"] == name or i["prenom"] == surname:
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
cases = len(data)
ratio = int((malenb / cases)*100)
dlrt = int((dlrtypique/cases)*100)
evolfav = int((evol/cases)*100)
casesMonth = defaultdict(list)
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
    casesMonth[i] = []
for i in infos:
    casesMonth[str(month(i["date_E"]))].append(i["nom"])
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


@ app.route('/login')
def login():
    return render_template("login.html")


@ app.route('/')
def index():
    return render_template("index.html", cases=cases, ratio=ratio, dlrt=dlrt, evolfav=evolfav, casesMonth=casesMonth, casesAge=casesAge)


@ app.route('/charts')
def charts():
    return render_template("charts.html", cases=cases, ratio=ratio, dlrt=dlrt, evolfav=evolfav, casesMonth=casesMonth, casesAge=casesAge)


@ app.route('/tables')
def tables():
    return render_template("tables.html", data=infos)


@ app.route('/archive')
def archive():
    return render_template("archive.html", data=infos)


@ app.route('/add')
def add():
    return render_template("add.html")


@ app.route('/archive/<name>')
def download(name):
    dc.wordmaker(name)
    return send_file(os.getcwd() + "/docx/"+name + ".docx", as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@ app.route('/search', methods=['GET', 'POST', 'DELETE'])
def search():
    name = request.form.get('searchbox')
    parseSearch(name)

    return render_template("search.html", data=searchinarch)


if __name__ == "__main__":
    app.run(debug=True)
