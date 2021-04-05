from bs4 import BeautifulSoup
from requests import get
import sqlite3

URL = 'https://www.alx.pl/tech/office/'
db = sqlite3.connect('courses.db')
cursor = db.cursor()

page = get (URL)
bs = BeautifulSoup(page.content, 'html.parser')
courses = bs.find_all('td', class_='lp-courseName')
for course in courses:
    course_title = course.find('a').get_text()
    course_url = 'alx.pl' + course.find('a')['href']
    cursor.execute ('INSERT INTO courses VALUES (?, ?)', (course_title, course_url))
db.commit()

db.close()