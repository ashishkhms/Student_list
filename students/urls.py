from django.urls import path
from . import views
urlpatterns = [
    path('', views.studentlist, name = 'studentlist'),
]
