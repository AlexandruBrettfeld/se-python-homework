"""
    Veti primi un string de la tastatura.
    Veti primi un numar intreg de la tastatura, x.
    Va trebui sa creati un dictionar care sa contina ca si chei, toate numerele
    pana la x, iar ca si valori caracterele de pe indexurile corespunzatoare.

    Observatii:
        - lungimea stringului va fi mereu egala cu numarul primit
        - indexarea in python incepe de la 0 (prima cheie va fi 0)

    exemplu:
        Veti primi: 'cmi', 3
        Veti printa: {
            0: 'c',
            1: 'm',
            2: 'i'
        }
"""
s=input('sir= ')
x=int(input('x= '))
d1={}

while len(s)!=x:
    print('stringul are o lungime diferita de x. Introdu x din nou')
    s=input("sir= ")
l=[]
for i in s:
    l.append(i)
for i in range(len(s)):
    d1[i]=l[i]
print(d1)


