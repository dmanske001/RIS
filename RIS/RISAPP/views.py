from django.shortcuts import render
<<<<<<< Updated upstream

# Create your views here.
def index(request):
    return render(request, "RISAPP/index.html", {})
=======
from django.db import models
from .models import Category, Rule, Rule_Change
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect


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
    return render(request, "RISAPP/viewrulechanges.html", {})





>>>>>>> Stashed changes
