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


topics = ['programowanie', 'sieci', 'machine learning', 'big data', 'Windows', 'Linux', 'Mac', 'test', 'web', 'grafik', 'zarządzanie', 'Microsoft', 'Apple', 'bezpieczeństwo', 'bazy']
topics_stats = get_data(topics)
draw_plot(topics_stats, 'liczba ofert', 'Najpopularniejsza tematyka kursu', 'topicsChart.png')