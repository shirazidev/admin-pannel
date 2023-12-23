from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_page),
    path('users/',views.users),
    path('<name>/',views.home_page)
]
