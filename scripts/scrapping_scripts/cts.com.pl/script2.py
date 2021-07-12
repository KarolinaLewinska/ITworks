import requests
from bs4 import BeautifulSoup
import sqlite3

def get_data_from_multiple_pages(category, category_name, page_number):
    URL = 'https://cts.com.pl/'+category+'/'+category_name+'/page/'+ str(page_number)
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    results_by_id = bs.find(id='main')
    courses = results_by_id.find_all('header', class_='entry-header')
    for course in courses:
        course_title = course.find('a').get_text()
        course_url = course.find('a')['href']
        cursor.execute('INSERT INTO courses VALUES (?, ?)', (course_title, course_url))
        
    conn.commit()
    conn.close()

i = 1
for i in range(3):
    get_data_from_multiple_pages('kategoria-szkolenia','azure', i)

for i in range(8):
    get_data_from_multiple_pages('kategoria-szkolenia', 'microsoft', i)

for i in range(3):
    get_data_from_multiple_pages('kategoria-szkolenia','microsoft-office', i)

for i in range(4):
    get_data_from_multiple_pages('tcat', 'apple', i)