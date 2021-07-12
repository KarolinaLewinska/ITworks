from matplotlib.figure import Figure
import numpy as np
import sqlite3

def get_data(categories):
    stats = dict.fromkeys(categories, 0)
    conn = sqlite3.connect('courses.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    for key in stats.keys():
        cur.execute("SELECT COUNT(*) FROM courses WHERE course_title LIKE '%" + key + "%'")
        conn.commit()
        rows = cur.fetchall(); 
        for row in rows:
            stats[key] = row[0]
    conn.close()
    return stats

def draw_plot(stats, y_label, title, file_title):
    stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=True))
    lan_names = list(stats.keys())
    lan_values = list(stats.values())

    fig1 = Figure()
    ax1 = fig1.subplots()
    ax1.bar(lan_names[:5], lan_values[:5], color = ['limegreen', 'SeaGreen', 'forestgreen', 'green', 'darkgreen'])
    ax1.set_ylabel(y_label)
    ax1.set_title(title)
    fig1.savefig('static/'+file_title)


languages = ["Python", "C#", "C++", "Java", "VisualBasic", "JavaScript", "PHP", "SQL"]
languages_stats = get_data(languages)
draw_plot(languages_stats, 'liczba ofert', 'Najpopularniejsze jezyki programowania', 'languagesChart.png')


topics = ['Programowanie', 'Sieci', 'Machine-learning', 'Big-Data', 'Windows', 'Linux', 'Mac', 'Testowanie', 'Grafika', 'Zarządzanie', 'Microsoft', 'Apple', 'Bezpieczeństwo', 'Bazy']
topics_stats = get_data(topics)
draw_plot(topics_stats, 'liczba ofert', 'Najpopularniejsza tematyka', 'topicsChart.png')