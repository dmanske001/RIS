# Generated by Django 4.2.10 on 2024-05-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RISAPP', '0011_alter_rule_change_rule_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule_change',
            name='rule_description',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
    ]
