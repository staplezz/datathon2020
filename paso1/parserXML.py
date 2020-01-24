from xml.etree import ElementTree
import os
import csv

'''
Parte 1 del proyecto de Datathon.
- Parser del xml dado de los autores hacia un archivo csv.
- Se incluyen los datos de los autores que tengan solo la etiqueta
- id_article y autor.
 Además se extraen sólo las publicaciones con etiqueta "article" e
 "inproceeding"
'''

#Leemos el archivo xml.
tree = ElementTree.parse("dblp_1990_2000_clean_utf8.xml")

#Creamos el archivo csv en donde almacenaremos
#los datos necesarios.
csv_authorships = open("authorships.csv", "w", newline='', encoding='utf-8')
csvwriter = csv.writer(csv_authorships)

#Creamos y escribimos los nombres de las columnas de nuestros datos.
col_names = ['id_article', 'author']
csvwriter.writerow(col_names)

#Obtenemos la raíz del árbol de xml.
root = tree.getroot()

#Iteramos sobre los datos del xml.
#Artículos
for article in root.findall('article'):
	articleyear = int(article.find('year').text)
	if articleyear >= 1990 and articleyear <= 2000:
		for autor in article.iter('author'):
			event_data = []
			key = article.get('key')
			key = key.split("/")[-1]
			event_data.append(key)
			event_data.append(autor.text)

			csvwriter.writerow(event_data)
	else:
		continue

#Inproceedings
for article in root.findall('inproceedings'):
	articleyear = int(article.find('year').text)
	if articleyear >= 1990 and articleyear <= 2000:
		for autor in article.iter('author'):
			event_data = []
			key = article.get('key')
			key = key.split("/")[-1]
			event_data.append(key)
			event_data.append(autor.text)

			csvwriter.writerow(event_data)
	else:
		continue

csv_authorships.close()
