""" Classe qui traduis du texte avec les Apis du site www.deepl.com """

import sys
import requests
import json
import urllib
from urllib.parse import urlparse

""""
Example Request
GET /v1/translate?text=Hallo%20Welt!&target_lang=EN&auth_key=123
Example Response
{ "translations": [ { "detected_source_language": "DE", "text": "Hello World!" } ] }

exemple du compteur d'utilisation du compte Deepl
GET /v1/usage?auth_key=123
Response: {'character_count': 1600, 'character_limit': 1000000}

exemple de requête Get, anglais vers français
get("https://api.deepl.com/v1/translate?auth_key=0ab6522e-c7ca-80f9-89ae-f08f625b5c12&text=The%20link%20changes%20automatically%20&source_lang=EN&target_lang=FR")
réponse json
{'translations': [{'detected_source_language': 'EN', 'text': 'Le lien change automatiquement'}]}

//pour les gros volume de texte, on peut fractionner les envois
//avec plusieurs paramètres "text:" dans la limite de 50			
//en retour le résultat est lui aussi fractionné						
//donc on suppose que le texte est fractionné

"""


class Deepl:
    def __init__(self):
        super(Deepl, self).__init__()
        self.auth_key = "ac3f95a0-eb04-8064-867c-ded3eb95f373"
        self.url_deepl = "https://api.deepl.com/v2/"
        self.url_traduc_deepl = f"{self.url_deepl}translate?auth_key={self.auth_key}"
        self.url_infos_compte = f"{self.url_deepl}usage?auth_key={self.auth_key}"
        self.source = "en"
        self.cible = "fr"

    def traduire(self, source):
        txt = urllib.parse.quote(source)
        url = f"{self.url_traduc_deepl}&text={txt}&source_lang={self.source}&target_lang={self.cible}"
        req1 = requests.get(url)
        return req1.json()['translations'][0]['text']

    def infos(self):
        req = requests.get(self.url_infos_compte)
        return req.json()


