from django.contrib import admin

# Register your models here.
from .models import Student,Organization

admin.site.register(Student)
admin.site.register(Organization)
