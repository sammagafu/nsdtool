from rest_framework import serializers
from . models import QuestionCategory

class QuestionCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = QuestionCategory
        fields = '__all__'
