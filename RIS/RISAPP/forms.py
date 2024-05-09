from django.forms import ModelForm
from socket import fromshare
from django import forms
from .models import Rule, Rule_Change, Category
from django.forms import ModelForm

class Make_Rule_Change_Form(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = ["category", "rule", "rule_description"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['rule'].queryset = Rule.objects.none()
