from django.urls import path
from .views import PersonView

urlpatterns = [
    path('persons/', PersonView.as_view())
]