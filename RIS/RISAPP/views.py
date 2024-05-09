from django.shortcuts import render
from django.db import models
from .models import Category, Rule, Rule_Change
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import logout as logouts
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Make_Rule_Change_Form
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})

def home(request):
    return render(request, "RISAPP/home.html", {})

def make_rule_change(request):
    displaycategories = Category.objects.all()
    displayrules = Rule.objects.all()

    return render(request, "RISAPP/makerulechange.html", {"Category":displaycategories, "Rule":displayrules})


def view_approved_rule_changes(request):
    rule_change = Rule_Change.objects.all()
    return render(request, "RISAPP/viewapprovedchanges.html", {'rulechangesdata': rule_change})

def view_rule_changes(request):
    rule_change = Rule_Change.objects.all()
    return render(request, "RISAPP/viewrulechanges.html", {'rulechangesdata': rule_change})

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('')








