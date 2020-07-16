# Vamos a usar la librería pytrends (librería no oficial para la API de Google Trends)
import pandas as pd    
from datetime import datetime                   
from pytrends.request import TrendReq
from models import trend
import database as db

def getData(searchData):
    #Ponemos la fecha como un String, en formato estadounidense (YYYY/MM/DD) y creamos el intervalo, donde primero va la fecha anterior
    interval = '2019-01-01 '+ datetime.today().strftime('%Y-%m-%d')
    # Creamos la conexion a google trends
    pytrend = TrendReq(hl='en-US', tz=360)
    """ Ahora, obtenemos las busquedas desde hoy hasta el 1 de Enero. Solo el atributo kw_list es obligatorio. 
        timeframe: Intervalo de tiempo. Por defecto va desde hoy hasta hace 5 años
        geo: Localizacion, alpha-2 code del pais. Spain seria 'ES'
        gprop: Tipo de busqueda (web, imagenes, youtube...). Vacio es busqueda de web
    """
    pytrend.build_payload(
        kw_list = searchData,
        geo = 'ES',
        timeframe = interval,
        gprop = 'youtube'
        )
    #Extraemos los datos de interes a lo largo del tiempo
    data = pytrend.interest_over_time()
    return data


# Erase everything we have to mine properly
with db.engine.connect() as con:
    con.execute("DELETE FROM trends WHERE trends.id>=1;")

# Grupos de Analisis
groups={
    'Resistiré':['Resistiré','Dúo Dinámico'],
	'YTKids':['Peppa Pig','Patrulla Canina'],
}

"""
    Group = Grupo de analisis, i.e. Teleenseñanza
    data = Pandas DataFrame (nuestros datos)
    ind = Fecha - TimeStamp Object (la fecha que acompaña al valor numérico)
    name = Busqueda a analizar, i.e. Zoom
    x[i][ind] = Valor Numérico  
"""

for group in groups:
    data = getData(groups[group])
    for ind in data.index:
        for name in groups[group]: 
            dbtrend = trend(group,name,str(ind),data[name][ind])
            db.session.add(dbtrend)

    db.session.commit()
db.session.commit()

