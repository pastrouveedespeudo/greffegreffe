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
        page = request.POST.get('a')
        étape = request.POST.get('b')


        if page == "yahou":
            page = 'https://fr.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMdlxFFv1CpIEQ0VuhLMZl4pjm_0Ur2KGpLoKBkg4lBqmzqdwLxulK-E29QEXf815EL1VsURfRYB-M3USUSs2fFR6tT63nGaOfQyk5mY4V9AltWx-EzQiluy32sS5KxDY0lQRsL6YmEXNMq4qWdOpBoyt2T6KtkfK9Bce2Dt8ViB'
            return HttpResponse('ok')

        if étape:
            page = 'https://login.yahoo.com/?.src=ym&lang=&done=https%3A%2F%2Fmail.yahoo.com%2F%3F.intl%3Dfr%26.lang%3Dfr-FR%26.partner%3Dnone%26.src%3Dfp%26guce_referrer%3DaHR0cDovLzEyNy4wLjAuMTo4MDAwL3BhZ2U%26guce_referrer_sig%3DAQAAANaMkL1WAY3p59RCA2AOJ-PhiKoEDDaSoiKwrHneojN6D12eiM3Bw7wgsZQHW64-tp4a_Xqy4eOhYzHjilm0OeMFxdaGXHyJB0843EPfMLgGfJR-pdPfDeOfzlwaEYJvu3MbN2OeeVM7s7ZHLyXq8SQHtM8WDpKBsNSHSJztdNQd&.partner=none'
            return HttpResponse('ok')



    
    return render(request, 'home.html')




def page(request):
    return render(request, 'inscription/page.html')

def page1(request):
    return render(request, 'inscription/page1.html')
def page2(request):
    return render(request, 'inscription/page2.html')





















