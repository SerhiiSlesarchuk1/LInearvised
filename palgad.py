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

