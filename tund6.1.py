from random import randint
andmed={}
andmed= {"nimi": "Mari", "vastus": 25, "keel": "eesti"}
andmed=dict(nimi="Mari", vastus=25, keel="eesti")
print(andmed)
print(andmed["nimi"])
print(andmed.get("nimi"))
print(andmed.get("nimi_","Ei ole sõnastikus"))
print(andmed.keys())
print(andmed.values())
for k,v in andmed.items():
    print(k, v)
andmed["email"]="serhiislesarchuk@gmail.com"
print(andmed)
andmed["prillid"]=True
print(andmed)
andmed.update({"nimi":"kati"})
read=["mis on python?-programmerimiskeel", "eesti pealinn?-Tallinn"]
kus_vas={}
for rida in read:
    kysimus, vastus=rida.split("-")
    kus_vas[kysimus.strip()]=vastus.strip()
    print(kus_vas)

kysimused=list(kus_vas.keys())
n=randint(0, len(read)-1)
valitud_kysimus=kysimused[n]
print(valitud_kysimus)
vastus=input("Sisesta vastus: ")
if kus_vas[valitud_kysimus].lower()==vastus.lower():
    print("Õige vastus")
else:
    print("Vale vastus")



#Ülesande 6.1
import random

# Sõnastik
sonastik={'koer': 'собака','kass': 'кошка','maja': 'дом','auto': 'машина','päike': 'солнце'}
def peamenyy():
    """
    """
    while True:
        print("\nValikud:")
        print("1 - Eesti -> Vene")
        print("2 - Vene -> Eesti")
        print("3 - Lisa sõna")
        print("4 - Paranda sõna")
        print("5 - Test")
        print("6 - Välju")
        valik=input("Vali: ")
        if valik=='1':
            est=input("Eesti sõna: ")
            print("Vene keeles:", sonastik.get(est, "Ei leitud"))
        elif valik=='2':
            rus=input("Vene sõna: ")
            leitud=False
            for e, r in sonastik.items():
                if r==rus:
                    print("Eesti keeles:", e)
                    leitud=True
                    break
            if not leitud:
                print("Ei leitud")
        
        elif valik=='3':
            est=input("Uus eesti sõna: ")
            rus=input("Vene tõlge: ")
            sonastik[est]=rus
            print("Lisatud!")
        
        elif valik=='4':
            est=input("Millist eesti sõna parandada: ")
            if est in sonastik:
                rus=input("Uus vene tõlge: ")
                sonastik[est] = rus
                print("Parandatud!")
            else:
                print("Ei leitud")
        
        elif valik=='5':
            oige=0
            kokku=0
            for e, r in random.sample(list(sonastik.items()), len(sonastik)):
                vastus=input(f"{e} -> ")
                if vastus==r:
                    print("Õige!")
                    oige+=1
                else:
                    print("Vale! Õige oli:", r)
                kokku+=1
            print("Tulemus:", round(oige / kokku * 100), "%")
        elif valik=='6':
            break
        else:
            print("Vale valik!")
peamenyy()


