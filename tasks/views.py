from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import  TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from django.db.models import Q, Count
from django.contrib import messages

# Create your views here.


def manager_dashboard(request):
    
    

    #getting task count

    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status = "COMPLETED").count()
    # pending_task = Task.objects.filter(status = "PENDING").count()
    # in_progress = Task.objects.filter( status = "IN_PROGRESS").count()
    # type = request.GET.get('type', 'all')
    # print(type)

    counts = Task.objects.aggregate(
        total = Count('pk'),
        completed = Count('pk', filter=Q(status='COMPLETED')),
        pending = Count('pk', filter=Q(status ="PENDING")),
        in_progress = Count('pk', filter=Q(status ="IN_PROGRESS"))
        )
    
    #Retriving task data

    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
    type = request.GET.get('type', 'all')

    if type == 'completed':
        tasks = base_query.filter(status = 'COMPLETED')
    
    elif type == 'in-progress':
        tasks = base_query.filter(status = 'IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status = 'PENDING')
    elif type == 'all':
        tasks = base_query.all()
    

    context = {
        "tasks":tasks,
        "counts": counts
    }


    return render(request, "dashboard/manager-dashboard.html", context)

#CRUD:


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
    task_form = TaskModelForm() 
     # For GET
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)

    if task_form.is_valid() and task_detail_form.is_valid():
        task = task_form.save()
        task_detail = task_detail_form.save(commit=False)
        task_detail.task = task
        task_detail.save()

        messages.success(request, "task created successfully")

        return redirect('create-task')

           

    context = {
        "task_form": task_form,
        "task_detail_form": task_detail_form
        }
    return render(request, "task_form.html", context)
def update_task(request, pk):
    # employees = Employee.objects.all()
    task = Task.objects.get(pk=pk)
    task_form = TaskModelForm(instance = task) 
     # For GET
    if task.details:
        task_detail_form = TaskDetailModelForm(instance = task.details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance = task)
        task_detail_form = TaskDetailModelForm(request.POST, instance = task.details)

    if task_form.is_valid() and task_detail_form.is_valid():
        task = task_form.save()
        task_detail = task_detail_form.save(commit=False)
        task_detail.task = task
        task_detail.save()

        messages.success(request, "task updated successfully")

        return redirect('update-task', pk)

           

    context = {
        "task_form": task_form,
        "task_detail_form": task_detail_form
        }
    return render(request, "task_form.html", context)

def delete_task(request, pk):

    if request.method =="POST":
        task = Task.objects.get(pk = pk)
        task.delete()
        messages.success(request, 'Task Deleted successfully')

        return redirect('manager-dashboard')
    
    


    

def view_task(request):

    #Select_related (ForeignKey, OneToOneField)

    #prefetch_related(reverse foreign key manytomany)

    tasks = Project.objects.prefetch_related('task_set').all()

    # tasks = TaskDetail.objects.select_related('details').all()

    context = {
        "tasks": tasks,
        
       
        }

    return render(request, 'show_task.html', context)


