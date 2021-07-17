from django.conf.urls import url
from django.urls import path
from . import views
from moods import views as moods_views

app_name = 'accounts'

urlpatterns = [
    path('', views.account_view, name=""),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('account/', views.account_view, name="account"),
    path('new/', moods_views.new_view, name="new"),
    path('today/', moods_views.today_view, name="today"),
    path('delete/<int:id>/', moods_views.delete_view, name="delete"),
    path('edit/<int:id>/', moods_views.edit_view, name="edit"),
]
