from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

STATUSES = (
    ('pending', 'PENDING'),
    ('approved', 'APPROVED'),
    ('declined', 'DECLINED'),
)

class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)

class Rule(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True, null=True)

    class Meta:
        verbose_name = "rule"
        verbose_name_plural = "Rules"

    def __str__(self):
        return str(self.name)

class Rule_Change(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True, null=True)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    date_created = models.DateField(blank=False, auto_now_add=False, default=None, null=True)
    date_decided = models.DateField(blank=True, auto_now_add=False, default=None, null=True)
    rule_description = models.CharField(max_length=200, default=None, null=True)
    rule_status = models.CharField(max_length=8, choices=STATUSES, default='pending', null=True)

    class Meta:
        verbose_name = "rule change"
        verbose_name_plural = "rule changes"



