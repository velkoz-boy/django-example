from django.urls import path

from .views import SomeListView

urlpatterns = [
    path('<int:list_id>', SomeListView.as_view(), name='index'),
]