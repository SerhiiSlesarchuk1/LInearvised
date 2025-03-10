# from ma+th import isnan--------------------------------------------

# #1
# try:
#     arv=input("Sisesta arv:")
#     if arv.isnumeric():
#         arv=int(arv)
#         if arv>0:
#             if arv%2==0:
#                 print("Paaris arv")
#             else:
#                 print("Paaritu arv")
#         else:
#             print("Negatiivn arv")
# except:
#     print("Kirjuta numbreid")

#2
# try:
#     nurk1=float(input("Esimene nurk:"))
#     nurk2=float(input("Teine nurk:"))
#     nurk3=float(input("Kolmas nurk:"))
#     if nurk1>0 and nurk2>0 and nurk3>3:
#         print("Nurgad on posiriivsed")
#         if nurk1+nurk2+nurk3==100:
#             print("See on kolmas")
#             if nurk1==nurk2 and nurk2==nurk3:
#                 print("Võrdkülgne kolmnurk")
#             elif nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
#                 print("Võrdvaarne kolmnurk")
#             else:
#                 print("Erikülgne kolmnurk")
#         else:
#             print("See ei ole kolmnurk")
#     else:
#         print("Negatiivsed nurgad ei soobi")
# except:
#     print("Sisesta ujukomarnud")

#3
# try:
#     soov=input("Kas tahd dekodeerida?:")
#     if soov=="Jah":
#         try:
#             nr=int(input("Päeva number: "))
#             if nr in range(1,8):
#                 if nr==1:
#                     print("Esmaspäev")
#                 elif nr==2:
#                     print("Teisipäev")
#                 elif nr==3:
#                     print("Kolmapäev")
#                 elif nr==4:
#                     print("Neljapäev")
#                 elif nr==5:
#                     print("Reedel")
#             else:
#                 print("Ainult 1-7")
#         except:
#             print("Numbrid vahemikust 1-7")
# except:
#     print("Mul on vaja vastus jah või ei")

#4
# päev=int(input("kirjuta oma sünnipäev: "))
# kuu=int(input("kirjuta oma sünnikuu: "))
# if (1<=päev<=31) and (1<=kuu<=12):
#     if (kuu==3 and päev>=21) or (kuu==4 and päev<=19):
#         tähemärk="Jäär"
#     elif (kuu==4 and päev>=20) or (kuu==5 and päev<=20):
#         tähemärk="Sõnn"
#     elif (kuu==5 and päev>=21) or (kuu==6 and päev<=20):
#         tähemärk="Kaksikud"
#     elif (kuu==6 and päev>=21) or (kuu==7 and päev<=22):
#         tähemärk="Vähk"
#     elif (kuu==7 and päev>=23) or (kuu==8 and päev<=22):
#         tähemärk="Lõvi"
#     elif (kuu==8 and päev>=23) or (kuu==9 and päev<=22):
#         tähemärk="Neitsi"
#     elif (kuu==9 and päev>=23) or (kuu==10 and päev<=22):
#         tähemärk="Kaalud"
#     elif (kuu==10 and päev>=23) or (kuu==11 and päev<=21):
#         tähemärk="Skorpion"
#     elif (kuu==11 and päev>=22) or (kuu==12 and päev<=21):
#         tähemärk ="Ambur"
#     elif (kuu==12 and päev>=22) or (kuu==1 and päev<=19):
#         tähemärk ="Kaljukits"
#     elif (kuu==1 and päev>=20) or (kuu==2 and päev<=18):
#         tähemärk="Veevalaja"
#     else:
#         tähemärk = "Kalad"
#     print(f"sinu tähemärk on: {tähemärk}")
# else:
#     print("vale andmed palun vaata")

#ü 5

user_input=input("kirjuta number: ")

if user_input():
    num=int(user_input)
    print(f"täis arv. 50% arvest: {num * 0.5}")
   
elif user_input('.', '', 1) and user_input('.') == 1:
    num = float(user_input)
    print(f"Дробное arv. 70% arvest: {num * 0.7}")
   
elif user_input():
    print(f" {user_input}")

else:
    print("vale andmet")