from django.urls import path
from habits import views

app_name = 'habits'

urlpatterns = [
    path('', views.habits, name = 'index'),
    path('habit/', views.habit, name = 'habit'),
]
