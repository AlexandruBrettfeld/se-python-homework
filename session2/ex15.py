"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

x=input()
contor=0
for i in (x):
    if i== 'a'or i=='e' or i=='i' or i=='u' or i=='o':
        contor=contor+1

print(contor)



