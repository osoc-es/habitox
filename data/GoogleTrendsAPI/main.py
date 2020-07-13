# Vamos a usar la librería pytrends (librería no oficial para la API de Google Trends)
import pandas as pd    
import datetime as dt                    
from pytrends.request import TrendReq
# Creamos la conexion a google trends
pytrend = TrendReq(hl='en-US', tz=360)
# Definimos las tendencias a buscar (kw, keywords). Observacion: Google Trends no distingue tildes
kw = ['Resistiré','Dúo Dinámico']
# Obtenemos la fecha actual el intervalo de tiempo
currentYear = dt.datetime.now().year
currentMonth = dt.datetime.now().month
currentDay = dt.datetime.now().day

#Ponemos la fecha como un String, en formato estadounidense (MM/DD/YYYY) y creamos el intervalo, donde primero va la fecha anterior
interval = '2019-01-01 ' + str(currentYear) + '-' + str(currentMonth) + '-' + str(currentDay)

"""Ahora, obtenemos las busquedas desde hoy hasta el 1 de febrero. Solo el atributo kw_list es obligatorio. 
timeframe: Intervalo de tiempo. Por defecto va desde hoy hasta hace 5 años
geo: Localizacion, alpha-2 code del pais. Spain seria 'ES'
gprop: Tipo de busqueda (web, imagenes, youtube...). Vacio es busqueda de web"""
pytrend.build_payload(
    kw_list = kw,
    geo = 'ES',
    timeframe = interval
    )

#Extraemos los datos de interes a lo largo del tiempo
data = pytrend.interest_over_time()
#Ponemos los datos en un CSV. Antes de ello, borramos la columa 'isPartial' vacía que se genera.
data = data.drop(labels=['isPartial'],axis='columns')
image = data.plot(title = 'Búsquedas relacionadas con Resistiré en YouTube')
#Guardamos la grafica como png y los datos en csv
fig = image.get_figure()
fig.savefig('Trends_ResistireYT.png')
data.to_csv('Trends_ResistireYT.csv', encoding='utf_8_sig')