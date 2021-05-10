import sqlite3
import os

def get_list_of_files(dir_name):
    list_of_file = os.listdir(dir_name)
    all_files = list()
    for entry in list_of_file:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
                
    return all_files

def delete_all_courses():
    conn = sqlite3.connect('courses.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM courses")
    conn.commit()
    conn.close()


delete_all_courses()

dir_name = os.path.dirname(__file__)
main_path = os.path.join(dir_name, 'scrapping_scripts')
list_of_files = get_list_of_files(main_path)
for file_path in list_of_files:
    print("Wykonuję skrypt" + file_path)
    exec(open(file_path).read())