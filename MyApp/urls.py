from django.urls import path
from .views import *

urlpatterns = [
path('', MyHome,name = 'home'),
path('register/', RegisterUser.as_view()),
path('loginuser/', LoginUser.as_view()),
path('logoutuser/', LogoutUser.as_view()),
path('student/', StudentAPI.as_view()),
path('student/<str:pk>/', StudentAPI.as_view()),
]