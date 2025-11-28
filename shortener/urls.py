from django.urls import path
from .views import CreateShortURLView

urlpatterns = [
    path('create/',CreateShortURLView.as_view(),name='create'),
]