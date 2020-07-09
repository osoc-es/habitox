# Vamos a usar la libreria pytrends (libreria no oficial para la API de google trends)
import pandas as pd                        
from pytrends.request import TrendReq
# Creamos la conexion a google trends
pytrend = TrendReq(hl='en-US', tz=360)
# Definimos las tendencias a buscar (kw, keywords). Observacion: Google Trends no distingue tildes

"""Solo kw_list es es requerido. 
timeframe: Intervalo de tiempo. Por defecto va desde hoy hasta hace 5 anios
geo: Localizacion, alpha-2 code del pais. Spain seria 'ES'
gprop: Tipo de busqueda (web, imagenes, youtube...). Vacio es busqueda de web"""
pytrend.build_payload(
    kw_list=['Resistire'],
    geo = 'ES',
    gprop='youtube'
    )

#Extraemos los datos de interes a lo largo del tiempo
data = pytrend.interest_over_time()
#Ponemos los datos en un CSV. Antes de ello, borramos la columa 'isPartial' vacia que se genera.
data = data.drop(labels=['isPartial'],axis='columns')
image = data.plot(title = 'Busquedas de Resistire en Youtube acorde a Google Trends ')
#Guardamos la grafica como png y los datos en csv
fig = image.get_figure()
fig.savefig('Trends_ResistireYT.png')
data.to_csv('Trends_ResistireYT.csv', encoding='utf_8_sig')   