from django.shortcuts import redirect,get_object_or_404
from games.models import Games
from .forms import ReviewForm

# Create your views here.
def create_review(request,game_id):
    if request.method == 'POST':
        game = get_object_or_404(Games,id=game_id)
        #cria uma instancia do FORM com o post
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            #cria mas nao salva uma instancia review
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            #salva a instancia
            review.save()
        
        return redirect('game_detail',pk=game_id)

