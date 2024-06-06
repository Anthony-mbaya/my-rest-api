from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello_tonny', views.HelloAPIView.as_view()),
]
