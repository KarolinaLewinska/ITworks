from bs4 import BeautifulSoup
from requests import get
import sqlite3

db = sqlite3.connect('courses.db')
cursor = db.cursor()

categories = {'big-data', 'elektronika', 'grafika-wideo-cax', 'gry', 'machine-learning', 'matematyka', 
    'narzedzia-programistyczne', 'office', 'programowanie', 'sieci-komputerowe', 'systemy-operacyjne',
    'urzadzenia-mobilne', 'webmasterstwo', 'biznes-i-ekonomia', 'rozwoj-osobisty', 'dla-dzieci'}

for category in categories:
    URL = 'https://videopoint.pl/kategorie/'+category
    page = get (URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    courses = bs.find_all("img", class_="lazy")
    for course in courses:
        course_title = course.parent['title']
        course_url = "https:"+course.parent['href']
        cursor.execute ('INSERT INTO courses VALUES (?, ?)', (course_title, course_url))
db.commit()
db.close()