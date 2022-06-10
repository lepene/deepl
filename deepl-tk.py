""" Traduction avec les Apis du site www.deepl.com
    avec interface graphique Tkinter.
"""

import requests
import urllib
from urllib.parse import urlparse
from tkinter import *
from tkinter import ttk

""""
Example Request
GET /v2/translate?text=Hallo%20Welt!&target_lang=EN&auth_key=123
Example Response
{ "translations": [ { "detected_source_language": "DE", "text": "Hello World!" } ] }

exemple du compteur d'utilisation du compte Deepl
GET /v1/usage?auth_key=123
Response: {'character_count': 1600, 'character_limit': 1000000}

exemple de requête Get, anglais vers français
get("https://api.deepl.com/v2/translate?auth_key=ac3f95a0-eb04-8064-867c-ded3eb95f373
                &text=The%20link%20changes%20automatically%20&source_lang=EN&target_lang=FR")
réponse json
{'translations': [{'detected_source_language': 'EN', 'text': 'Le lien change automatiquement'}]}
"""

url_deepl = "https://api.deepl.com/v2/translate"
auth_key = "ac3f95a0-eb04-8064-867c-ded3eb95f373"
langue_source = "en"
langue_cible = "fr"
# création fenetre d'acceuil
fenetre_acceuil = Tk()
fenetre_acceuil.title('Traduire avec Deepl')
style = ttk.Style()
style.theme_use('classic')
panneau_central = ttk.PanedWindow(fenetre_acceuil, orient=VERTICAL)
# ajouter les zones de textes
label_utilisation = Label(panneau_central)
label_utilisation.pack(side=BOTTOM)
panneau_central.add(label_utilisation)
txt_source = Text(panneau_central)
txt_source.pack(side=BOTTOM)
panneau_central.add(txt_source)
txt_destination = Text(panneau_central)
txt_destination.pack(side=BOTTOM)
panneau_central.add(txt_destination)


# traduire de la zone de texte source vers la zone de texte cible
def traduire():
    txt = txt_source.get(1.0, END)
    txt = urllib.parse.quote(txt)
    url = f"{url_deepl}?auth_key={auth_key}&text={txt}&source_lang={langue_source}&target_lang={langue_cible}"
    req1 = requests.get(url)
    traduction = req1.json()['translations'][0]['text']
    txt_destination.insert(END, traduction)


# afficher des infos sur le compte Deepl
def infos():
    req = requests.get(f"https://api.deepl.com/v1/usage?auth_key={auth_key}")
    label_utilisation.insert(0, str(req.json()))


# ajouter les bouttons
btn_traduire = Button(fenetre_acceuil, text='Traduire', command=traduire)
btn_traduire.pack(side=BOTTOM)
panneau_central.add(btn_traduire)
# afficher fenêtre
panneau_central.pack(fill=BOTH, expand=True)
fenetre_acceuil.mainloop()
