from rest_framework import serializers
from question.serializers import QuestionAnswerSerializer,CommenetSerializer
from .models import Patient
from question.models import QuestionAnswer,PatientComment


class PatientSerializer(serializers.ModelSerializer):
    patientQuestion = QuestionAnswerSerializer(many=True)
    patientComment = CommenetSerializer(many=True)
    class Meta:
        model = Patient
        fields = ['full_name', 'dateofbirth','region','facility','height','weight','patientQuestion','phonenumber','address','patientComment']

    def create(self, validated_data):
        question_data = validated_data.pop('patientQuestion')
        comment = validated_data.pop('commets')
        patient = Patient.objects.create(**validated_data)
        for question in question_data:
            QuestionAnswer.objects.create(patient=patient, **question)
        for comm in comment:
            PatientComment.objects.create(patient=patient, **comm)
        return patient
