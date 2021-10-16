"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""
a=int(input())
s=0
for i in range(a+1):
    s=i+s
print(s)
