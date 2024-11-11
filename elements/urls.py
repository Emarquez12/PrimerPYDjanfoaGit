from django.urls import path
from elements import views

urlpatterns = [
    path('element/', views.ElementsView, name='home'),
]
