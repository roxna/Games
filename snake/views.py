from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from snake.form import RegisterForm

# Create your views here.


def home(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    return render(request, 'home.html', {'form': form})


def snake(request):
    return render(request, 'snake.html')


def memory_game(request):
    return render(request, 'memory_game.html')


@login_required
def profile(request):
    return render(request, 'profile.html')