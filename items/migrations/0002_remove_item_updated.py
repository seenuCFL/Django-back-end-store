# Generated by Django 3.0.6 on 2020-10-22 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='updated',
        ),
    ]