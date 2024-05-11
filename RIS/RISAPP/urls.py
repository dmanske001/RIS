"""
URL configuration for RIS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('makerulechangerequest/', views.make_rule_change, name='makerulechangerequest'),
    path('viewapprovedchanges/', views.view_approved_rule_changes, name='viewapprovedrulechanges'),
    path('viewrulechanges/', views.view_rule_changes, name='viewrulechanges'),
    path('logout/', views.logout, name='logout'),
    path('viewrulechange/<rule_change_id>/', views.update_status, name='viewrulechange'),
    path('viewapprovedrulechange/<rule_change_id>/', views.update_status_dev, name='viewapprovedrulechange'),
    path('rules', views.getRules, name = "rules")
]
