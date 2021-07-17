from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import redirect
from django.contrib.auth.models import User
from accounts.models import UserProfile
from . import models
from django.db import IntegrityError
from datetime import date
import requests

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


@login_required(login_url="/accounts/login/")
def delete_view(request, id):
    instance = models.Mood.objects.get(id=id)
    instance.delete()
    profile = UserProfile.objects.get(user=request.user)
    # Order moods by date in descending order, hence the most recent is first.
    moods = models.Mood.objects.all().filter(creator=request.user).order_by('-date')
    response = requests.get("https://zenquotes.io/api/random")
    return render(request, 'accounts/manage.html', {"quote": profile.quote, "location": profile.location, 'moods':moods, "quote": response.json()[0]})

@login_required(login_url="/accounts/login/")
def edit_view(request, id):
    instance = models.Mood.objects.get(id=id)
    if request.method == 'POST':
        form = forms.EditMood(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            profile = UserProfile.objects.get(user=request.user)
            # Order moods by date in descending order, hence the most recent is first.
            moods = models.Mood.objects.all().filter(creator=request.user).order_by('-date')
            response = requests.get("https://zenquotes.io/api/random")
            return render(request, 'accounts/manage.html', {"quote": profile.quote, "location": profile.location, 'moods':moods, "quote": response.json()[0]})
    else:
        form = forms.EditMood(instance=instance)
    return render(request, 'moods/edit_mood.html', {'form':form, 'id': id})
