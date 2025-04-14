

#1
def kool():
    """
    Täidab kaks loendit ja sorteerib õpilased nende hinnete järgi
    """
    opilased,puudumised=[],[]
    n=int(input("Kui palju õpilasi? "))
    for _ in range(n):
        nimi, puud = input("Nimi: "), int(input("Koolipuudus: "))
        opilased.append(nimi)
        puudumised.append(puud)

    while True:
        valik=input("\n1 – Ülemine n\n2 – Sorteeri\n3 – Komisjonitasu alusel\n4 – Mahaarvamine\n5 – Välju: ")
        if valik=="1":
            for nimi, puud in sorted(zip(opilased, puudumised), key=lambda x: x[1])[:int(input("Топ n: "))]:
                print(f"{nimi}: {puud}")
        elif valik=="2":
            for nimi, puud in sorted(zip(opilased, puudumised), key=lambda x: x[1]):
                print(f"{nimi}: {puud}")
        elif valik=="3":
            for nimi, puud in zip(opilased, puudumised):
                if puud>50:
                    print(f"{nimi} komisjonitasu")
        elif valik=="4":
            for i in range(len(puudumised) - 1, -1, -1):
                if puudumised[i]>100:
                    print(f"{opilased[i]} välja saadetud")
                    opilased.pop(i)
                    puudumised.pop(i)
        elif valik=="5":
            break


#2
import random
def sport():
    """
    Täidab kaks loendit ja sorteerib sportlased nende punktisummade järgi
    """
    sportlased,tulemused=[],[]
    n = int(input("Mitu sportlast? "))
    for _ in range(n):
        nimi=input("Nimi: ")
        sportlased.append(nimi)
        tulemused.append(max([random.randint(1, 100) for _ in range(3)]))
    while True:
        valik = input("\n1 - Ülemine n\n2 - Sorteeri\n3 - Tulemus\n4 - Diskvalifitseerimine\n5 - Väljumine: ")
        if valik=="1":
            for nimi, tulemus in sorted(zip(sportlased, tulemused), key=lambda x: -x[1])[:int(input("Топ n: "))]:
                print(f"{nimi}: {tulemus}")
        elif valik=="2":
            for i, (nimi, tulemus) in enumerate(sorted(zip(sportlased, tulemused), key=lambda x: x[1]), 1):
                print(f"{i}. {nimi}: {tulemus}")
        elif valik=="3":
            name = input("Nimi: ")
            if name in sportlased:
                print(f"{name}: {tulemused[sportlased.index(name)]}")
        elif valik=="4":
            limit = int(input("Minimaalsed punktid: "))
            for i in range(len(tulemused) - 1, -1, -1):
                if tulemused[i] < limit:
                    print(f"{sportlased[i]} diskvalifitseeritud")
                    sportlased.pop(i)
                    tulemused.pop(i)
        elif valik == "5":
            break


#3
def linnad():
    """

    """
    linnad,elanikud=[],[]
    n=int(input("Mitu linna? "))
    for _ in range(n):
        linnad.append(input("Linn: "))
        elanikud.append(int(input("Elanikud: ")))

    while True:
        valik=input("\n1 – Elanikud\n2 – Sorteeri\n3 – Lähim\n4 – Vähem kui n\n5 – Väljumine: ")
        if valik=="1":
            name=input("Linn: ")
            if name in linnad:
                print(f"{name}: {elanikud[linnad.index(name)]}")
        elif valik=="2":
            for nimi, arv in sorted(zip(linnad, elanikud)):
                print(f"{nimi}: {arv}")
        elif valik=="3":
            soov = int(input("Soovitud number: "))
            closest=min(zip(linnad, elanikud), key=lambda x: abs(x[1] - soov))
            print(f"Lähim: {closest[0]}")
        elif valik=="4":
            n = int(input("Vähem kui number: "))
            for nimi, arv in zip(linnad, elanikud):
                if arv<n:
                    print(f"{nimi}: {arv}")
        elif valik=="5":
            break


#4
def pood():
    """
    
    """
    ostud,hinnad =[],[]
    n=int(input("Mitu toodet? "))
    for _ in range(n):
        ostud.append(input("Toode: "))
        hinnad.append(float(input("Hind: ")))

    while True:
        valik=input("\n1 - Osta\n2 - Sorteeri\n3 - Kallis/Odav\n4 - Leia hind\n5 - Kontrollige\n6 - Välju: ")
        if valik=="1":
            toode=input("Ostetud: ")
            if toode in ostud:
                idx=ostud.index(toode)
                print(f"{toode}: {hinnad.pop(idx)}€")
                ostud.pop(idx)
        elif valik=="2":
            for toode, hind in sorted(zip(ostud, hinnad)):
                print(f"{toode}: {hind:.2f}€")
        elif valik=="3":
            print(f"Kallis: {ostud[hinnad.index(max(hinnad))]}, Odav: {ostud[hinnad.index(min(hinnad))]}")
        elif valik=="4":
            toode=input("Toode: ")
            if toode in ostud:
                print(f"{toode}: {hinnad[ostud.index(toode)]}€")
        elif valik=="5":
            print(f"Kontrollige: {sum(hinnad):.2f}€")
        elif valik=="6":
            break

