from django.urls import path
from api.views import studentView , studentDetailView , Employees , EmployeeDetail

app_name="api"
urlpatterns = [
  path("students/" , studentView , name="studentView"),
  path("students/<int:pk>" , studentDetailView , name="studentDetailView"),

  path("employees/" , Employees.as_view() , name="Employees"),
  path("employeesdetail/<int:pk>" , EmployeeDetail.as_view() , name="EmployeeDetail")
  
]
