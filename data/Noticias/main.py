# Importamos las noticias desde el comienzo de la pandemia (febrero) hasta la nueva normalidad
from datetime import datetime                   
from models import news
import database as db
import csv

with open('Noticias.csv', newline='\n',encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Starting CSV READ")
            
        date = row["date"]
        keyWords = str(row["key_words"])
        description = str(row["description"])
        

        Dailynew = news(date,keyWords.encode("UTF-8"),description.encode("UTF-8"))
        db.session.add(Dailynew)


        line_count += 1
    db.session.commit()
    print(f'Processed {line_count} lines.')