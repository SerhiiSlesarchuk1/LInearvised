from random import randint
# andmed={}
# andmed= {"nimi": "Mari", "vastus": 25, "keel": "eesti"}
# andmed=dict(nimi="Mari", vastus=25, keel="eesti")
# print(andmed)
# print(andmed["nimi"])
# print(andmed.get("nimi"))
# print(andmed.get("nimi_","Ei ole sõnastikus"))
# print(andmed.keys())
# print(andmed.values())
# for k,v in andmed.items():
#     print(k, v)
# andmed["email"]="serhiislesarchuk@gmail.com"
# print(andmed)
# andmed["prillid"]=True
# print(andmed)
# andmed.update({"nimi":"kati"})
# read=["mis on python?-programmerimiskeel", "eesti pealinn?-Tallinn"]
# kus_vas={}
# for rida in read:
#     kysimus, vastus=rida.split("-")
#     kus_vas[kysimus.strip()]=vastus.strip()
#     print(kus_vas)

# kysimused=list(kus_vas.keys())
# n=randint(0, len(read)-1)
# valitud_kysimus=kysimused[n]
# print(valitud_kysimus)
# vastus=input("Sisesta vastus: ")
# if kus_vas[valitud_kysimus].lower()==vastus.lower():
#     print("Õige vastus")
# else:
#     print("Vale vastus")



#Ülesande 6.1
from curses.ascii import isalpha
import random

# Sõnastik
sonastik = {'koer': 'собака','kass': 'кошка','maja': 'дом','auto': 'машина','päike': 'солнце'}

#eesti -> vene
def tolgi_est_rus(sona):
    return sonastik.get(sona, "Sõna ei leitud!")

#vene -> eesti
def tolgi_rus_est(sona):
    for est, rus in sonastik.items():
        if rus == sona:
            return est
    return "Sõna ei leitud!"

#Lisa uus sõna
def lisa_sona():
    est = input("Sisesta uus sõna eesti keeles: ")
    rus = input("Sisesta selle sõna vene tõlge: ")
    sonastik[est] = rus
    print("Sõna lisatud!")

#Paranda sõna
def paranda_sona():
    est = input("Sisesta parandatav sõna eesti keeles: ")
    if est in sonastik:
        uus_rus = input("Sisesta uus vene tõlge: ")
        sonastik[est] = uus_rus
        print("Sõna parandatud!")
    else:
        print("Sõna ei leitud!")

# Teadmiste test
def testi_teadmisi():
    if not sonastik:
        print("Sõnastik on tühi!")
        return

    oige = 0
    kokku = 0

    suund = input("Vali suund: 1 - eesti -> vene, 2 - vene -> eesti: ")
    sonade_list = list(sonastik.items())
    random.shuffle(sonade_list)

    for est, rus in sonade_list:
        if suund == '1':
            vastus = input(f"Sisesta vene tõlge sõnale '{est}': ")
            if vastus.lower() == rus.lower():
                print("Õige!")
                oige += 1
            else:
                print(f"Vale! Õige vastus on: {rus}")
        elif suund == '2':
            vastus = input(f"Sisesta eesti tõlge sõnale '{rus}': ")
            if vastus.lower() == est.lower():
                print("Õige!")
                oige += 1
            else:
                print(f"Vale! Õige vastus on: {est}")
        kokku += 1

    protsent = (oige / kokku) * 100
    print(f"Test lõppenud! Sinu tulemus: {protsent:.0f}%")

# Põhimenüü
def peamenyy():
    while True:
        print("\nTere tulemast eesti-vene sõnastikku!")
        print("Valikud:")
        print("1 - Tõlgi eesti -> vene")
        print("2 - Tõlgi vene -> eesti")
        print("3 - Lisa uus sõna")
        print("4 - Paranda sõna")
        print("5 - Testi teadmisi")
        print("6 - Välju")

        valik = input("Tee oma valik: ")

        if valik == '1':
            sona = input("Sisesta sõna eesti keeles: ")
            print("Tõlge vene keelde:", tolgi_est_rus(sona))
        elif valik == '2':
            sona = input("Sisesta sõna vene keeles: ")
            print("Tõlge eesti keelde:", tolgi_rus_est(sona))
        elif valik == '3':
            lisa_sona()
        elif valik == '4':
            paranda_sona()
        elif valik == '5':
            testi_teadmisi()
        elif valik == '6':
            print("Head aega!")
            break
        else:
            print("Tundmatu valik, proovi uuesti!")

# Käivitame menüü
peamenyy()



