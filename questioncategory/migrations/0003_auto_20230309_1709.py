# Generated by Django 3.2.5 on 2023-03-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questioncategory', '0002_questioncategory_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questioncategory',
            name='age',
        ),
        migrations.AlterField(
            model_name='questioncategory',
            name='category',
            field=models.CharField(max_length=180, verbose_name='Question Category'),
        ),
    ]
