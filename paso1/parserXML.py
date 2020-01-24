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
for article in root.findall('article'):
	for autor in article.iter('author'):
		event_data = []
		print(autor.text)
		event_data.append(article.get('key'))
		event_data.append(autor.text)
		print(article.get('key'))
		

		csvwriter.writerow(event_data)

csv_authorships.close()
