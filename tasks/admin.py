from django.contrib import admin
from .views import Task, TaskDetail, Employee, Project

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(Employee)
admin.site.register(Project)
