import requests
from bs4 import BeautifulSoup

url = "https://www.antyradio.pl/Radio/Turbo-Top"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('div', {'class': 'votingData'})
rows = table.find_all('div', {'class': 'list-element track list'})
songs = []
for row in rows:
    title_track_soup = row.find('div', {'class': 'title-track'})
    title_track = title_track_soup.text.strip()
    songs.append(title_track)
print(songs)

