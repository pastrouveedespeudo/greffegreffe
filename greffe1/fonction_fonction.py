from fonction_fonction_fonction import le_type


MAIL = ['mail', 'Mail']

def found(page):
    liste = []
    liste.append(str(page))

    liste_find = []

    for i in MAIL:
        a = str(liste).find(i)
        if a >= 0:
            liste_find.append(a)




    liste = le_type(liste_find, liste)

    
    return liste



    






































