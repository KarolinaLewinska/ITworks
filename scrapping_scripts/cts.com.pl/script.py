import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('courses.db')
cursor = conn.cursor()

categories = {'active-directory', 'android', 'apache-solr', 'autocad', 'bpmnrupuml', 
    'ecc-ec-council-ceh-ecsa', 'cissp', 'comptia', 'dl', 'docker','inzynieria-wymagan', 
    'isaca','linuxunix', 'mcafee', 'bezpieczenstwo-testy-penetracyjne-hacking', 'sql',
    'testowanie', 'user-experience', 'net-visual-studio-net', 'windows-server'}

for category in categories:
    URL = 'https://cts.com.pl/kategoria-szkolenia/'+category
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