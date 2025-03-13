from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project

# Create your views here.


def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")


def test(request):
    names = ["Mahmud", "Ahamed", "John", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names": names,
        "age": 23,
        "count": count
    }
    return render(request, 'test.html', context)


def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm()  # For GET

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():

            """ For Model Form Data """
            form.save()
            return render(request, 'task_form.html', {"form": form, "message": "task added successfully"})

           

    context = {"form": form}
    return render(request, "task_form.html", context)

def view_task(request):

    #Select_related (ForeignKey, OneToOneField)

    #prefetch_related(reverse foreign key manytomany)

    tasks = Project.objects.prefetch_related('task_set').all()

    # tasks = TaskDetail.objects.select_related('details').all()


  


    context = {
        "tasks": tasks,
        
       
        }

    return render(request, 'show_task.html', context)