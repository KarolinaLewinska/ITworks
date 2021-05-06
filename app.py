from flask import Flask, render_template, request, redirect, flash, redirect
import sqlite3
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
    return render_template('index.html')
                   
@app.route('/browser', methods=['GET','POST'])
def browser():
    if request.method == "GET": 
        return render_template('browser.html')
    if request.method == "POST":
        if 'java' in request.form:
            return redirect("/search-java")      
        elif 'html' in request.form:
            return redirect("/search-html")  
        elif 'csharp' in request.form:
            return redirect("/search-csharp") 
        elif 'c' in request.form:
            return redirect("/search-c") 
        elif 'cplusplus' in request.form:
            return redirect("/search-cplusplus") 
        elif 'javascript' in request.form:
            return redirect("/search-javascript") 
        elif 'php' in request.form:
            return redirect("/search-php") 
        elif 'python' in request.form:
            return redirect("/search-python") 
        elif 'sql' in request.form:
            return redirect("/search-sql") 
        elif 'searchButton' in request.form:
            try:
                conn = sqlite3.connect('courses.db')
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                search = request.form['search']
                query = "SELECT * from courses where course_title LIKE '% "+ search +" %' OR course_title LIKE '% "+ search +".%' OR course_title LIKE '% "+ search +",%' OR course_title LIKE '% "+ search +":%' ORDER BY course_title"
                cur.execute(query)
                conn.commit()
                rows = cur.fetchall(); 
                rows_number = len(rows)
                if rows:
                    flash("Liczba dostępnych kursów: " + str(len(rows)))
                if not rows:
                    flash("Brak kursów w bazie! Wpisz w wyszukiwarkę inne zagadnienie.")

                conn.close()
                return render_template('browser.html', rows=rows)
            except OperationalError:
                flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-java', methods=['GET','POST'])
def search_java():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%java%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page,pagination=pagination)
    except OperationalError:
            flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-html', methods=['GET','POST'])
def search_html():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%html%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
        page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-csharp', methods=['GET','POST'])
def search_csharp():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%c#%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-c', methods=['GET','POST'])
def search_c():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '% c %' OR course_title LIKE '% c.%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-cplusplus', methods=['GET','POST'])
def search_cplusplus():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%c++%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-javascript', methods=['GET','POST'])
def search_javascript():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%javascript%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-php', methods=['GET','POST'])
def search_php():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%php%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-python', methods=['GET','POST'])
def search_python():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%python%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.route('/search-sql', methods=['GET','POST'])
def search_sql():
    def get_courses(offset=0, per_page=10):
        return rows[offset: offset + per_page]
    try:
        conn = sqlite3.connect('courses.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        query = "SELECT * from courses WHERE course_title LIKE '%sql%' ORDER BY course_title"
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        rows_number = len(rows)
        if rows:
            flash("Liczba dostępnych kursów: " + str(len(rows)))
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total = len(rows)
        pagination_courses = get_courses(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
        conn.close()
        return render_template('categories_search_results.html', rows=pagination_courses, 
            page=page, per_page=per_page, pagination=pagination)
    except OperationalError:
        flash("Wystąpił błąd podczas próby połączenia się z bazą")

@app.errorhandler(500) 
def internal_error(error):
    return render_template('error.html')    

if __name__ == "__main__":
    app.run()