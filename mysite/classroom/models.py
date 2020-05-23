from django.utils import timezone
from django.db import models

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)

    def __str__(self):
    	return self.teacher_name



class Class(models.Model):
	classNum = models.CharField(max_length=2)
	section = models.CharField(max_length=2)

	class Meta:
		verbose_name_plural = 'Classes'

	def __str__(self):
		return '{0} {1}'.format(self.classNum,self.section)


'''
class Section(models.Model):
	student_section = models.CharField(max_length=1)
	student_class = models.ForeignKey(Class,on_delete=models.CASCADE,default='')

	def __str__(self):
		return self.student_section
'''

class Subject(models.Model):
	subject = models.CharField(max_length=100)

	def __str__(self):
		return self.subject

class Question(models.Model):
	question = models.TextField()
	subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
	question_for_class = models.ForeignKey(Class,on_delete=models.CASCADE,default='')
	#question_for_section = models.ForeignKey(Section,on_delete=models.CASCADE,default='')
	#question_by_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,default='')
	question_published = models.DateTimeField('date published',default=timezone.now())

	def __str__(self):
		return self.question
	
class Answer(models.Model):
	answer = models.TextField()
	answer_for_question = models.ForeignKey(Question,on_delete=models.CASCADE,default='')
	answer_published = models.DateTimeField('date published',default=timezone.now())

	def __str__(self):
		return self.answer

class Student(models.Model):
	student_name = models.CharField(max_length=200)
	#student_section = models.ForeignKey(Section,on_delete=models.CASCADE) 
	student_class = models.ForeignKey(Class,on_delete=models.CASCADE)

	def __str__(self):
		return self.student_name
