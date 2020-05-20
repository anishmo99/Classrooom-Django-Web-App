from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher

def teacher_list(request):
	return render(request = request, template_name = 'classroom/teacher_list.html', context = {"teachers" : Teacher.objects.all()}) 

def homepage(request):	
    return HttpResponse('Welcome to <strong>Classroom Web Application</strong>')
