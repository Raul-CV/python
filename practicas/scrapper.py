import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url,timeout=10)

texto = respuesta.text

soup = BeautifulSoup(texto, "html.parser")

preguntas = soup.select(".s-post-summary")

for pregunta in preguntas:
     titulo = pregunta.select_one(".s-link").get_text()
     autor = pregunta.select_one(".s-user-card--link").get_text()
     print(f"el autor es: {autor.strip()} \nel titulo es: {titulo}")
     print(f"===============**=====================================")

