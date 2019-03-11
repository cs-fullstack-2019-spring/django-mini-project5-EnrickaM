from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path("newuser/",views.newuser,name='newuser'),
    path("login/",views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path("all_recipes/",views.all_recipes,name='all_recipes'),
    path("profile_page/",views.profile_page,name='profile_page'),
]