
from django.urls import path
from .views import Message_View

urlpatterns = [
    
    path("", Message_View.as_view(), name="message")
    
]
