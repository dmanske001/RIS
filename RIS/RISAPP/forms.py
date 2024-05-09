from django.forms import ModelForm
from django import forms
from .models import Rule, Rule_Change, Category
from django.forms import ModelForm

class Make_Rule_Change_Form(ModelForm):
    class Meta:
        model = Rule_Change
        fields = ()

        def Save(self, commit=True):
            
