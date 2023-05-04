from rest_framework import serializers
from . models import QuestionCategory
from question.serializers import QuestionnaireSerializer

class QuestionCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = QuestionCategory
        fields = '__all__'

class CategoryQuestionSerializer(serializers.ModelSerializer):
    questions = QuestionnaireSerializer(many=True)
    class Meta:
        model = QuestionCategory
        fields = ['id','category','questions']
