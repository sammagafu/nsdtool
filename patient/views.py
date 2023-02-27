from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailsview(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer