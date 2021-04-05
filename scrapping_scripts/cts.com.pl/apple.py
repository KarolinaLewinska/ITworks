import requests
from bs4 import BeautifulSoup
import sqlite3

def get_data_from_pages(page_number):
    url = 'https://cts.com.pl/tcat/apple/page/' + str(page_number)
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    page = requests.get(url)
    soup_parser = BeautifulSoup(page.content, 'html.parser')
    results_by_id = soup_parser.find(id='main')
    courses_info = results_by_id.find_all('header', class_='entry-header')
    for course in courses_info:
        title = course.find('a').get_text()
        url = course.find('a')['href']
        cursor.execute('INSERT INTO courses VALUES (?, ?)', (title, url))
        conn.commit()
    conn.close()

i = 2
for i in range(4):
    get_data_from_pages(i)

