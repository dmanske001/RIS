from django.shortcuts import render
from django.db import models
from .models import Category, Rule, Rule_Change


# Create your views here.
def index(request):

    return render(request, "RISAPP/index.html", {})

def home(request):
    return render(request, "RISAPP/home.html", {})

def make_rule_change(request):
    return render(request, "RISAPP/makerulechange.html", {})

def view_approved_rule_changes(request):
    return render(request, "RISAPP/viewapprovedchanges.html", {})

def view_rule_changes(request):
    return render(request, "RISAPP/viewrulechanges.html", {})





