from django.contrib import admin
from main.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['rollno','name','email','password']


