from django.contrib import admin
from teacher.models import Teacher
from django.contrib.auth.admin import UserAdmin

class TeacherAdmin(UserAdmin):
	list_display	=	('email','username','date_joined','is_admin','is_staff')
	search_fields	=	('email','username')
	readonly_fields	=	('date_joined','last_login')

	filter_horizontal	=	()
	list_filter			=	()
	fieldsets			=	()

admin.site.register(Teacher,TeacherAdmin)