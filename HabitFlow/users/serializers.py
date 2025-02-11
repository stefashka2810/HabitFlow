from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Подтверждение пароля

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'gender', 'age', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Убираем поле подтверждения пароля
        user = User.objects.create_user(**validated_data)
        return user
