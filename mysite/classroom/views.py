from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate


from classroom.forms import TeacherRegistrationForm
from classroom.models import Teacher

def teacher_list(request):
	return render(request = request, template_name = 'classroom/teacher_list.html', context = {"teachers" : Teacher.objects.all()}) 

def homepage(request):	
	message="Welcome to <strong>Classroom Web Application</strong>"
	message=message+"<p><a href='teacher_list'>Teacher List</a>"
	message=message+"<p><a href='teacher_register'>Teacher Register</a>"
	return HttpResponse(message)

def teacher_registration(request):
	context={}
	if request.POST:
		form=TeacherRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email=form.cleaned_data.get('email')
			raw_password=form.cleaned_data.get('password1')
			account=authenticate(email=email,password=raw_password)
			login(request,account)
			return redirect("homepage")
		else:
			context['teacher_registration_form']=form
	else:
		form=TeacherRegistrationForm()
		context['teacher_registration_form']=form
	return render(request,'classroom/teacher_register.html',context)
