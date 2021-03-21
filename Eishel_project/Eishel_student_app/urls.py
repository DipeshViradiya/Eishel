from django.contrib import admin
from django.urls import path, include
from Eishel_student_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("student_login",views.student_login, name="student_login"),
    path("teacher_signup",views.teacher_signup, name="teacher_signup"),
    path("teacher_login",views.teacher_login, name="teacher_login"),
    path("exam_login",views.exam_login, name="exam_login"),
    path("teacher_home",views.teacher_home, name="teacher_home"),
    path("create_exam",views.create_exam, name="create_exam"),

]