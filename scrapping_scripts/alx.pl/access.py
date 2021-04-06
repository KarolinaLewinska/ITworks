from bs4 import BeautifulSoup
from requests import get
import sqlite3

URL = 'https://www.alx.pl/tech/access/'
db = sqlite3.connect('courses.db')
cursor = db.cursor()

page = get (URL)
bs = BeautifulSoup(page.content, 'html.parser')
courses = bs.find_all('tr', class_='lp-courseRow')
for course in courses:
    course_title = course.find('a').get_text()
    course_url = 'alx.pl' + course.find('a')['href']
    # course_price = course.find('p', class_='lp-coursePriceNormal').get_text().strip()
    # cursor.execute ('INSERT INTO courses VALUES (?, ?, ?)', (course_title, course_url, course_price))
    cursor.execute ('INSERT INTO courses VALUES (?, ?)', (course_title, course_url))
db.commit()

db.close()