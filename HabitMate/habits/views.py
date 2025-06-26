from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import HabitForm
from .models import Habit

# Sign up
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('habit_list')
    else:
        form = UserCreationForm()
    return render(request, 'habits/signup.html', {'form': form})

# Log in
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('habit_list')
        else:
            return render(request, 'habits/login.html', {'error': 'Invalid credentials'})
    return render(request, 'habits/login.html')

# Log out
def logout_view(request):
    logout(request)
    return redirect('login')

# Habit list
@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    done_count = habits.filter(is_done=True).count()
    not_done_count = habits.filter(is_done=False).count()
    return render(request, 'habits/habit_list.html', {
        'habits': habits,
        'done_count': done_count,
        'not_done_count': not_done_count
    })

# Add Habit
@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'habits/add_habit.html', {'form': form})

# Edit Habit
@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit_list')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habits/edit_habit.html', {'form': form})

# Delete Habit
@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.delete()
    return redirect('habit_list')

# Toggle Done
@login_required
def toggle_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.is_done = not habit.is_done
    habit.save()
    return redirect('habit_list')
