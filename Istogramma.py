from Backend_Citizien_Science import res
import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import OSMPythonTools as osm
import folium as fol
import webbrowser
import dash
from dash import dcc, html, Output, Input
import plotly.express as px
import pandas as pd
import folium
import json
import webbrowser

# Simula i dati (sostituisci res() con la tua funzione se serve)
dati = json.loads(res())
df = pd.DataFrame(dati, columns=["ID", "Orario", "Val Inquinanti", "Latitudine", "Longitudine"])
df["ID_Orario"] = df["ID"].astype(str) + " - " + df["Orario"]

# Crea l'app Dash
app = dash.Dash(__name__)

# Grafico interattivo
fig = px.bar(
    df,
    x="ID_Orario",
    y="Val Inquinanti",
    custom_data=["Latitudine", "Longitudine", "Val Inquinanti", "ID", "Orario"]
)
fig.update_traces(hovertemplate='ID-Orario: %{x}<br>Valore: %{y}<extra></extra>')

app.layout = html.Div([
    html.H2("Valori Inquinanti (clicca per mappa)"),
    dcc.Graph(id='grafico', figure=fig),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('grafico', 'clickData')
)
def apri_mappa(clickData):
    if clickData is not None:
        lat = clickData["points"][0]["customdata"][0]
        lon = clickData["points"][0]["customdata"][1]
        val_inquinante = clickData["points"][0]["customdata"][2]
        id_val = clickData["points"][0]["customdata"][3]
        orario = clickData["points"][0]["customdata"][4]

        # Crea la mappa con popup dettagliato
        mappa = folium.Map(location=[lat, lon], zoom_start=15)
        popup_text = f"ID: {id_val}<br>Orario: {orario}<br>Inquinante: {val_inquinante}<br>Lat: {lat}, Lon: {lon}"
        folium.Marker([lat, lon], popup=popup_text).add_to(mappa)
        nome_file = "mappa_osm.html"
        mappa.save(nome_file)
        webbrowser.open(nome_file)

        return f"Mappa aperta per ID {id_val} alle {orario} (valore: {val_inquinante})"
    return "Clicca su una colonna per aprire la mappa."

app.run(debug=True)
