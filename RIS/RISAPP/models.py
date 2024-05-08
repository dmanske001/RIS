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
    date_created = models.DateField
    date_decided = models.DateField
    rule_status = models.CharField(max_length=8, choices=STATUSES, default='pending')

    class Meta:
        verbose_name = "rule change"
        verbose_name_plural = "rule changes"



