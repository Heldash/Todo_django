from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,UserRegistration,RenameForm,ChangePhoto
from django.http import HttpRequest,HttpResponse
from todo.models import Task
# Create your views here.
User = get_user_model()
print(User)
def registration(request:HttpRequest):
    if request.method=="POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistration
    return render(request,"signup.html",context={"form":form})
@login_required
def account_view(request:HttpRequest):
    print(request.user.id)
    todo_count= Task.objects.filter(author=request.user).count()
    form_rename= RenameForm
    form_photo = ChangePhoto
    return render(request,"account.html",context={"count_todo":todo_count,
                                                  "form_rename":form_rename,
                                                  "form_photo":form_photo})
@login_required
def change_photo(request:HttpRequest):
    if request.method=="POST":
        form = ChangePhoto(request.POST,request.FILES)
        print(request)
        print(request.FILES)
        if form.is_valid():
            user = request.user
            photo = form.cleaned_data["photo"]
            print(request.FILES)
            user.photo_user=photo
            user.save()
    return redirect("account")
@login_required
def rename_view(request:HttpRequest):
    if request.method == "POST":
        form = RenameForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            user.name = name
            user.save()
    return redirect("account")
def login_view(request:HttpRequest):
    context ={}
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data["username"]
            # password = form.cleaned_data["password"]
            # user = authenticate(request,username=username,password=password)
            user = form.auth(request)
            print(user)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                context["message"]="Неверный логин или пароль"
    form = LoginForm()
    context["form"]=form
    context["message"]=None
    return render(request,"login.html",context=context)
def exit(request:HttpRequest):
    logout(request)
    return redirect("login")
def web_prog_redir(request:HttpRequest):
    return redirect("home")
