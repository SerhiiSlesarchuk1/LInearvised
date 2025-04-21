from palgad1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("andmed: ")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1-Andmete lisamiseks\n2_Andmete kustutamiseks nime järgi")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest?: "))
        for i in range(k):
         Lisa_andmed(palgad,inimesed)
    elif v==2:
        kustuda_andmed(palgad,inimesed)
    elif v==3:
       s
    
    elif v==2:
        kustuda_andmed(palgad,inimesed)


#6
def sama_palk(palgad, nimed):
    for palk in set(palgad):
        mitu = palgad.count(palk)
        if mitu > 1:
            print(f"\nPalk: {palk}")
            for i in range(len(palgad)):
                if palgad[i] == palk:
                    print(nimed[i])

#7
def otsi_palk(nimi, nimed, palgad):
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            print(f"{nimed[i]} saab {palgad[i]}")

#8
def palk_filter(nimed, palgad, summa, rohkem=True):
    for i in range(len(palgad)):
        if rohkem and palgad[i] > summa:
            print(nimed[i], palgad[i])
        elif not rohkem and palgad[i] < summa:
            print(nimed[i], palgad[i])



#12
def sort_names(nimi_list, reverse=False):
    return sorted(nimi_list, reverse=reverse)
def main():
    nimi=["Aleks","Anna","Maria","Julia","Boris","Yana","Dmitry"]
    print("Valige sortimissuund:")
    print("1. A-st Z-ni")
    print("2. Z-st A-ni")
    choice=input("Sisestage 1 või 2: ")
    if choice=="1":
        sorted_names=sort_nimi(nimi, reverse=False)
    elif choice=="2":
        sorted_names=sort_nimi(nimi, reverse=True)
    else:
        print("Vale sisend. Vaikimisi sortimine (A kuni Z).")
        sorted_names=sort_nimi(nimi)
    print("\nSorteeritud nimed:")
    for name in sorted_names:
        print(name)

#18
def leia_nimed_ja_palgad(andmed, taht):
    taht=taht.upper()
    tulemused=[]
    for nimi, palk in andmed.items():
        if nimi.upper().startswith(taht):
            tulemused.append((nimi, palk))
    return tulemused
def main():
    # Näidisandmed: nimi – palk
    andmed={"Aivar": 2500,"Annika": 3200,"Peeter": 2800,"Kadi": 3100,"Arne": 2700,"Mari": 2900}
    taht=input("Sisesta täht, millega nimi algab: ").strip()
    if not taht:
        print("Täht puudub!")
        return
    tulemused=leia_nimed_ja_palgad(andmed, taht)
    if tulemused:
        print("\nNimed ja palgad:")
        for nimi, palk in tulemused:
            print(f"{nimi} – {palk} €")
    else:
        print(f"Ühtegi nime ei leitud tähega '{taht}'.")

def Bonus_Salary(p: list, i: list):
    """
    """
    for idx, (name, salary) in enumerate(zip(i, p), 1):
        print("\nCurrent employees and salaries: ")
        print(f"{idx}. {name}: {salary}")
    try:
        choise=int(input("Valige töötaja: ")) - 1
        bonus=float(input("Kirjutage mittu protsentis palk tõused: "))
        if 0<=choice<len(i) and bonus>0:
            original_salary=p[choice]
            bonus_to=bonus/100
            bonus_salary=original_salary*bonus_to+original_salary
            print(f"New salary is: {bonus_salary}")
        else:
            print("Valige eksisteeriv töötaja ja valige bonus rohkem kui 0")

    except:
        print("Error!")
