# Importamos las noticias desde el comienzo de la pandemia (febrero) hasta la nueva normalidad
from datetime import datetime                   
#from models import trend
#import database as db
import csv


with open('Noticias.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["date"]} - {row["key_words"]} - {row["description"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')