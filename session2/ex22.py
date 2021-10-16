"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
s=input('Cuvant= ')
s=s.upper()
l=[]
for i in range(len(s)):
    l.append(s[i])
for i in range(len(s)):
    if i%2==1:
        l[i]=s[i].lower()

print("".join(l))




