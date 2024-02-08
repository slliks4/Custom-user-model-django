from django.urls import path
from .import views

urlpatterns = [
    path('student_portal/', views.Student_portal, name='student_portal'),
]
