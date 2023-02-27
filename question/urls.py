from django.urls import path
from . import views

urlpatterns = [
    path('',views.QuestionnairetList.as_view()),
    path('<int:pk>',views.QuestionnaireDetailsview.as_view())
]