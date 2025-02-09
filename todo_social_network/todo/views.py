from django.shortcuts import render,redirect
from .models import Task,Comment
from django.contrib.auth import get_user_model
from django.http import HttpRequest,HttpResponse
from .forms import AddTodoForm, AddCommentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
User = get_user_model()
@login_required
def home_view(request:HttpRequest):
    user= request.user
    todo_list = Task.objects.filter(author = user)
    return render(request,"home_todo.html",context={"todo_list":todo_list})
def add_todo(request:HttpRequest):
    if request.method=="POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            author = request.user
            text = form.cleaned_data["text"]
            deadline = form.cleaned_data["deadline"]
            task = Task(author=author,text=text,deadline=deadline)
            task.save()
            return redirect("home")
    else:
        form = AddTodoForm()
    return render(request,"add_todo.html",context={"form":form})

def delete_kom(request:HttpRequest):
    print(request.META.get('HTTP_REFERER', '/'))
    if request.method=="POST":
        id = int(request.POST.get("id",-1))
        print("id: ",id)
        if id>-1:
            try:
                com = Comment.objects.get(id=id)
                com.delete()
            except ObjectDoesNotExist as ex:
                print(ex)
                HttpResponse("SUCKS")


    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_todo(request:HttpRequest):
    if request.method=="POST":
        id = int(request.POST.get("id",-1))
        user = request.user
        try:
            task = Task.objects.get(id=id)
            print(type(task))
        except Exception as ex:
            print(ex)
            return redirect("home")
        if user == task.author:
            task.delete()
        return redirect("home")
    else:
        return redirect("home")
def user_view(request:HttpRequest):
    id = request.GET.get("id",-1)
    if int(id) <=-1:
        users = User.objects.all()
        return render(request,"list_users.html",context={"users":users})
    else:
        try:
            user_data = User.objects.get(id=id)
            context = {"user_data":user_data.username}
            todo_list = Task.objects.filter(author = user_data)
            context["todo_list"] = todo_list
            return render(request,"home_todo.html",context)
        except Exception as ex:
            print(ex)
            return HttpResponse("404 такого пользователя не существует")

def comment_view(request:HttpRequest):
    context = {}
    id = int(request.GET.get("id", -1))
    if id <=-1:
        return HttpResponse("404 pizda")
    else:
        try:
            task = Task.objects.get(id=id)
        except Exception as ex:
            print(ex)
            return HttpResponse("404 pizda")
    if request.method=="POST":
        form = AddCommentForm(request.POST)
        print(request.POST)
        if form.is_valid() and id >-1:
            text = form.cleaned_data["text"]
            author = request.user
            task = Task.objects.get(id=id)
            Comment(author=author,text=text,task=task).save()
            return redirect(str(request.path)+f"?id={id}")
        else:
            return HttpResponse("404 pizda")
    else:
        form = AddCommentForm()
    context["form"]=form
    context["todo"]=task
    context["comments"]=Comment.objects.filter(task=task).order_by("date_create")
    return render(request,"post_task.html",context=context)