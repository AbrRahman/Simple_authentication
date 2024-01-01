
from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile,name="profile"),
    path('register/', views.register,name="register"),
    path('login/', views.user_login,name="login"),
    path('logout/', views.user_logout,name="logout"),
    path('passchange/', views.pass_change,name="passchange"),
    path('passchange1/', views.pass_change1,name="passchange1"),
]
