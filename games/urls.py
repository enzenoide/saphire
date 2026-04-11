# games/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'), # Rota de cadastro
    path('<int:pk>/', views.game_detail, name='game_detail'),
]