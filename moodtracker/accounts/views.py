from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from moods.models import Mood
from django.shortcuts import redirect
from django.contrib.auth import login, logout
import requests

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('/accounts/account')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/accounts/account')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts')

@login_required(login_url="/accounts/login/")
def account_view(request):
    profile = UserProfile.objects.get(user=request.user)
    # Order moods by date in descending order, hence the most recent is first.
    moods = Mood.objects.all().filter(creator=request.user).order_by('-date')
    # Retrieves a random quote from ZenQuotes.io
    response = requests.get("https://zenquotes.io/api/random")
    return render(request, 'accounts/manage.html', {"quote": profile.quote, "location": profile.location, "moods":moods, "quote": response.json()[0]})
