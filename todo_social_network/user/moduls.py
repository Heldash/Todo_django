from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(UserModel)
        print("Backend:",username,password)
        try:
            user = UserModel.objects.get(email=username)
            print("User:",user)
        except UserModel.DoesNotExist:
            return None
        else:
            print(user.password)
            print(check_password(password,user.password))
            if user.check_password(password):
                return user
        return None