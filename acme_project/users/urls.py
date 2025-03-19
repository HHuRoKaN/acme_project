from django.urls import include, path
from .views import MyUserCreateView


app_name = 'users'

urlpatterns = [
    path('registration/', MyUserCreateView.as_view(), name='registration'),
]
