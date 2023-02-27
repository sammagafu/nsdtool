from rest_framework import generics
from .models import Questionnaire
from .serializers import QuestionnaireSerializer

# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

class QuestionnairetList(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionnaireDetailsview(generics.RetrieveUpdateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer