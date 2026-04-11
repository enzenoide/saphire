from django.shortcuts import render, get_object_or_404
from .models import Games
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    # this line is basically, go to the database and get all the games and store them in a variable called games, then we will pass this variable to the template to display the games on the homepage
    games = Games.objects.all()
    context = {
        'games': games
    }
    return render(request, 'index.html', context)


def game_detail(request, pk):
    jogo = get_object_or_404(Games, pk=pk)
    context = {
        'jogo': jogo
    }
    return render(request, 'game_detail.html', context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'