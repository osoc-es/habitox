import database as db
from models import tweets
import requests

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"

querystring = {"autoCorrect":"false","pageNumber":"1","pageSize":"10","q":"Coronavirus","safeSearch":"true","fromPublishedDate":"2020-02-01"}

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "79b62f1513mshef86f0add182909p174046jsn96335696bb47"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)