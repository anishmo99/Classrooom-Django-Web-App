from django.urls import path
from . import views

app_name = 'classrooom'

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('teacher_list',views.teacher_list, name = 'teacher_list')
]