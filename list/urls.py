from django.urls import path

from .views import SomeListView

urlpatterns = [
    path('', SomeListView.as_view()),
]