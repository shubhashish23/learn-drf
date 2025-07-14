from django.urls import path
from api.views import studentView , studentDetailView

app_name="api"
urlpatterns = [
  path("students/" , studentView , name="studentView"),
  path("students/<int:pk>" , studentDetailView , name="studentDetailView"),
]
