from bs4 import BeautifulSoup
from requests import get
import sqlite3

db = sqlite3.connect('courses.db')
cursor = db.cursor()

categories = {'access', 'ajax-javascript', 'analiza-statystyka', 'android', 'c-linux-kernel', 'c-net', 
    'bazy-danych-sql', 'excel', 'java', 'linux', 'sieci', 'office', 'openoffice', 'inne-jezyki-programowania',
    'outlook', 'php', 'powerpoint', 'project', 'python', 'security', 'uml', 'ux', 'vba', 'word', 'xml'}

for category in categories:
    URL = 'https://www.alx.pl/tech/'+category+'/'
    page = get (URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    courses = bs.find_all('td', class_='lp-courseName')
    for course in courses:
        course_title = course.find('a').get_text()
        course_url = "https://www.alx.pl" + course.find('a')['href']
        cursor.execute ('INSERT INTO courses VALUES (?, ?)', (course_title, course_url))
    db.commit()

db.close()