# from random import *
# sõnad=["Arvuti","Hiir","Kuvar"]
# salasõna=choice(sõnad)
# print(salasõna)
# k=len(salasõna)
# p=6
# while p>0:
#     print("_ "*k)
#     print(f"On jäänud {p} katset")
#     p-=1
#     sõna=input("Sisesta oma variant: ")
#     if sõna==salasõna:
#         print("Huraa!")
#         break
#     else:
#         pass

#4.3
from random import *
o=-1
wrds=["cat","dog","cow","mouse","hen","lizard","ant","bee","wasp","fly","rat","fish","horse","goat","pig"]

rnd=choice(wrds)
rndlist=list(rnd)
k=len(rndlist)
for i in range(0,6,1):
    o=-1
    print("Guess the word. You have ", 6-i, "attempts")
    answer=input("[] "*k)
    answerlist=list(answer)
    for a in range(0,k,1):
        o+=1
        if answerlist[o]==rndlist[o]:
            print(answerlist[o],end=" ")

        else:
            print("*",end=" ")
    print()
    if answer==rnd:
        print("Correct! the word was ", rnd, )
        break
    else:
        print("Wrong! ", 6-i-1, " attemps remains")