import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('courses.db')
cursor = conn.cursor()

categories = {'analysis', 'mobile', 'architecture', 'automotive', 'data-engineering-data-science', 
    'databases', 'devops', 'excel', 'git', 'java', 'management', 'methodologies', 'script', 
    'administration', 'telecom', 'testing', 'web'}

for category in categories:
    URL = 'https://www.luxoft-training.pl/katalog/'+category+'/'
    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    results_by_id = bs.find(id='middle-content')
    courses = results_by_id.find_all('div', class_='course-content')
    for course in courses:
        course_title = course.find('div', class_='course-name').get_text()
        main_url = 'https://www.luxoft-training.pl'
        course_url = main_url + course.find('a')['href']
        cursor.execute('INSERT INTO courses VALUES (?, ?)', (course_title, course_url))

conn.commit()
conn.close()