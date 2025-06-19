from django.urls import path
from .views import SignupView, SigninView, health_check

urlpatterns = [
    path('signup/', SignupView.as_view(), name="list-create-user-view"),
    path('signin/', SigninView.as_view(), name="sigin-view"),
    path('health/', health_check, name='health-check'),
]

