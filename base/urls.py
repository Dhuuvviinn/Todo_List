from django.urls import path
from .views import home,sign,login,addTodo,signout,delete_todo,change_status
urlpatterns = [
    path("",home,name="home"),
    path("sign/",sign,name="sign"),
    path("login/",login,name="login"),
    path("add-form/",addTodo,name="addTodo"),
    path("logout/",signout,name="signout"),
    path("delet-todo/<int:id>",delete_todo,name="delete_todo"),
    path("change-status/<int:id>/<str:status>",change_status,name="change_status")
    
]
