def le_type(liste_find, liste):

    
    type_de_i = ''

    BOUTON = ['#', '}', '{']

    
    liste1 = []
    liste2 = []

    
    for i in liste_find:
        liste1.append(liste[0][i-1000:i+100])

    c = 0
    for i in liste1:
        for j in i:
            for k in BOUTON:
                if j == k:
                    c += 1
                    
        liste2.append([int(c), i])


        

    liste3 = []

    c = 0
    for i in liste2:
        if liste2[c][0] > 5:
            liste3.append(liste2[c][1])


        c+=1

    liste3 = local_bouton(liste3)
    
    return liste3


def local_bouton(liste3):

    MAIL = ['mail', 'Mail']

    mot = ''

    liste = []
    
    for i in liste3:
        
        for j in i:
        
            if j == '.' or j == ' ':
                mot += j
                liste.append(mot)
                mot = ''
                
                
            else:
                mot += j
            

    for i in liste:
         print(i)

































































