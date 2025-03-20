# a=0
# while a==0:
#     print(a)
#     a=int(input("a: "))
# while True:
#     print(a)
#     a=int(input("a: "))
#     if a==100: break
# print()
# for i in range(0,10,1):
#     print(f"{i+1}. samm")
# print()
# for i in range(1,11):
#     print(f"{i}. samm")
#----------------------------------
# ÜL 1
# while True:
#     try:
#         nimi=input("Tere! mis su nimi on?: ")
#         if nimi.isalpha(): break
#     except:
#             print("Viga!")
# while True:
#     try:
#         k=int(input("Mitu korda tervitada: "))
#         if k>0: break
#     except:
#            print("Viga")
# #1 variant---------------------------
# i=0
# while True:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i}. korda")
#     if i==k: break
# #2 variant----------------------------
# i=0
# while i<k:
#      i+=1
#      print(f"Ole tervitatud, {nimi}, {i}. korda")
# #3 variant----------------------------
# print("For")
# for i in range(1,k+1):
#      print(f"Ole tervitatud, {nimi}, {i}. korda")
#ÜL 2
# summa=0
# j=0
# while True:
#     try:
#         a=float(input("a: "))
#         summa+=a
#         j+=1
#         if j==10: break
#     except:
#         print("ebaõnnestuda")
# print()
# for j in range(0,1):
#     print(f"summa on {summa}")
#---------------------------------
#ÜL 3
# import random
# salajane_number=random.randint(1, 50)
# katseid=5  

# print("\nMa mõtlesin numbri välja vahemikus 1 kuni 50. Proovi see ära arvata!")

# for katse in range(1, katseid + 1):
#     pakkumine = int(input(f"Katse {katse}/{katseid}. Sisesta number: ")) 

#     if pakkumine == salajane_number:
#         print("Palju õnne!  Sa arvasid numbri ära!")
#         break
#     elif pakkumine < salajane_number:
#         print("Salajane number on suurem.")
#     else
#         print("Salajane number on väiksem.")

# if pakkumine != salajane_number:
#     print(f"\nSa kaotasid!  Õige number oli: {salajane_number}")
#--------------------------------------
#ÜL 4
# for i in range(1, 11):
#     for j in range(1, 11):
#         /print(f"{i} × {j} = {i * j}")
#     print()  
#--------------------------------------
#ÜL 5
# N = int(input("Sisesta ruudu suurus N: "))

# for i in range(N):
#     for j in range(N):
#         if i == j or i + j == N - 1:
#             print("X", end=" ")  
#         else:
#             print("O", end=" ")  
#     print()  
#--------------------------------------
#ÜL 6
#1 variant
# for i in range(5):
#     print("* " * 5)
# #------------------
# #2 variant
# for i in range(1, 6):
#     print("* " * i)
# #------------------
# #3 variant
# for i in range(5, 0, -1):
#     print("* " * i)
#--------------------------------------
#ÜL 7
# import random  

# for i in range(5):  
#     print(random.randint(0, 9), end="")  

# print()  
#--------------------------------------
#ÜL 8
# paaris_loendur = 0
# paaritu_loendur = 0

# for arv in range(1, 101):  
#     if arv % 2 == 0:
#         print(f"{arv} - paaris")
#         paaris_loendur += 1
#     else:
#         print(f"{arv} - paaritu")
#         paaritu_loendur += 1

# print(f"\nPaaris arvude arv: {paaris_loendur}")
# print(f"Paaritute arvude arv: {paaritu_loendur}")
#---------------------------------------
#ÜL 9
# for i in range(1, 11):  
#     print(f"5 × {i} = {5 * i}")
#---------------------------------------
