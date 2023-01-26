from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterCreateView, SignInView


urlpatterns = [
    path('reg/', RegisterCreateView.as_view(), name='reg'),
    path('auth/', SignInView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
]