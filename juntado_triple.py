"""import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import glob
import json

# Configurar las credenciales de cliente de Spotify
client_id = 'ea9682c5803845a8864dfd8f121fbcdd'
client_secret = 'cfd9c8d9f9a5409b819220c9eb91a81b'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtener la lista de archivos JSON en el directorio info_canciones
json_files = glob.glob('info_canciones/*.json')

# Iterar sobre cada archivo JSON
for json_file_path in json_files:
    # Leer el archivo JSON que contiene los datos de la canción
    with open(json_file_path, 'r', encoding='utf-8') as f:
        song_data = json.load(f)

    # Obtener el ID del primer artista de la lista
    artist_id = song_data["artists"][0]["id"]

    # Hacer una llamada a la API de Spotify para obtener información adicional del artista
    artist_info = spotify.artist(artist_id)

    # Extraer la información deseada del artista
    followers = artist_info['followers']['total']
    genres = artist_info['genres']

    # Imprimir la información del artista
    print("Seguidores del artista:", followers)
    print("Géneros del artista:", genres)"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Configurar las credenciales de cliente de Spotify
client_id = 'ea9682c5803845a8864dfd8f121fbcdd'
client_secret = 'cfd9c8d9f9a5409b819220c9eb91a81b'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Ruta al archivo JSON
json_file_path = 'info_canciones/*.json'

# Leer el archivo JSON que contiene los datos de la canción
with open(json_file_path, 'r', encoding='utf-8') as f:
    song_data = json.load(f)

# Obtener el ID del primer artista de la lista
artist_id = song_data["artists"][0]["id"]

# Hacer una llamada a la API de Spotify para obtener información adicional del artista
artist_info = spotify.artist(artist_id)

# Extraer la información deseada del artista
followers = artist_info['followers']['total']
genres = artist_info['genres']

# Imprimir la información del artista
print("Seguidores del artista:", followers)
print("Géneros del artista:", genres)