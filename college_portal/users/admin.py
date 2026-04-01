from django.contrib import admin
from users.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "age")
    
admin.site.register(Student,StudentAdmin)    