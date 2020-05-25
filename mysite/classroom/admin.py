from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Teacher, Class, Student, Question, Answer, Subject
from django.contrib.auth.admin import UserAdmin

class QuestionAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField : {'widget' : TinyMCE()}
	}

class AnswerAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField : {'widget' : TinyMCE()}
	}


class TeacherAdmin(UserAdmin):
	list_display	=	('email','username','date_joined','is_admin','is_staff','is_teacher')
	search_fields	=	('email','username')
	readonly_fields	=	('date_joined','last_login')

	filter_horizontal	=	()
	list_filter			=	()
	fieldsets			=	()

class StudentAdmin(UserAdmin):
	list_display	=	('email','username','student_class','date_joined','is_admin','is_student')
	search_fields	=	('email','username')
	readonly_fields	=	('date_joined','last_login')

	filter_horizontal	=	()
	list_filter			=	()
	fieldsets			=	()


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Class)
admin.site.register(Student,StudentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Subject)


