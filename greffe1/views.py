from django.shortcuts import render
from django.http import HttpResponse

from .fonction import function
from .fonction import ecrire
from .fonction import lecture
from .fonction import ecrire2




def home(request):
    if request.method == "POST":
        page = request.POST.get('a')

        page = function(page)
        ecrire(page)


    
        page_affichage = lecture()
        ecrire2(page_affichage)
        print(page_affichage)

        return HttpResponse('ok')



    
    return render(request, 'home.html')




def page(request):
    return render(request, 'page.html')
