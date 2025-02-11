from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

# �������� ������ ��������
class Habit(models.Model):
    
    CATEGORY_CHOICES = [
        ('useful', 'Useful'),
        ('harmful', 'Harmful'),
    ]

    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # �������� � ������������
    name = models.CharField(max_length=150)  # �������� ��������
    description = models.TextField(blank=True, null=True)  # �������� (�����������)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)  # �������� ��� �������
    frequency = models.PositiveIntegerField(help_text="Times per week")  # ������� ����������
    target_date = models.DateField(help_text="Deadline to achieve this habit")  # ���� ����������
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='in_progress')  # �������������� ������

    created_at = models.DateTimeField(auto_now_add=True)  # ���� ��������
    updated_at = models.DateTimeField(auto_now=True)  # ��������� ����������

    def save(self, *args, **kwargs):
        # ������������� ��������� ������
        if self.target_date < date.today():
            self.status = 'completed'
        else:
            self.status = 'in_progress'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

    class Meta:
        unique_together = ('user', 'name')  # ���� ������������ �� ����� ������� ���������� �������� ������
        


