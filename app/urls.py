
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('get/<str:u>',views.get),
    path('info/<str:u>',views.info)
]
