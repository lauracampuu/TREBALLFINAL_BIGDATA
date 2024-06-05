import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import glob
import json
import pandas as pd

# Configurar las credenciales de cliente de Spotify
client_id = 'ea9682c5803845a8864dfd8f121fbcdd'
client_secret = 'cfd9c8d9f9a5409b819220c9eb91a81b'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtener la lista de archivos JSON en el directorio info_canciones
json_files = glob.glob('info_canciones/*.json')

# Inicializar listas para almacenar los datos de artistas, seguidores y géneros
artist_id_list = []
followers_list = []
genres_list = []

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

    # Agregar los datos a las listas
    artist_id_list.append(artist_id)
    followers_list.append(followers)
    genres_list.append(genres)

# Crear un DataFrame con los datos de artistas, seguidores y géneros
artist_data = pd.DataFrame({
    "ID del Artista": artist_id_list,
    "Seguidores": followers_list,
    "Géneros": genres_list
})

print(artist_data)

# Cargar el archivo Excel existente como DataFrame
existing_excel_path = "excels_de_playslist/todas_las_playlists.xlsx"
existing_df = pd.read_excel(existing_excel_path)

# Fusionar el DataFrame existente con los nuevos datos del artista
merged_df = pd.merge(existing_df, artist_data, on="ID del Artista", how="left")

# Guardar el DataFrame combinado en un nuevo archivo Excel
merged_excel_path = "excels_de_playslist/artistas_con_informacion.xlsx"
merged_df.to_excel(merged_excel_path, index=False)

