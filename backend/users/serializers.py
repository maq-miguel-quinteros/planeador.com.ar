from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    # redefine create function from ModelSerializer
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
