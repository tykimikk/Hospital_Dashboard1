import json
import datetime

# initial Infos


def trueFal(intg):
    if int(intg) == 2:

        return 0
    else:
        return 1


def date(dt):
    dtl = dt.split("-")
    d = int(dtl[0])
    m = int(dtl[1])
    y = int(dtl[2])
    x = datetime.datetime(y, m, d)
    return x


def imcfx(height, weight):
    imc = weight/(height*height)
    return imc


def calcul_Age(dateN):
    dtl = dateN.split("-")
    d = int(dtl[0])
    m = int(dtl[1])
    y = int(dtl[2])
    x = datetime.datetime(y, m, d)
    now = datetime.datetime.now()
    age = int((now - x).days/365)
    return age


nom = input("Nom ").capitalize()
prenom = input("Prenom ").capitalize()

age = input("Age ")
if len(age) > 3:
    age = calcul_Age(age)
else:
    age = int(age)
try:
    numd = int(input("Dossier No "))
except:
    pass
date_Ee = date(input("Date d'entree "))
date_E = str(date_Ee.strftime("%x"))
try:
    date_Ss = date(input("Date du sortie "))
    date_S = str(date_Ss.strftime("%x"))
except:
    date_S = "Inconnu"
try:
    sejour = int((date_Ss - date_Ee).days)
except:
    sejour = "Inconnu"
print("Sex:  1-male 2-female ")
sex = bool(trueFal(input("Sex ")))
imc = input("IMC ")
if imc == "":
    try:
        imc = int(imcfx(float(input("Height ")), float(input("Weight "))))
    except:
        pass


motifs = []
while True:
    motif = input("Motifs de consultation : ").capitalize()
    if bool(motif):
        motifs.append(motif)
    else:
        break

print("Douleur Typique:  1-Oui 2-No ")
dlr = bool(trueFal(input("")))
print("Vommisements:  1-Oui 2-No ")
vom = bool(trueFal(input("")))

sps = []
while True:
    sp = input("Signes Physiques: ").capitalize()
    if bool(sp):
        sps.append(sp)
    else:
        break

print("Fievre:  1-Oui 2-No ")
fievre = bool(trueFal(input("")))
print("Asthenie:  1-Oui 2-No ")
asthenie = bool(trueFal(input("")))
print("AEG:  1-Oui 2-No ")
aeg = bool(trueFal(input("")))
print("SIRS:  1-Positif 2-Negatif ")
sirs = bool(trueFal(input("")))
gb = float(input("Gb "))
hb = float(input("Hb "))
plq = float(input("plq "))
lip = int(input("lipasemie "))
print("CRP:  ?")
crp = 0
if int(input("")) > 10:
    crp = 1
crp = bool(crp)
bio_autres = {}
while True:
    bio = input("Autre signes biologiques: ")
    if bool(bio):
        sign = bio.split("-")[0].upper()
        quan = bio.split("-")[1]
        ter = bio.split("-")[2].capitalize()
        bio_autres[sign] = [quan, ter]
    else:
        break
echo = input("Echographie .. ").capitalize()
belt = input("score beltazar  ").capitalize()
print("REA:  1-Oui 2-No ")
rea = bool(trueFal(input("")))
anta = int(input("Antalgique palier ?  "))
atbq = []
while True:
    atb = input("ATB: oui/nn ")
    if bool(atb):
        print("Fievre:  1-Oui 2-No ")
        fievre_cp = bool(trueFal(input("")))
        print("Elevation Gb:  1-Oui 2-No ")
        gb_cp = bool(trueFal(input("")))

        atbq.append(fievre_cp)
        atbq.append(gb_cp)
    else:

        break

evod = []
while True:
    evo = input("Evolution: defav ? ").capitalize()
    if bool(evo):
        evod.append(evo)
    else:
        break
print("Treatement Medical:  1-Oui 2-No ")
trtmed = bool(trueFal(input("")))

print("Treatement Chirurgical:  1-Oui 2-No ")
trtchir = bool(trueFal(input("")))
moment = "none"
pourqoui = ""
if trtchir:
    print("Moment:  1-Meme sejour  2-06-08 S Apres ")
    moment = bool(trueFal(input("")))
    if not moment:
        pourqoui = input("Pourquoi? ")
print("Suites post op :  1-Simples 2-Complique ")
suites = bool(trueFal(input("")))


dict = {numd: {
    "nom": nom,
    "prenom": prenom,
    "age": age,
    "date_E": date_E,
    "date_S": date_S,
    "sejour": sejour,
    "sex": sex,
    "imc": imc,
    "motifs": motifs,
    "dlr": dlr,
    "vom": vom,
    "sps": sps,
    "fievre": fievre,
    "asthenie": asthenie,
    "aeg": aeg,
    "sirs": sirs,
    "gb": gb,
    "hb": hb,
    "plq": plq,
    "lip": lip,
    "crp": crp,
    "bio_autres": bio_autres,
    "echo": echo,
    "balt": belt,
    "rea": rea,
    "anta": anta,
    "atbq": atbq,
    "evod": evod,
    "trtmed": trtmed,
    "trtchir": trtchir,
    "moment": moment,
    "pourquoi": pourqoui,
    "suites": suites,
}}
try:
    with open("data.json", "r") as d:
        data = json.load(d)
        data.append(dict)
except:
    data = []
    data.append(dict)
    pass
with open("data.json", "w") as d:
    json.dump(data, d, indent=2)
