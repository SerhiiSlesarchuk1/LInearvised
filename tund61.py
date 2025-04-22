from tund611 import *
#------------

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
