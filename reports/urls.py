from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('student_home/', views.student_home, name='student_home'),
    path('student.html', views.student_view, name='student'),


]
