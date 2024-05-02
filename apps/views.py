from django.shortcuts import render
from apps.models import Post


def news(request):
    data = {}
    data["dataset"] = Post.objects.all()
    return render(request, "news.html",data)

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"home.html")