import os
import re
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Función para llamar a la API de Grobid y extraer el texto del documento PDF
def extract_text_with_grobid(pdf_path):
    url = 'https://kermitt2-grobid.hf.space/api/processFulltextDocument'
    files = {'input': open(pdf_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to extract text from {pdf_path} using Grobid")
        return ''

# Función para crear una nube de palabras clave basada en la información del abstract
def generate_keyword_cloud(abstracts):
    text = ' '.join(abstracts)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Función para contar el número de figuras por artículo
def count_figures(articles):
    fig_counts = [len(re.findall(r'\bfigure\b|\bfig\b', article, flags=re.IGNORECASE)) for article in articles]
    plt.bar(range(1, len(articles) + 1), fig_counts)
    plt.xlabel('Article')
    plt.ylabel('Number of Figures')
    plt.title('Number of Figures per Article')
    plt.show()

# Función para extraer los enlaces de un artículo
def extract_links(article_url):
    url = 'https://kermitt2-grobid.hf.space/api/processReferences'
    files = {'input': open(pdf_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        references = [a['href'] for a in soup.find_all('a', href=True)]
        return references
    else:
        print(f"Failed to extract references from {pdf_path} using Grobid")
        return []

# Directorio donde se encuentran los archivos PDF
pdf_directory = '/Users/adrian/Developer/GitHub/ResearchSE_Deliver1/papers'

# Listas vacías para almacenar los datos extraídos
abstracts = []
articles = []

# Extraer texto de archivos PDF y llenar las listas abstracts y articles utilizando Grobid
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        text = extract_text_with_grobid(pdf_path)
        abstracts.append(text[:1000])  # Tomar solo los primeros 1000 caracteres como abstracto
        articles.append(text)

# Llamadas a las funciones para realizar las tareas
generate_keyword_cloud(abstracts)
count_figures(articles)

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        print(f"Links found in {pdf_path}:")
        links = extract_links(pdf_path)
        print(f"Links found in {pdf_path}:")
        for link in links:
            print(link)
        print("\n")
