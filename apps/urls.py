from django.urls import path
from apps.views import news,contact,home

urlpatterns = [
    path('', home, name='about'),
    path('news', news, name='about'),
    path('contact', contact, name='contact'),
]