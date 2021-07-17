from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'moods'

urlpatterns = [
    path('new/', views.new_view, name="new"),
    path('today/', views.today_view, name="today"),
    path('delete/<int:id>/', views.delete_view, name="delete"),
    path('edit/<int:id>/', views.edit_view, name="edit"),
]
