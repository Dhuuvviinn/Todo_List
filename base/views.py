from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .form import todoForm
from .models import TODO
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def home(request):
     if request.user.is_authenticated:
        user= request.user
        form = todoForm()
        todos= TODO.objects.filter(user=user)
        return render(request,"index.html",{"form":form,"todos":todos})

def sign(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request,"sign.html",{"form":form})
    else:
        form = UserCreationForm(request.POST)
        print(form,"form")
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = UserCreationForm()
            print(form.error_messages)
            return render(request,"sign.html",{"form":form,"error":"error"})
def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request,"login.html",{"form":form})
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
           username = form.cleaned_data.get("username")
           password = form.cleaned_data.get("password")
           user = authenticate(username=username,password=password) 
           if user is not None:
               loginUser(request,user)
               return redirect("home")

        else:
            form = UserCreationForm()
            return render(request,"login.html",{"form":form})

def addTodo(request):
    form = todoForm(request.POST)
    if request.user.is_authenticated:
        user= request.user
        print(user)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request,"index.html",{"form":form})
        


def signout(request):
    logout(request)
    return redirect("login")

def delete_todo(request,id):
    print(id)
    TODO.objects.get(pk=id).delete()
    return redirect("home")
def change_status(request,id,status):
    todos = TODO.objects.get(pk=id)
    todos.status = status
    todos.save()
    return redirect("home")