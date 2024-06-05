import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from pathlib import Path

# Inicializar cliente de autenticación de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id='ea9682c5803845a8864dfd8f121fbcdd',client_secret='cfd9c8d9f9a5409b819220c9eb91a81b')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

todas_las_playlists = pd.read_excel("todas_las_playlists.xlsx")
print(todas_las_playlists)


for index, row in todas_las_playlists.iterrows():
    print(row)
    track_id = row["track_id"]
    file_path = Path(f'info_canciones/{track_id}.json')


    if file_path.exists():
        print(f"La playlist {track_id} ya se ha descargado")
        pass
    else:
        print(f"Se está pidiendo el track {track_id}")
        api_response = spotify.track(track_id)
        print(f"Se ha capturado el track {track_id}")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(api_response, f, ensure_ascii=False, indent=4)