# #Töö 4.4
# #1
# from string import *
# vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
# konsonanti="jflsjdflsjlif"
# numbrid=digits
# märkid=punctuation
# v=k=n=m=t=0
# tekst=input("Sisend (sõna või lause): ").lower()
# tekst_list=list(tekst)
# for s in tekst_list:
#     if s in vokaali:
#         v+=1
#     elif s in konsonanti:
#         k+=1
#     elif s in numbrid:
#         n+=1
#     elif s in märkid:
#         m+=1
#     elif s==" ":
#         t+=1






# sõne="Programmeerimine"
# print(sõne)
# list_sõne=list(sõne)
# print(list_sõne)
# print(f"Viies täht: {list_sõne[4]}")
# print(f"Sõnes on {len(sõne)} t")
# elemendid=[]
# for i in range(5):
#     elemendid.append(input(f"{i+1}. element: "))
# print(elemendid)
# for e in elemendid:
#     print(e)
# #extend
# list_sõne.extend(elemendid)
# print(list_sõne)
# print(elemendid)
# #insert
# elemendid.insert(0,"A")
# print(elemendid)
# #remove
# elemendid.remove("A")
# print(elemendid)
# #pop
# elemendid.pop(0)
# elemendid.pop()
# print(elemendid)
# #index
# ind=list_sõne.index("r")
# print(f"Täht r on {ind}-indeksiga")
# #count
# k=list_sõne.count("r")
# print(f"Täht r kohtume {k} korda sõnas {sõne}")
# #sort
# list_sõne.sort(reverse=True)
# print(list_sõne)
# #reverse
# list_sõne.reverse()
# print(list_sõne)
# #copy
# list_sõne2=list_sõne.copy()
# #clear
# list_sõne2.clear()
# print()

#2.1
# nimed = []
# for i in range(5):
#     nimi = input(f"Palun sisesta {i + 1}. nimi: ")
#     nimed.append(nimi)

# nimed.sort()

# print("\nTähestikulises järjekorras:")
# for nimi in nimed:
#     print(nimi)

# print(f"\nViimati lisatud nimi: {nimed[-1]}")

# muuda = input("\nKas soovid muuta mõnda nime? (jah/ei): ")
# if muuda.lower() == 'jah':
#     vanus = int(input("Sisesta nime muutmiseks järjekord (1-5): "))
#     vana_nimi = nimed[vanus - 1]
#     uus_nimi = input(f"Muuda {vana_nimi}: ")
#     nimed[vanus - 1] = uus_nimi
#     nimed.sort()

#     print("\nUus nimekiri:")
#     for nimi in nimed:
#         print(nimi)

#2.2
# nimi=[]
# for i in range(5):
#     nimi.append(input(f"{i+1}. nimi: "))
# print(nimi)
# list_nimi=list(nimi)

#2.3
# # Vanuste loend
# vanused = [23, 45, 67, 34, 29, 40, 56]

# # Leiame suurima ja väikseima arvu
# suurim_vanus = max(vanused)
# vakeim_vanus = min(vanused)

# # Kogusumma ja keskmine
# kogusumma = sum(vanused)
# keskmine_vanus = kogusumma / len(vanused)

# # Kuvame tulemused
# print(f"Suurim vanus: {suurim_vanus}")
# print(f"Väikseim vanus: {vakeim_vanus}")
# print(f"Kogusumma: {kogusumma}")
# print(f"Keskmine vanus: {keskmine_vanus:.2f}")

#3
arvud = [18, 19, 32, 45, 60, 12]
for arv in arvud:
    print('*' * arv)


