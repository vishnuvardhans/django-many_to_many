# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializer import *

class StudentCourses(APIView):
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        Students=request.data.get("student_name")
        course= request.data.get("courses")
        print("course",course)
        print("Students",Students)
        # print("request data",request.data)
        serializer = CourseSerializerPost(data=course,many=True)
        if serializer.is_valid():
            print("jnfdsndjnfngad fnjbsdfsdbc")
            course_instance=serializer.save()
            print(serializer.data)
            # students_data = [{"student_name": name} for name in Students]
            # studentserilizing = studentSerializerpost(data=students_data, many=True)
            studentserilizing=studentSerializerpost(data={"student_name":Students})
            print("studentserilizing",studentserilizing)
            if studentserilizing.is_valid():
                student_instance = studentserilizing.save()
                student_instance.courses.set(course_instance)
                student_instance.save()
             # print("student_instance",course_instance)
            # instance_id = student_instance.id
            # Students["studentid"] = instance_id
            # print(Students)
            # for course in course:
            #     print()
            #     print("subjectsubjectsubjectsubjectsubjectsubject",course)
                response_data = {
                'student name': studentserilizing.data,
                'marks and subjects': serializer.data,
            }
                print("valid")
                return Response(response_data)
            else:
                print("innvalid")
                return Response(serializer.errors)
        else:
            print("invalid")
            return Response(serializer.errors)