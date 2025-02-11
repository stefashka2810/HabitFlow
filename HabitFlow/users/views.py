from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class LoginView(TokenObtainPairView):
    """Логин через email и пароль (JWT)"""
    pass
