# Generated by Django 3.2.5 on 2023-07-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questioncategory', '0003_auto_20230309_1709'),
        ('question', '0008_patientcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='questioncategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questioncategory.questioncategory'),
        ),
    ]
