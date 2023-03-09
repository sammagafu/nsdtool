from django.contrib import admin
from .models import QuestionAnswer,Questionnaire

admin.site.register(Questionnaire)
admin.site.register(QuestionAnswer)
# Register your models here.
