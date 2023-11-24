from django.shortcuts import render
from cat_game.cat import Cat
from django.http import HttpResponseRedirect


def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        Cat.name = request.POST.get('cat_name')
        return HttpResponseRedirect('/cat_stats')


def cat_stats_view(request):
    if request.method == "GET":
        context = {
            'name': Cat.name,
            'age': Cat.age,
            'satiety': Cat.satiety,
            'happiness': Cat.happiness,
            'avatar': Cat.avatar
        }
        return render(request, 'cat_stats.html', context)
    elif request.method == "POST":
        action = request.POST.get('action')
        if action == 'play':
            Cat.play()
        elif action == 'feed':
            pass
        elif action == 'sleep':
            pass
        return HttpResponseRedirect('/cat_stats')

