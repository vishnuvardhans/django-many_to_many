# yourapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentCourses.as_view(), name='student_courses'),
]