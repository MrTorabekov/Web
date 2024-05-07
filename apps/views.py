from django.shortcuts import render
from apps.models import Post
from apps.forms import InputForm


def contact(request):
    if (request.method == 'POST'):
        forms = InputForm(request.POST)
        if (forms.is_valid()):
            # first_name = forms.cleaned_data['first_name']
            # last_name = forms.cleaned_data['last_name']
            # country = forms.cleaned_data['country']
            # subject = forms.cleaned_data['subject']
            # student = Contact.objects.create(first_name=first_name, last_name=last_name, country=country,
            #                                  subject=subject)
            # student.save()
            forms.save()

    contact_form = InputForm()
    return render(request, "contact.html", {"form": contact_form})


def news(request):
    data = {}
    data['dataset'] = Post.objects.all()
    return render(request, "news.html",data)


def home(request):
    return render(request, "home.html")
