from django.shortcuts import render

def home(request):
    if request.method == "POST":
        page = request.POST.get('a')

        print(page,'000000000000000000000,')










    
    return render(request, 'home.html')
