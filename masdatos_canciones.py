import glob
import json
import pandas as pd

# Cargar el archivo Excel existente
excel_file_path = "excels_de_playslist/todas_las_playlists.xlsx"
df_existing = pd.read_excel(excel_file_path)

# Iterar sobre los datos JSON y agregar características al DataFrame existente
for index, row in df_existing.iterrows():
    track_id = row["track_id"]
    json_file_path = glob.glob(f"rawdata2/{track_id}*.json")

    if json_file_path:  # Verificar si se encontró un archivo JSON
        with open(json_file_path[0], 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            features_dict = json_data[0]  # Obtener el primer elemento del JSON

            # Añadir características al DataFrame
            df_existing.at[index, "danceability"] = features_dict.get("danceability")
            df_existing.at[index, "energy"] = features_dict.get("energy")
            df_existing.at[index, "key"] = features_dict.get("key")
            df_existing.at[index, "loudness"] = features_dict.get("loudness")
            df_existing.at[index, "mode"] = features_dict.get("mode")
            df_existing.at[index, "speechiness"] = features_dict.get("speechiness")
            df_existing.at[index, "acousticness"] = features_dict.get("acousticness")
            df_existing.at[index, "instrumentalness"] = features_dict.get("instrumentalness")
            df_existing.at[index, "liveness"] = features_dict.get("liveness")
            df_existing.at[index, "valence"] = features_dict.get("valence")
            df_existing.at[index, "tempo"] = features_dict.get("tempo")
            df_existing.at[index, "duration_ms"] = features_dict.get("duration_ms")
            df_existing.at[index, "time_signature"] = features_dict.get("time_signature")

# Guardar el DataFrame actualizado en el mismo archivo Excel
df_existing.to_excel(excel_file_path, index=False)