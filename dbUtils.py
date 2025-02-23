import sqlite3


#================================================================
#===================USERS========================================
#================================================================
def createUserDb():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        ID TEXT,
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
    INSERT INTO users (ID, Old_Name, Name, Password, User_URL, Registration_Date, Message_Count, Reaction_Count, Last_Activity, Status, Role) 
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



#================================================================
#===================Messages=====================================
#================================================================
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
        id TEXT,
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
    
    # Подготовка SQL запроса для вставки данных
    insert_query = '''
    INSERT INTO users (
        Path_Avatar, Path_Files, Urls, Date, Text,
        ID, Likes_User_ID, User_ID, Forum_ID, Reply_Message_ID
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    
    # Вставка данных
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