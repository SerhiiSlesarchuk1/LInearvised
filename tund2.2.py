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

# # Ввод данных от пользователя
# user_input = input("Введите число или текст: ")

# # Проверка, является ли введенное значение числом
# if user_input.isdigit() or (user_input.replace('.', '', 1).isdigit() and user_input.count('.') < 2):
#     # Преобразуем введенное значение в число
#     try:
#         num = float(user_input)
        
#         if num.is_integer():
#             # Если число целое, находим 50%
#             result = num * 0.5
#             print(f"Arv on täisarv. 50% -st {num} = {result}")
#         else:
#             # Если число дробное, находим 70%
#             result = num * 0.7
#             print(f"Arv on murdosa. 70% -st {num} = {result}")
#     except ValueError:
#         print("Numbrite teisendamise viga.")
# else:
#     # Если введено не число, проверяем текст
#     if user_input.isalpha():
#         print(f"Olete sisestanud teksti: {user_input}")
#     else:
#         print("Sisestatud väärtus, mis ei ole arv ega tekst.")

#Ül 6
# import math

# valik = input("Kas soovite lahendada ruutvõrrandi? (jah/ei): ").strip().lower()
# if valik != "jah":
#     print("Head aega!")
# else:
#     try:
#         a = float(input("Sisestage kordaja a: "))
#         b = float(input("Sisestage kordaja b: "))
#         c = float(input("Sisestage kordaja c: "))
#     except ValueError:
#         print("Viga: Sisestage arvulised väärtused.")
#     else:
#         if a == 0:
#             print("Viga: kordaja a ei tohi olla 0.")
#         else:
#             D = b ** 2 - 4 * a * c
#             print(f"Diskriminant D = {D}")

#             if D > 0:
#                 x1 = (-b + math.sqrt(D)) / (2 * a)
#                 x2 = (-b - math.sqrt(D)) / (2 * a)
#                 print(f"Kaks lahendit: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
#             elif D == 0:
#                 x = -b / (2 * a)
#                 print(f"Üks lahend: x = {round(x, 2)}")
#             else:
#                 print("Lahend puudub (D < 0)")