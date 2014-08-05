from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from snake.form import RegisterForm
from snake.models import *

# Create your views here.


def home(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    return render(request, 'home.html', {'form': form})


def leaderboard(request):
    top_scores = Score.objects.order_by('-score')[:20]
    return render(request, 'leaderboard.html', {'top_scores': top_scores})

@login_required
def snake(request):
    return render(request, 'snake.html')

@login_required
def memory_game(request):
    return render(request, 'memory_game.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@csrf_exempt
def add_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Score.objects.create(score=int(data['score']),
                             player=request.user,
                             game=data['game'])
        return HttpResponseRedirect('/profile/')


@csrf_exempt
def highest_score(request):
    highest_score = max(Score.objects.filter(player=request.user).aggregate(Max('score')), 0)
    data = {'high_score': highest_score['score__max']}
    return HttpResponse(json.dumps(data), content_type='application.json')