from django.shortcuts import render
from django.db import models
from .models import Category, Rule, Rule_Change
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import logout as logouts


# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})

def home(request):
    return render(request, "RISAPP/home.html", {})

def make_rule_change(request):
    return render(request, "RISAPP/makerulechange.html", {})

def view_approved_rule_changes(request):
    return render(request, "RISAPP/viewapprovedchanges.html", {})

def view_rule_changes(request):
    rule_change = Rule_Change.objects.all()
    return render(request, "RISAPP/viewrulechanges.html", {'rulechangesdata': rule_change})

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('')





