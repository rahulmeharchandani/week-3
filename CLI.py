import sqlite3
def contact_table():
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("""
        create table if not exists contacts(
        id integer primary key,
        name text,
        phone text,
        email text
        )
        """)
    conn.commit()
    conn.close()
    
def add_contact(name, phone, email):
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("insert into contacts (name, phone, email) values(?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    
def update_contact(contact_id, name, phone, email):
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("update contacts set name = ?, phone = ?, email = ? where id = ?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()
    
def delete_contact(contact_id):
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("delete from contacts where name like ?",(contact_id,))
    conn.commit()
    conn.close()
    
def search_contact(name):
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("select * from contacts where name like ?",(f"%{name}%",))
    records=cursor.fetchall()
    for row in records:
        print(row)
    conn.close()
    
if __name__=="__main__":
    contact_table()
    add_contact("Rahul", "8745874598", "rahul@gmail.com" )
    search_contact("Rahul")
    update_contact(1, "Rahul Sharma", "9876543210", "rahulsharma@gmail.com")
    delete_contact(1)
        
    