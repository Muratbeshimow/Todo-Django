from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task
from django.db.models import Q
from .forms import TaskForm, LoginForm


# LOGIN
def login_user(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('task_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# REGISTER
def register(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(
                request, 'Invalid registration details. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# BASE
@login_required(login_url='login')
def base(request):
    return render(request, 'base.html')


# VIEW
@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})


# CREATE
@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})


# UPDATE
@login_required(login_url='login')
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_update.html', {'form': form})


# DELETE
@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})


# SEARCH
def search_view(request):
    search_input = request.GET.get('search-area', '')
    tasks = Task.objects.filter(Q(title__icontains=search_input))
    return render(request, 'search_results.html', {'tasks': tasks, 'search_input': search_input})


# LOGOUT
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
