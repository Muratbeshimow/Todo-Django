from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.task_list, name='task_list'),
    path('create/task', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    path('search/', views.search_view, name='search'),
]
