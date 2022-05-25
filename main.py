import csv
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

f = open('cartoon.csv', 'w', newline='\n')
f_obj = csv.writer(f)
f_obj.writerow(['Title', 'Year', 'IMDB'])
ind = 1
while ind < 5:
    url = f'https://geo.saitebi.ge/cat/3/{str(ind)}/anime.html'
    r = requests.get(url)
    soup_all = BeautifulSoup(r.text, 'html.parser')
    soup = soup_all.find('div', id='content')
    all_movies = soup.find_all('div', class_='movie-items-wraper')
    for each in all_movies:
        title = each.find('div', class_='h-title-origin').text
        year = each.find('div', class_='h-year').text
        imdb1 = each.find('div', class_='hover-wraper')
        imdb = each.imdb.text
        print(title, year, imdb)
        f_obj.writerow([title, year, imdb])

    ind += 1
    sleep(randint(15, 20))

