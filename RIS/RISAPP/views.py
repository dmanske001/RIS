from django.shortcuts import render
from django.db import models
from .models import Category, Rule, Rule_Change
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import logout as logouts
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Make_Rule_Change_Form, Change_Rule_Status_Form, Change_Status_Form, Change_Status_Form_Dev
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.http import JsonResponse
import json



# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})

def home(request):
    return render(request, "RISAPP/home.html", {})

def update_status(request, rule_change_id):
    rule_change = Rule_Change.objects.get(pk=rule_change_id)
    form = Change_Status_Form(request.POST or None, instance=rule_change)
    if form.is_valid():
        form.save()
        return redirect('viewrulechanges')
    return render(request, 'RISAPP/viewrulechange.html', {"rule_change_id" : rule_change, "form": form})

def update_status_dev(request, rule_change_id):
    rule_change = Rule_Change.objects.get(pk=rule_change_id)
    form = Change_Status_Form_Dev(request.POST or None, instance=rule_change)
    if form.is_valid():
        form.save()
        return redirect('viewapprovedrulechanges')
    return render(request, 'RISAPP/viewapprovedrulechange.html', {"rule_change_id" : rule_change, "form": form})

def make_rule_change(request):
    displaycategories = Category.objects.all()
    displayrules = Rule.objects.all()

    form = Make_Rule_Change_Form()

    if request.method == "POST":
        form = Make_Rule_Change_Form(request.POST)
        if form.is_valid():

            form.save()
            return redirect('makerulechangerequest')


    return render(request, "RISAPP/makerulechange.html", {"Category":displaycategories, "Rule":displayrules, "form": form})


def view_approved_rule_changes(request):
    rule_change = Rule_Change.objects.all()
    return render(request, "RISAPP/viewapprovedchanges.html", {'rulechangesdata': rule_change})

def view_rule_changes(request):
    rule_change = Rule_Change.objects.all()
    form = Change_Rule_Status_Form

    if request.method == "POST":
        form = Change_Rule_Status_Form(request.POST)
        if form.is_valid():

            form.save()
    return render(request, "RISAPP/viewrulechanges.html", {'rulechangesdata': rule_change, "form": form})


def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('')

def getRules(request):
    return JsonResponse("It is working", safe=False)








