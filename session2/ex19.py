"""
    Veti primi un string de la tastatura.
    Va trebui sa printati un tuplu care sa contina toate literele acelui string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: ('c', 'm', 'i')
"""
s=input('sir= ')
l=[]
for i in s:
    l.append(i)
l=tuple(l)
print(l)