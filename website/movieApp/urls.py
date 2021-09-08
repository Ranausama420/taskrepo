from django.urls import path

from . import views
app_name = 'movieApp'


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/<str:title>/', views.detail, name='detail'),



]