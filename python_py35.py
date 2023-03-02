import random

lista=[]

for _ in range(10):
    szamok =random.randint(1,3)
    lista.append(szamok)
print("A generált számok: ", lista)

felh_szam= int(input("Adj meg egy számot [1;3] intervallumon belül: "))

while felh_szam in szamok:
    szamok.remove(felh_szam)

print("A módosított lista: ", szamok)
