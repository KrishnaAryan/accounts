
from django.urls import path,include
from .views import *
urlpatterns = [
    path('api/message/',MessageList.as_view())
    
]
