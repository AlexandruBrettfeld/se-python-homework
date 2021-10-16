"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
s=input().lower()
vocale=0
consoane=0

for i in s:
    if i=="a" or i=="e" or i=="i" or i== "o" or i=="u":
        vocale=vocale+1
consoane=len(s)-vocale

print(f"Cuvantul {s} are {vocale} vocale si {consoane} consoane.")
