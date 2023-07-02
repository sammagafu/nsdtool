# Generated by Django 3.2.5 on 2023-07-02 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20230314_1601'),
        ('questioncategory', '0003_auto_20230309_1709'),
        ('question', '0007_alter_questionnaire_whattodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commentCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentCategory', to='questioncategory.questioncategory')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patientComment', to='patient.patient')),
            ],
        ),
    ]
