from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('alterar-senha/', views.user_change_password, name='user_change_password'),
]