from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'moods'

urlpatterns = [
    path('new/', views.new_view, name="new"),
]
