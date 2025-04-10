import sqlite3
conn = sqlite3.connect("profesores-c-usuarios.db")
cursor = conn.cursor() #creating the cursor for selecting/inserting/fetching
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT
    )
''')
conn.commit()
conn.close()
print("THE TABLE WAS SUCCESFULLY CREATED")