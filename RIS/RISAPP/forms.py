from django.forms import ModelForm
from socket import fromshare
from django import forms
from .models import Rule, Rule_Change, Category
from django.forms import ModelForm

class Make_Rule_Change_Form(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = '__all__'
        exclude = ('date_created', 'date_decided', 'rule_status')

    def __init__(self, *args, **kwargs):
        super(Make_Rule_Change_Form, self).__init__(*args, **kwargs)

        self.fields['category'].queryset = self.fields['category'].queryset.order_by('name')


class Change_Status_Form(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = '__all__'
        exclude = ('category', 'date_created', 'rule', 'rule_description', 'date_decided' )


class Change_Status_Form_Dev(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = '__all__'
        exclude = ('category', 'date_created', 'rule', 'rule_description', 'date_decided',)





class Change_Rule_Status_Form(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = ["rule_status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



