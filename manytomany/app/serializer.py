# serializers.py
from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'
class CourseSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class studentSerializerpost(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['student_name']