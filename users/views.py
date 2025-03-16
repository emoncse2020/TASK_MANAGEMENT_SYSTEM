from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, CustomRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.tokens import default_token_generator

# Create your views here.


def sign_up(request):
    form = CustomRegistrationForm()
    if request.method =="POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            messages.success(request, "A confirmation mail sent. Please check your email")
            return redirect('sign-in')
            



    context = {
        "form": form
    }

    return render (request, 'registration/register.html', context)

def sign_in(request):

    form = LoginForm()
   
    if request.method == "POST":
        
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

            
    return render(request, 'registration/login.html', {"form":form})

def sign_out(request):
    if request.method == "POST":
        logout(request)
        return redirect('sign-in')
    

def activate_user(request, user_id, token):
    user = get_object_or_404(User, id=user_id)
    # user = User.objects.get(id = user_id)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('sign-in')
    
    else:
        return HttpResponse("Invalid Id or Token")
