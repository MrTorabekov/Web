from django import forms
from django.forms import ModelForm
from apps.models import Contact


class InputForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
