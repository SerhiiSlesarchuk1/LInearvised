#Töö 4.4
# 1
from string import *
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti="jflsjdflsjlif"
numbrid=digits
märkid=punctuation
v=k=n=m=t=0
tekst=input("Sisend (sõna või lause): ").lower()
tekst_list=list(tekst)
for s in tekst_list:
     if s in vokaali:
        v+=1
     elif s in konsonanti:
        k+=1
     elif s in numbrid:
        n+=1
     elif s in märkid:
        m+=1
     elif s==" ":
        t+=1


# sõne="Programmeerimine"
# print(sõne)
# list_sõne=list(sõne)
# print(list_sõne)
# print(f"Viies täht: {list_sõne[4]}")
# print(f"Sõnes on {len(sõne)} t")
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

3
arvud = [18, 19, 32, 45, 60, 12]
for arv in arvud:
    print('*' * arv)

5
loend = [1, 2, 3, 4, 5, 6]
n = int(input("Mitu elementi vahetada? "))
for i in range(n):
    loend[i], loend[-1 - i] = loend[-1 - i], loend[i]
print(loend)

6
numbrid = [10, 25, 8, 50, 13]
numbrid[numbrid.index(max(numbrid))] /= len(numbrid)
print(numbrid)

7
nums = [-5, 10, -3, 8, -2]
print(sorted(nums, key=abs))

8
sonad = ['kass', 'koer', 'jänes']
max_pikkus = max(map(len, sonad))
print([s.ljust(max_pikkus, '_') for s in sonad])

11
sõnad=[]
for i in range(1):
    sõnad.append(input(f"{i+1}. sõna: "))
print(sõnad)
print(sõnad,sõnad)
print(sõnad,sõnad,sõnad)
print(sõnad,sõnad,sõnad,sõnad) 

# len() — Возвращает количество элементов (например, символов или чисел).
# list() — Преобразует в список.
# max() — Находит наибольшее значение.
# lower() — Преобразует строку в маленькие буквы.
# punctuation — Строка с знаками препинания.
# input() — Получает текст от пользователя.
# insert() — Вставляет элемент на нужное место в списке.
# append() — Добавляет элемент в конец списка.
# clear() — Удаляет все элементы из списка.
# pop() — Удаляет и возвращает элемент из списка.
# index() — Находит индекс первого элемента.
# count() — Считает, сколько раз элемент встречается в списке.
# reverse() — Переворачивает элементы в списке.
# copy() — Копирует список.
# range() — Создаёт последовательность чисел.
# digits — Строка с цифрами (0-9).
# min() — Находит наименьшее значение.
# sort() — Сортирует список по порядку.
# remove() — Удаляет первый найденный элемент.
# if — Проверяет условие и выполняет код, если оно верно.