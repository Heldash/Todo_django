from django.urls import path
from .views import add_todo,home_view,user_view,comment_view,delete_todo,delete_kom
urlpatterns=[
    path("add_task/",add_todo,name="add_todo"),
    path("home/",home_view,name="home"),
    path("user/",user_view,name="users"),
    path("post/",comment_view,name="comment"),
    path("delete/",delete_todo,name="delete"),
    path("comment/delete/",delete_kom,name="delete_komm")
]

# hx - post = "{% url 'like_url' %}?task={{todo.id}}"
# hx - swap = "none"
