from rest_framework import serializers
from . models import QuestionAnswer,Questionnaire
from questioncategory.serializers import QuestionCategorySerializer

class QuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = '__all__'
        depth = 1


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'

