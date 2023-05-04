from rest_framework import generics
from .models import QuestionCategory
from .serializers import CategoryQuestionSerializer

# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

class QuestionnairetList(generics.ListCreateAPIView):
    queryset = QuestionCategory.objects.all()
    serializer_class = CategoryQuestionSerializer