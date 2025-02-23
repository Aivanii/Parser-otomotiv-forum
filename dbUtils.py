import sqlite3

def createUserDb():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT,
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

def insertUser(user_data):

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO users (user_id, Old_Name, Name, Password, User_URL, Registration_Date, Message_Count, Reaction_Count, Last_Activity, Status, Role) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''

    cursor.execute(insert_query, (
        user_data['ID'],
        user_data['Old_Name'],
        user_data['Name'],
        user_data['Password'],
        user_data['User_URL'],
        user_data['Registration_Date'],
        user_data['Message_Count'],
        user_data['Reaction_Count'],
        user_data['Last_Activity'],
        user_data['Status'],
        user_data['Role']
    ))

    conn.commit()
    conn.close()

    print("Пользователь успешно добавлен!")
    print(user_data)

def createMessagesDB():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        path_avatar TEXT,
        path_files TEXT,
        urls TEXT,
        date TEXT,
        text TEXT,
        message_id TEXT,
        likes_user_id TEXT,
        user_id TEXT,
        forum_id TEXT,
        reply_message_id TEXT
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def insertMessage(message_data):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    
    insert_query = '''
    INSERT INTO users (
        Path_Avatar, Path_Files, Urls, Date, Text,
        message_id, Likes_User_ID, User_ID, Forum_ID, Reply_Message_ID
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    
    for item in message_data:
        cursor.execute(insert_query, (
            item['path_avatar'],
            item['path_files'],
            item['urls'],
            item['date'],
            item['text'],
            item['id'],
            item['likes_user_id'],
            item['user_id'],
            item['forum_id'],
            item['reply_message_id']
        ))

    conn.commit()
    conn.close()

def createCategoriesDB():
    conn = sqlite3.connect('categories.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        category_id TEXT,
        Name TEXT,
        Description TEXT,
        Sub_forum_count INTEGER,
        Sub_forum_id_list TEXT
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def insertCategories(categories_data):
    conn = sqlite3.connect('categories.db')
    cursor = conn.cursor()
    
    insert_query = '''
    INSERT INTO users (
        category_id, Name, Description, Sub_forum_count, Sub_forum_id_list
    ) VALUES (?, ?, ?, ?, ?);
    '''

    for category_data in categories_data:
        cursor.execute(insert_query, (
            category_data['Id'],
            category_data['Name'],
            category_data['Description'],
            category_data['Sub_forum_count'],
            category_data['Sub_forum_id_list']
        ))

    conn.commit()
    conn.close()
