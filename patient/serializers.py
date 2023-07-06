from rest_framework import serializers
from question.serializers import QuestionAnswerSerializer,CommenetSerializer
from .models import Patient
from question.models import QuestionAnswer,PatientComment


class PatientSerializer(serializers.ModelSerializer):
    patientQuestion = QuestionAnswerSerializer(many=True)
    patientComment = CommenetSerializer(many=True)
    class Meta:
        model = Patient
        fields = ['parentfull_name','full_name', 'dateofbirth','region','facility','height','weight','childAG','weeksborn','premature','patientQuestion','phonenumber','address','patientComment','overallcomment']

    def create(self, validated_data):
        question_data = validated_data.pop('patientQuestion')
        comment = validated_data.pop('patientComment')
        patient = Patient.objects.create(**validated_data)
        for question in question_data:
            QuestionAnswer.objects.create(patient=patient, **question)
        for comm in comment:
            comm['patient'] = patient 
            PatientComment.objects.create(**comm)
        return patient
