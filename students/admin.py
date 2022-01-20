from django.contrib import admin
from . models import Students
# Register your models here.

class StudentsAdmin(admin.ModelAdmin) :
    list_display = ('roll_no', 'fullname', 'course')

admin.site.register(Students, StudentsAdmin)
