from django.urls import path
from . import views
urlpatterns = [
    path('', views.iteam_page)
]
