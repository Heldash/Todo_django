# Generated by Django 5.1.5 on 2025-02-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_create',
            field=models.DateField(auto_now=True),
        ),
    ]
