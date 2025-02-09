"""
URL configuration for todo_social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import user.views as user_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",user_view.web_prog_redir),
    path("registration/",user_view.registration,name="signup"),
    path("login/",user_view.login_view,name="login"),
    path("logout/",user_view.exit,name="logout"),
    path("account/",user_view.account_view,name="account"),
    path("account/photo/",user_view.change_photo,name="photo_add"),
    path("account/rename/",user_view.rename_view,name="rename"),
    path("todo/",include("todo.urls")),
    # path("account/",,name="account_settings")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
