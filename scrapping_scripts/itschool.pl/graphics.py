from bs4 import BeautifulSoup
from requests import get
import sqlite3

URL = 'https://itschool.pl/szkolenia/grafika/'
db = sqlite3.connect('courses.db')
cursor = db.cursor()

page = get (URL)
bs = BeautifulSoup(page.content, 'html.parser')
courses = bs.find_all('a', class_='training-box')
for course in courses:
    course_title = course.find('h4', class_='name').get_text()
    course_url = course['href']
    cursor.execute ('INSERT INTO courses VALUES (?, ?)', (course_title, course_url))
db.commit()

db.close()