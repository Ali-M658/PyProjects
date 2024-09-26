import requests
from bs4 import BeautifulSoup


url = 'https://connected.mcgraw-hill.com/ssh/book.lesson.do?bookId=Y4HH351HGO4PJTR47L6WNELNBM&nodeId=TMX28L2YYNRW2RGC3N8MPS5QKY'

response = requests.get(url)

soup = BeautifulSoup(response.content ,'html.parser')

soup.find_all('p')

print(f'Content found: {soup}')