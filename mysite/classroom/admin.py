from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Teacher, Class, Section, Student, Question, Answer, Subject

class QuestionAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField : {'widget' : TinyMCE()}
	}

class AnswerAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField : {'widget' : TinyMCE()}
	}

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Subject)
