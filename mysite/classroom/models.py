from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(AbstractBaseUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)

# class Teacher(models.Model):
#     teacher_name = models.CharField(max_length=200)


#     def __str__(self):
#     	return self.teacher_name


class TeacherManager(BaseUserManager):
	def create_user(self,email,username,password=None):
		if not email:
			raise ValueError("Email required")

		if not username:
			raise ValueError("Username required")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			)

		user.set_password(password)
		user.save(using=self._db)
		return user


class Teacher(AbstractBaseUser):
	email 			=	models.EmailField(verbose_name="email",max_length=60,unique=True)
	username		=	models.CharField(max_length=30,unique=True)
	date_joined		=	models.DateTimeField(verbose_name="date joined",auto_now_add=True)
	last_login 		=	models.DateTimeField(verbose_name="last login",auto_now=True)
	is_admin		=	models.BooleanField(default=False)
	is_active		=	models.BooleanField(default=True)
	is_staff		=	models.BooleanField(default=False)
	is_superuser	=	models.BooleanField(default=False)
	is_teacher		=	models.BooleanField(default=True)

	USERNAME_FIELD	=	'email'
	REQUIRED_FIELDS =	['username',]

	objects = TeacherManager()

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return self.is_admin

	def has_module_perms(self,applabel):
		return True



class Class(models.Model):
	classNum = models.CharField(max_length=2)
	section = models.CharField(max_length=2)

	class Meta:
		verbose_name_plural = 'Classes'

	def __str__(self):
		return '{0} {1}'.format(self.classNum,self.section)


class Subject(models.Model):
	subject = models.CharField(max_length=100)

	def __str__(self):
		return self.subject

class Question(models.Model):
	question = models.TextField()
	subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
	question_for_class = models.ForeignKey(Class,on_delete=models.CASCADE,default='')
	# question_for_section = models.ForeignKey(Section,on_delete=models.CASCADE,default='')
	question_by_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,default='')
	question_published = models.DateTimeField('date published',default=timezone.now())

	def __str__(self):
		return self.question
	
class Answer(models.Model):
	answer = models.TextField()
	answer_for_question = models.ForeignKey(Question,on_delete=models.CASCADE,default='')
	answer_published = models.DateTimeField('date published',default=timezone.now())

	def __str__(self):
		return self.answer


class StudentManager(BaseUserManager):
	def create_user(self,email,username,password=None):
		if not email:
			raise ValueError("Email required")

		if not username:
			raise ValueError("Username required")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			)

		user.set_password(password)
		user.save(using=self._db)
		return user


class Student(AbstractBaseUser):
	email 			=	models.EmailField(verbose_name="email",max_length=60,unique=True)
	username		=	models.CharField(max_length=30,unique=True)
	student_class	=	models.ForeignKey(Class,on_delete=models.CASCADE)
	date_joined		=	models.DateTimeField(verbose_name="date joined",auto_now_add=True)
	last_login 		=	models.DateTimeField(verbose_name="last login",auto_now=True)
	is_admin		=	models.BooleanField(default=False)
	is_active		=	models.BooleanField(default=True)
	is_staff		=	models.BooleanField(default=False)
	is_superuser	=	models.BooleanField(default=False)
	is_student		=	models.BooleanField(default=True)

	USERNAME_FIELD	=	'email'
	REQUIRED_FIELDS =	['username',]

	objects = StudentManager()

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return self.is_admin

	def has_module_perms(self,applabel):
		return True


# class Student(models.Model):
# 	student_name = models.CharField(max_length=200)
# 	# student_section = models.ForeignKey(Section,on_delete=models.CASCADE) 
# 	student_class = models.ForeignKey(Class,on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.student_name
