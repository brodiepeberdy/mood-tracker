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
]
