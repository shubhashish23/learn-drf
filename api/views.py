from django.shortcuts import render
from django.http import Http404, JsonResponse
from employee.models import Employee
from student.models import Student
from api.serializers import EmployeeSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.views import APIView


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
    
class Employees(APIView):
    def get(self , request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK )
    def post(self , request):
        serializer = EmployeeSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status =status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    def get(self , request , pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self , request , pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self , request , pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)