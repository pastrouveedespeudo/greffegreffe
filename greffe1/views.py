from django.shortcuts import render
from django.http import HttpResponse

##from .fonction import function
##from .fonction import ecrire
##from .fonction import lecture
##from .fonction import ecrire2




def home(request):
    if request.method == "POST":

        #ici on récupere la page et l'étape
        #par exemple 1ok donc inscription
        #deux remplissage formulaire ect...
        page = request.POST.get('adresse')
        type_requete = request.POST.get('type')

        print(type_requete)
        
        if page == "yahou" and type_requete == 'inscription':
            page = 'https://fr.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMdlxFFv1CpIEQ0VuhLMZl4pjm_0Ur2KGpLoKBkg4lBqmzqdwLxulK-E29QEXf815EL1VsURfRYB-M3USUSs2fFR6tT63nGaOfQyk5mY4V9AltWx-EzQiluy32sS5KxDY0lQRsL6YmEXNMq4qWdOpBoyt2T6KtkfK9Bce2Dt8ViB'
            return HttpResponse('ok_inscription')

        if page == "yahou" and type_requete == 'connection':
            print('wouzaaaaaaaaaa')
            return HttpResponse('ok_connection')


    
    return render(request, 'home.html')


















#Section yahou inscription
def page(request):
    return render(request, 'inscription/yahou/page.html')
def page1(request):
    return render(request, 'inscription/yahou/page1.html')
def page2(request):
    return render(request, 'inscription/yahou/page2.html')





#section yahou connection
def page3(request):
    return render(request, 'connection/yahou/page3.html')
















