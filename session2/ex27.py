"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un string aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import random
a=int(input())
l=['a','s','y','h']
g=[]
for i in range(a):
    g.append(random.choice(l))
print("".join(g))


