from django.urls import path

from youtube import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='search_view'),
]
