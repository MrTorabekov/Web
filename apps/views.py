from django.shortcuts import render



def news(request):
    return render(request, "news.html")

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"home.html")