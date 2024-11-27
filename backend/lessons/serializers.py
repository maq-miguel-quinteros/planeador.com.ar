from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'created_at', 'applicated_at', 'teacher']
        extra_kwargs = {'teacher': {'read_only': True}}