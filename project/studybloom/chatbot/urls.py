
from django.urls import path
from . import views
from .views import chatbot

urlpatterns = [
    path('chatbot/', chatbot, name='chatbot'),

]
