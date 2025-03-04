from math import *
#-----------------------------------------
print("Ruudu karakteristikud")
try:
    a=int(input("Sisesta ruudu külje pikkus =>" ))
    if a>0:
        S=a**2
        print(f"Ruudu pindala, {S}")
        P=4*a
        print(f"Ruudu ümbermõõt {P}")
        di=a*sqrt(2)
        print("Ruudu diagonaal", round(di,2))
    else:
        print("Külg ei saa olla <=0-ga")
except:
    print("Külje suurus on vaja int formaadis sisestada!")
#------------------------------------------