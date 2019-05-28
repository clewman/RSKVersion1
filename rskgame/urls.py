from django.urls import include, path
from . import views

app_name = 'rskgame'
urlpatterns = [
    path('', views.index, name='index'),
    path('tests', views.tests, name='tests'),
]
