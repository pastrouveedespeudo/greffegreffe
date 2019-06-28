import requests
from bs4 import *

def function(path):

    request_html = requests.get(path)
    page = request_html.content

    var_soup = BeautifulSoup(page, "html.parser")

    
