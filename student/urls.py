
from django.urls import path
from student.views import student

app_name="student"
urlpatterns = [
    path("" , student , name="student"),
]