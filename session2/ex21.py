"""
    Veti primi stringuri de la tastatura, pana cand primiti stringul 'exit'.
    Va trebui sa printati o lista cu stringurile primite fara ultimul caracter
    al fiecarui string.

    Observatii:
        - lungimea stringurilor va fi intotdeauan cel putin 1

    exemplu:
        Veti primi: 'cmi', 'center', 'for', 'machines'
        Veti printa: ['cm', 'cente', 'fo', 'machine']
"""
s=input('cuvinte= ')
l=[]
while s!='exit':
    print('inca un cuvant')
    l.append(s[0:len(s)-1])
    s=input("cuvinte= ")

print(l)





