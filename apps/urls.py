from django.urls import path
from .views import contact , news,home

urlpatterns = [
    path('', home, name='home'),
    path('news', news, name='news'),
    path('contact', contact, name='contact'),
]