from django import forms
from django.contrib.auth.forms import UserCreationForm

from classroom.models import Teacher

class TeacherRegistrationForm(UserCreationForm):
	email	=	forms.EmailField(max_length=60,help_text="Required. Add a valid Email Address")

	class Meta:
		model	=	Teacher
		fields	=	("email","username","password1","password2")
