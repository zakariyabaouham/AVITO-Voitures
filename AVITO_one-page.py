#By BAOUHAM Zakariya
#Bibilotheques
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

#Liste des des donnes qu on veut recuperer
prixx=[] #Liste pour stocker les prix
voitures=[] #Liste pour stocker la liste des voitures
#images=[]#Liste pour stocker l'url de l'image
villes=[]
date_pubs=[]

url = "https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre"
reponse_page = requests.get(url)#requete http pour recuperer l url qui heberge la page web AVITO

page_web= BeautifulSoup(reponse_page.content,'lxml') #Anaylse de la page recuperee avec BeautifulSoup

all_cars=page_web.find_all('div', attrs={'class':['item li-hover', 'item li-hover bump', 'item li-hover bump bump bump bump', 'item li-hover highlight bump','item li-hover bump highlight','item li-hover bump bump highlight', 'item li-hover insertion bump bump bump','item li-hover insertion bump bump','item li-hover bump bump','item li-hover bump highlight bump','item li-hover insertion bump','item li-hover bump highlight bump highlight']})
#boucle for
for a in all_cars:
	prix = a.find('span', attrs={'class':'price_value'})
	voiture=a.find('h2', attrs={'class':'fs14 d-inline-block text-truncate'})
	#image=a.find('img', attrs={'class':'lazy'})
	ville=a.find('div', attrs={'class':'re-text'})
	date_pub=a.find('span', attrs={'class':'age-text'})
	#recuperation de texte
	prixx.append(prix.get_text())
        voitures.append(voiture.get_text())	
        #images.append(image.get("src"))
  	villes.append(ville.get_text())	
	date_pubs.append(date_pub.get_text())
	#print('\n')		
	#print(villes)		
	#decalaration de dataframe qui avoir de types differents (numeriques, text,..)
	df = pd.DataFrame({'voiture':voitures,'Ville':villes,'Date':date_pubs,'Prix':prixx}) 

	df.to_csv('Voitures.csv', index=False, encoding='utf-8') #stockage des donnees dans un format CSV
	print(df)

#Effectuer des operations sur les donnees recuperees		
dff=pd.read_csv('Voitures.csv') #lire les donnees de fichier produits
print(dff.Prix)
#Converstion en numeriques
dff.Prix = pd.to_numeric(dff.Prix, errors='coerce').fillna(0).astype(np.int64)
print (dff.Prix.dtypes)

print(dff.groupby('Ville').Prix.mean().reset_index(name="Prix moyen"))
print(dff.groupby('Ville').Prix.max().reset_index(name="Prix max"))

