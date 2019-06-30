from django.shortcuts import render
from django.http import HttpResponse

from .fonction import function
from .fonction import ecrire
from .fonction import lecture
from .fonction import ecrire2




def home(request):
    if request.method == "POST":

        #ici on récupere la page et l'étape
        #par exemple 1ok donc inscription
        #deux remplissage formulaire ect...
        page = request.POST.get('a')
        étape = request.POST.get('liste')


        if page == "yahou":
            page = 'https://fr.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMdlxFFv1CpIEQ0VuhLMZl4pjm_0Ur2KGpLoKBkg4lBqmzqdwLxulK-E29QEXf815EL1VsURfRYB-M3USUSs2fFR6tT63nGaOfQyk5mY4V9AltWx-EzQiluy32sS5KxDY0lQRsL6YmEXNMq4qWdOpBoyt2T6KtkfK9Bce2Dt8ViB'
            page = function(page)
            ecrire(page)


        
            page_affichage = lecture()
            ecrire2(page_affichage)

            return HttpResponse('ok')



    
    return render(request, 'home.html')




def page(request):
    return render(request, 'page.html')
