from django.urls import path

from users.views import login, UserCreateView, logout, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile')
]
