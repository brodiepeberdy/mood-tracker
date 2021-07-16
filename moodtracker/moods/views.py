from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db import IntegrityError



# Create your views here.
def new_view(request):
    return render(request, 'moods/new_mood.html')

@login_required(login_url="/accounts/login/")
def new_view(request):
    if request.method == 'POST':
        form = forms.NewMood(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user

            try:
                instance.save()
                return redirect('/')
            except IntegrityError:
                return redirect('/')
    else:
        form = forms.NewMood()
    return render(request, 'moods/new_mood.html', {'form':form})

@login_required(login_url="/accounts/login/")
def today_view(request):
    if request.method == 'POST':
        form = forms.TodayMood(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user

            try:
                instance.save()
                return redirect('/')
            except IntegrityError:
                return redirect('/')
    else:
        form = forms.TodayMood()
    return render(request, 'moods/new_today.html', {'form':form})
