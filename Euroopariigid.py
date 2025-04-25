from random import *
def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    file=open(f,'r',encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid

riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnad.txt")

#Lisa uus Riik ja Pealinn
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
