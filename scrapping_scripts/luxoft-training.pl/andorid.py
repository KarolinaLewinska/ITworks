import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.luxoft-training.pl/katalog/mobile/'
conn = sqlite3.connect('courses.db')
cursor = conn.cursor()
page = requests.get(url)
soup_parser = BeautifulSoup(page.content, 'html.parser')
results_by_id = soup_parser.find(id='middle-content')
courses_info = results_by_id.find_all('div', class_='course-content')
for course in courses_info:
    title = course.find('div', class_='course-name').get_text()
    main_url = 'https://www.luxoft-training.pl'
    url = main_url + course.find('a')['href']
    cursor.execute('INSERT INTO courses VALUES (?, ?)', (title, url))
    conn.commit()
conn.close()