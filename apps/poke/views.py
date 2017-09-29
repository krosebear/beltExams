from django.shortcuts import render, redirect
from ..main.models import User
from models import Poke
from django.db.models import Count
def index(request):
    x = Poke.objects.filter(receive=request.session['user_id']).values('give').distinct()
    context = {
        'user': User.objects.get(id = request.session['user_id']),
        'otherusers': User.objects.exclude(id = request.session['user_id']),
        'pokedUsers': Poke.objects.filter(receive__id=request.session['user_id']).values('give').annotate(count =Count('give')),
    }
    d = context['pokedUsers']
    for key, value in d:
        print key, value

    return render(request, 'poke/index.html', context)
def addPoke(request, user_id):
    Poke.objects.create(receive = User.objects.get(id=user_id), give = User.objects.get(id=request.session['user_id']))
    return redirect ('/pokes')
