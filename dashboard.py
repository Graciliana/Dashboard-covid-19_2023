import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

#leitura dos dados Covid2023
#df = pd.read_csv('covidbr2023.csv', sep=";")
#df_states_city =  df[(~df['estado'].isna())]
#df_states_city
# para remover os dados dos municipios 
#df_states =  df[(~df['estado'].isna()) & (df['codmun'].isna())]
#dataframe dos estados e municipios
#df_states
#dataframe das regiao do Brasil 
#df_brasil =  df[df['regiao'] == 'Brasil']
#df_brasil

#exportar os dados para um arquivo csv
#df_states_city.to_csv('df_states_city.csv')
#df_states.to_csv('df_states.csv')
#df_brasil.to_csv('df_brasil.csv')

#leitura dos dos dataFrames
df_states_city = pd.read_csv('df_states_city.csv')
df_brasil = pd.read_csv('df_brasil.csv')
df_states_city.read_csv('df_states_city.csv')
#geo
brazil_states = json.load(open('geojson/brazil_geo.json', 'r'))
# type(brazil_states) 
# brazil_states.keys()
# brazil_states['features']
# type(brazil_states['features'])
# brazil_states['features'][0].keys()
# brazil_states['features'][0]['id']

