# Generated by Django 3.2.5 on 2023-03-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20230309_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='visitdate',
            field=models.DateField(auto_now=True, verbose_name='visit date'),
        ),
    ]
