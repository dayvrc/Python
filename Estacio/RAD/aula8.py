import requests
from bs4 import BeautifulSoup

url='https://www.bbc.com/portuguese'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('h3', limit=5)

    for index, title in enumerate(titles):
        print(f"{index+1}, {title.text.strip()}")
else:
    print(f"Falha na requisição.",response.status_code)