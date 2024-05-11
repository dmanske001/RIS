from django.forms import ModelForm
from socket import fromshare
from django import forms
from .models import Rule, Rule_Change, Category
from django.forms import ModelForm

class Make_Rule_Change_Form(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = '__all__'
        exclude = ('date_created', 'date_decided', 'rule_status', 'user')

    def __init__(self, *args, **kwargs):
        super(Make_Rule_Change_Form, self).__init__(*args, **kwargs)
        self.fields['rule'].queryset = Rule.objects.none()
        self.fields['category'].queryset = self.fields['category'].queryset.order_by('name')

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['rule'].queryset = Rule.objects.filter(category_id=category_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['rule'].queryset = self.instance.category.rule.order_by('name')
        self.fields['rule'].queryset = self.fields['rule'].queryset.order_by('name')

class Change_Status_Form(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = '__all__'
        exclude = ('category', 'date_created', 'rule', 'rule_description', 'date_decided', 'user' )


class Change_Status_Form_Dev(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = '__all__'
        exclude = ('category', 'date_created', 'rule', 'rule_description', 'date_decided', 'user')





class Change_Rule_Status_Form(forms.ModelForm):
    class Meta:
        model = Rule_Change
        fields = ["rule_status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



