from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    """Менеджер для создания пользователей и суперпользователей"""

    def create_user(self, email, first_name, last_name, gender, age, password=None):
        if not email:
            raise ValueError("Email is required")
        if not first_name or not last_name:
            raise ValueError("First name and last name are required")
        if not gender:
            raise ValueError("Gender is required")
        if not age:
            raise ValueError("Age is required")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, gender=gender, age=age)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, gender, age, password):
        user = self.create_user(email, first_name, last_name, gender, age, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Кастомная модель пользователя"""

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    email = models.EmailField(unique=True)  # Логин по email
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Для доступа в админку

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Вход по email
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'age']  # Обязательные поля

    def __str__(self):
        return self.email
