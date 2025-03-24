from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = [
        ("PENDING",'Pending'),
        ("IN_PROGRESS",'In Progress'),
        ("COMPLETED",'Completed'),
    ]
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    # assigned_to = models.ManyToManyField(Employee, related_name="tasks")
    assigned_to = models.ManyToManyField(User, related_name="tasks")
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices= STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class TaskDetail(models.Model):
    HIGH = 'H'
    LOW = 'L'
    MEDIUM = 'M'
    PRIORITY_OPTIONS = (
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    )
    task = models.OneToOneField(Task, on_delete= models.DO_NOTHING, related_name='details')
    asset = models.ImageField(upload_to='tasks_asset', blank=True, null=True, default='tasks_asset/img.jpg')
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS)
    notes = models.TextField(blank= True, null= True)

    def __str__(self):
        return f'{self.task.title} | {self.priority}'

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null= True)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.name} | {self.start_date}"
    


