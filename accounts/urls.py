from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegistrationView, ProfileView, UsersListView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('user-<int:pk>/profile/', ProfileView.as_view(), name="profile"),
    path('users/', UsersListView.as_view(), name="user-list"),
]
