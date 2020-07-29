from django.urls import path
from classroom.views import( homepage,teacher_list,teacher_registration )

app_name = 'classrooom'

urlpatterns = [
    path('homepage/', homepage, name = "homepage"),
    path('teacher_list/',teacher_list, name = "teacher_list"),
    path('teacher_register/',teacher_registration,name="teacher_register")
]
