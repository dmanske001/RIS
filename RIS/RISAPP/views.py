from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "RISAPP/index.html", {})

def home(request):
    return render(request, "RISAPP/home.html", {})

def make_rule_change(request):
    return render(request, "RISAPP/makerulechange.html", {})

