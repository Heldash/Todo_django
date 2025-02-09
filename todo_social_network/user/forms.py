from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from .models import MyUser
# User = get_user_model()
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email",widget=forms.EmailInput)
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    def auth(self,request:HttpRequest):
        mail = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        print(mail,password)
        user = authenticate(request,username=mail,password=password)
        return user
class UserRegistration(forms.Form):
    username=forms.CharField(label="Логин",min_length=5,max_length=150)
    name = forms.CharField(label="Отображаемое имя",min_length=2,max_length=150)
    email = forms.EmailField(label="Почта",widget=forms.EmailInput)
    password1 =forms.CharField(label="Пароль",widget=forms.PasswordInput)
    password2 =forms.CharField(label="Повторите пароль",widget=forms.PasswordInput)
    field_order = ["username","name","email","password1","password2"]

    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        new = MyUser.objects.filter(username=username)
        if new.count():
            raise ValidationError("Username already exist")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        new = MyUser.objects.filter(email=email)
        if new.count():
            raise ValidationError("email already exist")
        return email

    def clean_password(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password2!=password1:
            raise ValidationError("password don`t match")
        return password1

    def save(self):
        # print(self.cleaned_data["username"],self.cleaned_data["email"],self.cleaned_data["password1"])
        user = MyUser.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password1"],
            name=self.cleaned_data["name"])
        return user


class RenameForm(forms.Form):
    name = forms.CharField(label="Переименовать",min_length=1,max_length=150)
    def save(self,request:HttpRequest):
        user = request.user
        if self.is_valid():
            user.name=self.name
            user.save()
class ChangePhoto(forms.Form):
    photo = forms.ImageField()
