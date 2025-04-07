from curses.ascii import isalpha


p=[]
i=[]
def Lisa_andmed(p:list,i:list):
    """
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                   palk=float(input("Palk: "))
                except:
                    print("Palk on arv!")
                break
                print("Andmed on lisatud")
        except:
             print("kirjuta ainult tähtede kasutades")
    p.append(palk) 
    i.append(nimi)
def Suurim_palk(p:list,i:list):
    """
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    for j in range(k):
        ind=p.index(suurim,)
        print(f"Saab kätte{i[ind]}")
        ind=ind+1

def Sorteerimine(p:list,i:list)-> any:
    """
    """
    v=input("Vali märk: >(kasvav või < (kahanev)")
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

def Võrdsed_palgad(p:list,i:list):
    """
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1