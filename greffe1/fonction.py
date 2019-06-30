import requests
from bs4 import *
from fonction_fonction import found


def function(path):

    request_html = requests.get(path)
    page = request_html.content

    var_soup = BeautifulSoup(page, "html.parser")

    page = found(page)
    
    return page




PATH = r'C:\Users\jeanbaptiste\Desktop\greffe\env\greffe\greffe\requete.py'
def ecrire(page):
    
    fichier = open(PATH, "w")
    fichier.write(str(page))
    fichier.close()

def lecture():
    fichier = open(PATH, "r")
    fichier = fichier.read()
    return str(fichier)

PATH1 = r'C:\Users\jeanbaptiste\Desktop\greffe\env\greffe\templates\page.html'
def ecrire2(page):
    
    fichier = open(PATH1, "w")
    fichier.write(str(page))
    fichier.close()
