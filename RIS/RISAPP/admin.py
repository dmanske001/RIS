from django.contrib import admin
from .models import Category, Rule, Rule_Change

admin.site.register(Category)
admin.site.register(Rule)
admin.site.register(Rule_Change)

