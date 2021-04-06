from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/browser', methods=['GET', 'POST'] )
def browser():
    if request.method == "POST":
        if 'java' in request.form:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from courses WHERE course_title LIKE '%java%'")
            conn.commit()
            rows = cur.fetchall()
            return render_template('browser.html', rows=rows)
        elif 'html' in request.form:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from courses WHERE course_title LIKE '%html%'")
            conn.commit()
            rows = cur.fetchall()
            return render_template('browser.html', rows=rows)
        elif 'csharp' in request.form:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from courses WHERE course_title LIKE '%c#%'") 
            conn.commit()
            rows = cur.fetchall()
            return render_template('browser.html', rows=rows)
        elif 'javascript' in request.form:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from courses WHERE course_title LIKE '%javascript%'")
            conn.commit()
            rows = cur.fetchall()
            return render_template('browser.html', rows=rows)
        elif 'php' in request.form:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from courses WHERE course_title LIKE '%php%'")
            conn.commit()
            rows = cur.fetchall()
            return render_template('browser.html', rows=rows)
        elif 'python' in request.form:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from courses WHERE course_title LIKE '%python%'")
            conn.commit()
            rows = cur.fetchall()
            return render_template('browser.html', rows=rows)
        elif 'sql' in request.form:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from courses WHERE course_title LIKE '%sql%'") 
            conn.commit()
            rows = cur.fetchall()
            return render_template('browser.html', rows=rows)
        else:
            conn = sqlite3.connect('courses.db')
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            search = request.form['search']
            cur.execute("SELECT * from courses")
            conn.commit()
            rows = cur.fetchall(); 
            return render_template('browser.html', rows=rows)
              
    return render_template('browser.html')

@app.errorhandler(500) 
def internal_error(error):
    return render_template('error.html')    

if __name__ == "__main__":
    app.run()