import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from pathlib import Path

# Inicializar cliente de autenticación de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id='b486662ed48c495ea920f68349468d18',client_secret='a1da923f2c2d4882b3fab9cd0c0ca44b')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

todaslasplaylists = pd.read_excel("todas_las_playlists.xlsx")
print(todaslasplaylists)

# Iterar sobre los países y obtener los artistas más escuchados
for index, row in todaslasplaylists.iterrows():
    track = row["track_id"]
    file_path = Path(f'rawdata2/{track}.json')

    if file_path.exists():
        print(f"La cancion {track} ya se ha descargado")
        pass
    else:
        api_response = spotify.audio_features(track)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(api_response, f, ensure_ascii=False, indent=4)
