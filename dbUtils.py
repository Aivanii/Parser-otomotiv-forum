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
        path_files TEXT,
        urls TEXT,
        date TEXT,
        text TEXT,
        message_id TEXT,
        likes_user_id TEXT,
        user_id TEXT,
        theme_id TEXT,
        reply_message_id TEXT,
        user_mention_id TEXT,
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
        Path_Files, Urls, Date, Text,
        message_id, Likes_User_ID, User_ID, Theme_ID, Reply_Message_ID,
        user_mention_id
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    
    for item in message_data:
        cursor.execute(insert_query, (
            item['path_files'],
            item['urls'],
            item['date'],
            item['text'],
            item['id'],
            item['likes_user_id'],
            item['user_id'],
            item['theme_id'],
            item['reply_message_id'],
            item['user_mention_id']
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

def categoriesId():
    conn = sqlite3.connect('categories.db')
    cursor = conn.cursor()

    select_query = '''
        SELECT category_id from users
        '''
    req = cursor.execute(select_query).fetchall()

    conn.close()
    return req
def createTopicsDB():
    conn = sqlite3.connect('topics.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        theme_id TEXT,
        parent_forum_id TEXT,
        creator_id TEXT,
        create_date TEXT,
        views TEXT,
        answers TEXT
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def insertTopics(topics_data):
    conn = sqlite3.connect('topics.db')
    cursor = conn.cursor()
    
    insert_query = '''
    INSERT INTO users (
        name, theme_id, parent_forum_id, creator_id, create_date, views, answers
    ) VALUES (?, ?, ?, ?, ?, ?, ?);
    '''

    for topic_data in topics_data:
        cursor.execute(insert_query, (
            topic_data['name'],
            topic_data['theme_id'],
            str(topic_data['parent_forum_id']),
            topic_data['creator_id'],
            topic_data['create_date'],
            topic_data['views'],
            topic_data['answers']
        ))

    conn.commit()
    conn.close()


def createForumsDB():
    conn = sqlite3.connect('forums.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        forum_id INTEGER PRIMARY KEY,
        name TEXT,
        themes_count TEXT,
        message_count TEXT
        
    );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()


def insertForums(forums_data):
    conn = sqlite3.connect('forums.db')
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO users (
        forum_id, name, themes_count, message_count
    ) VALUES (?, ?, ?, ?);
    '''

    for forum_data in forums_data:
        cursor.execute(insert_query, (
            forum_data['forum_id'],
            forum_data['name'],
            forum_data['themes_count'],
            forum_data['message_count']
        ))

    conn.commit()
    conn.close()

def forumsId():
    conn = sqlite3.connect('forums.db')
    cursor = conn.cursor()

    select_query = '''
        SELECT forum_id from users
        '''
    req = cursor.execute(select_query).fetchall()

    conn.close()
    return req
