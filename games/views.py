from django.shortcuts import render
from .models import Games
# Create your views here.
def index(request):
    # this line is basically, go to the database and get all the games and store them in a variable called games, then we will pass this variable to the template to display the games on the homepage
    games = Games.objects.all()
    context = {
        'games': games
    }
    return render(request, 'index.html', context)