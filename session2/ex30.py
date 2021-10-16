"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
openList = ["[", "{", "("]
closeList = ["]", "}", ")"]

def verifica(string):
    l = []
    for i in string:
        if i in openList:
            l.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if (len(l) > 0) and (openList[pos] == l[len(l) - 1]):
                l.pop()
            else:
                return "Parantezele nu se inchid bine"
    if len(l) == 0:
        return "Parantezele se inchid bine"

string=input()
print(verifica(string))