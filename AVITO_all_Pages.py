#By BAOUHAM Zakariya
import requests
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
prixx=[] #Liste pour stocker les prix
voitures=[] #Liste pour stocker le nom du voiture
#images=[]#Liste pour stocker l'url de l'image
villes=[]
date_pubs=[]
i=1 
url = "https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?o=" +str(i)
while True:
	i=i+1
	reponse_page = requests.get(url)
	if reponse_page.status_code != 200:
		break
	url = "https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?o=" +str(i)

	page_web= BeautifulSoup(reponse_page.content,'lxml')

	all_cars=page_web.find_all('div', attrs={'class':['item li-hover', 'item li-hover bump', 'item li-hover bump bump bump bump', 'item li-hover highlight bump','item li-hover bump highlight','item li-hover bump bump highlight', 'item li-hover insertion bump bump bump','item li-hover insertion bump bump','item li-hover bump bump','item li-hover bump highlight bump','item li-hover insertion bump','item li-hover bump highlight bump highlight']})
	for a in all_cars:
		prix = a.find('div', attrs={'class':'item-price'})
		voiture=a.find('h2', attrs={'class':'fs14 d-inline-block text-truncate'})
		#image=a.find('img', attrs={'class':'lazy'})
		ville=a.find('div', attrs={'class':'re-text'})
		date_pub=a.find('span', attrs={'class':'age-text'})
	
		prixx.append(prix.get_text())	
        	voitures.append(voiture.get_text())	
        	#images.append(image.get("src"))
  		villes.append(ville.get_text())	
		date_pubs.append(date_pub.get_text())
		#print('\n')		
		
		
		#print('\n'))
		df = pd.DataFrame({'Prix':prixx,'Voiture':voitures,'Ville':villes,'Date':date_pubs}) 
		df.to_csv('all_cars.csv', index=False, encoding='utf-8')
		print(df)
	




