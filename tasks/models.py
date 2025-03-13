from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name} | {self.email}'

class Task(models.Model):
    STATUS_CHOICES = [
        ("PENDING",'Pending'),
        ("IN_PROGRESS",'In Progress'),
        ("COMPLETED",'Completed'),
    ]
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    assigned_to = models.ManyToManyField(Employee, related_name="tasks")
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices= STATUS_CHOICES, default="PENDING")
    is_completed = models.BooleanField(default=False)
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
    task = models.OneToOneField(Task, on_delete= models.CASCADE, related_name='details')
    # assigned_to = models.CharField(max_length=100)
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