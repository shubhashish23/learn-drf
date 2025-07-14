from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# read and Create  view here.
@api_view(['GET' , 'POST'])
def studentView(request):
    # students = Student.objects.all()
    # return JsonResponse(students , safe=False)
    #student_list = list(students.values()) #manual serializing
    # return JsonResponse(student_list , safe=False)
    # using serializer
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors , status=status.HTTP_401_UNAUTHORIZED)

# read and update view here
@api_view(['GET' , 'PUT' , 'DELETE'])
def studentDetailView(request , pk):
    try:
        student = Student.objects.get(pk =pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET' :
        serializer = StudentSerializer(student)
        return Response(serializer.data , status = status.HTTP_200_OK)
    elif request.method == "PUT" :
        serializer = StudentSerializer(student , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' :
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    