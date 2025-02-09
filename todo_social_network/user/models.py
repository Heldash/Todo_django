from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# Create your models here.

class MyUser(AbstractUser):
    email=models.EmailField(blank=True)
    photo_user=models.ImageField(upload_to="user_avatars/",blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)



# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = MyUser.objects.get(email=email)
#         except MyUser.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None