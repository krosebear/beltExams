# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    request.session['name'] = result.alias
    messages.success(request, "Successfully registered!")
    return redirect('/pokes')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/pokes')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
