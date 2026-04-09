import requests
from django.core.management.base import BaseCommand
from games.models import Games
from dotenv import load_dotenv
import os
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

class Command(BaseCommand):
    help = 'Import games from RAWG API'

    def handle(self, *args, **kwargs):
        #the api key is from rawg.io, you can get your own api key by creating an account on their website and generating an api key in the settings
        api_key = os.getenv('RAWG_API_KEY')  # Certifique-se de que a variável de ambiente RAWG_API_KEY esteja definida no arquivo .env
        # getting the url for the api request, we are getting the first 20 games from the api
        # the amout of games is set in page_size
        url = f'https://api.rawg.io/api/games?key={api_key}&page_size=20'

        self.stdout.write('Importing games from RAWG API...')
        #getting the data from the api and converting it to json format
        response = requests.get(url)
        data = response.json()

        for game in data['results']:
            # we are using get_or_create to avoid importing duplicate games, if a game with the same name already exists in the database, it will not be imported again
            game,created = Games.objects.get_or_create(
                name = game['name'],
                defaults={
                    'release_date': game.get('released'),
                    'genre': game['genres'][0]['name'] if game['genres'] else '',
                    'platforms': ', '.join([platform['platform']['name'] for platform in game['platforms']]) if game['platforms'] else '',
                    'cover_image': game['background_image'] if game['background_image'] else '',
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Game "{game.name}" imported successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Game "{game.name}" already exists. Skipping import.'))
