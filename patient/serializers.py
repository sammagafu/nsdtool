from rest_framework import serializers
from question.serializers import QuestionAnswerSerializer
from .models import Patient
from question.models import QuestionAnswer


class PatientSerializer(serializers.ModelSerializer):
    patientQuestion = QuestionAnswerSerializer(many=True,read_only=False)
    class Meta:
        model = Patient
        fields = ['full_name', 'dateofbirth','region','facility','height','weight','patientQuestion']

    def create(self, validated_data):
        question_data = validated_data.pop('patientQuestion')
        patient = Patient.objects.create(**validated_data)
        for question in question_data:
            QuestionAnswer.objects.create(patient=patient, **question)
        return patient
