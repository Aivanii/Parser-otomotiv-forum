import sqlite3

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    ID TEXT PRIMARY KEY,
    Old_Name TEXT,
    Name TEXT,
    Password TEXT,
    User_URL TEXT,
    Registration_Date TEXT,
    Message_Count TEXT,
    Reaction_Count TEXT,
    Last_Activity TEXT,
    Status TEXT,
    Role TEXT
);
'''
cursor.execute(create_table_query)

conn.commit()
conn.close()

print("База данных и таблица успешно созданы!")
