""" Traduction avec les Apis du site www.deepl.com """

import sys
import requests
import json
import urllib
from urllib.parse import urlparse
from PyQt5 import QtCore, QtGui, QtWidgets
from f1 import Ui_f1

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

"""

urlDeepl = "https://api.deepl.com/v2/translate"
auth_key = "ac3f95a0-eb04-8064-867c-ded3eb95f373"
source = "en"
cible = "fr"


# classe de la fenêtre principale
class FenetreAcceuil(QtWidgets.QMainWindow, QtWidgets.QWidget, Ui_f1):
    def __init__(self):
        super(FenetreAcceuil, self).__init__()
        self.setupUi(self)
        self.show()


# traduire de la zone de texte source vers la zone de texte cible        
def traduire():
    txt = fen1.sourceText.toPlainText()
    txt = urllib.parse.quote(txt)
    url = f"{urlDeepl}?auth_key={auth_key}&text={txt}&source_lang={source}&target_lang={cible}"

    req1 = requests.get(url)
    traduction = req1.json()['translations'][0]['text']
    fen1.cibleText.setPlainText(traduction)


# création application
app = QtWidgets.QApplication([])
fen1 = FenetreAcceuil()
# liaison entre le boutton traduire et la fonction traduire
fen1.buttonTraduire.clicked.connect(traduire)
# afficher les stats d'utilisation du compte Deepl
req = requests.get(f"https://api.deepl.com/v1/usage?auth_key={auth_key}")
fen1.labelUtilisation.setText(str(req.json()))
# lancement application
app.exec_()

''' Code Windev
sUrl,sRequetePost sont des chaîne
nNbText sont des entiers

//url Get:"https://api.deepl.com/v2/translate?auth_key="+CLE_DEEPl+"&text=Do it&target_lang=FR&source_lang=EN"
//réponse en json de deepl :{"translations":[{"detected_source_language":"EN","text":"le faire"}]}
source_lang = COMBO_LangueSource
target_lang = COMBO_LangueCible
source_text = SAI_TexteSource
sRequetePost = "auth_key="+CLE_DEEPl+"&text="+source_text+"&target_lang=FR&source_lang=EN"

sUrl = "https://api.deepl.com/v2/translate"
HTTPRequête(sUrl,"","",sRequetePost)
Resultat = UTF8VersChaîne(HTTPDonneRésultat(httpRésultat))
//pour les gros volume de texte, on peut fractionner les envois
//avec plusieurs paramètres "text:" dans la limite de 50			
//en retour le résultat est lui aussi fractionné						
//donc on suppose que le texte est fractionné

//compter le nombre de résultat de traductions
nNbText = ChaîneOccurrence(Resultat,"""text"":")
//la 1ère traduction commence en position 10, séparé par des guillemets
//(plus simple que les fonctions Json de windev)
POUR i = 1 À nNbText
	SAI_TexteCible += ExtraitChaîne(Resultat,i+9,"""") +RC	
FIN
'''
