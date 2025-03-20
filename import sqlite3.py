import sqlite3

def create_table():
    conn=sqlite3.connect("studinfo.db")
    cursor=conn.cursor()
    cursor.execute(""" 
                create table  if not exists students (
                id integer primary key autoincrement,
                name TEXT ,
                age integer,
                marks integer)
                """)
    conn.commit()
    conn.close()
    
def insert_students():
    students=[
        ("Aryan", 22, 70),
        ("Nikhil", 21, 74),
        ("khushal", 23, 75),
        ("Rahul", 22, 81)
    ]
    conn=sqlite3.connect("studinfo.db")
    cursor=conn.cursor()
    cursor.executemany("insert into students (name,age,marks) values (?, ?, ?)", students)
    conn.commit()
    conn.close()
    
def fetch_students():
    conn=sqlite3.connect("studinfo.db")
    cursor=conn.cursor()
    cursor.execute("select * from students")
    records=cursor.fetchall()
    for row in records:
        print(row)
    conn.close()
    
def update_student(student_id, new_marks):
    conn=sqlite3.connect("studinfo.db")
    cursor=conn.cursor()
    cursor.execute("update students set marks = ? where id = ?", (new_marks, student_id))
    conn.commit()
    conn.close()
    
def delete_student(student_id):
    conn=sqlite3.connect("studinfo.db")
    cursor=conn.cursor()
    cursor.execute("delete from students where id = ?",(student_id,))
    conn.commit()
    conn.close()
    
if __name__=="__main__":
   create_table()
   insert_students()
   fetch_students()
   update_student(1,80)
   delete_student(2)
   fetch_students()
   