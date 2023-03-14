import sqlite3
from dotenv.main import load_dotenv
import os
import mysql.connector
load_dotenv()

con = sqlite3.connect('data.db',check_same_thread=False)
cur = con.cursor()

def create_table(table_name):
    query = f"CREATE TABLE IF NOT EXISTS {table_name} (chat_id INT PRIMARY KEY NOT NULL, email TEXT UNIQUE NOT NULL, enroll INT UNIQUE NOT NULL,sname TEXT NOT NULL,reg INT UNIQUE NOT NULL,phone INT UNIQUE NOT NULL)"
    try:
        cur.execute(query)
        print('table created')
    except:
        print('error')

create_table('info')

def show_all_table():
    cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
    data = cur.fetchall()
    return data

# print(show_all_table())

def table_schema(table_name):
    cur.execute(f"""PRAGMA table_info({table_name})""")
    data = cur.fetchall()
    return data

# print(table_schema('info'))

def insertion_table(table_name,data_tuple):
    try:
        query = f"INSERT INTO {table_name} VALUES {data_tuple}"
        cur.execute(query)
        con.commit()
        print("sucessfully inserted")
        return "sucessfully inserted"
    except:
        print("error insertion")
        return "error insertion, tuple format error OR user already exist ,use /delete to add again"

# data = (12345,"hash@gmail.com",1200,"harsh",3040,9100)
# insertion_table('info',data)

def table_data_deletion(chat_id):
    try:
        cur.execute(f"DELETE from info WHERE chat_id = {chat_id}")
        con.commit()
        return "deleted sucessfully"
    except:
        return "user not found , add first"

def view_data(table_name):
    query = f"SELECT * FROM {table_name}"
    cur.execute(query)
    data = cur.fetchall()
    return data

def view_chatid_data(chat_id):
    query = f"SELECT * FROM info WHERE chat_id = {chat_id}"
    cur.execute(query)
    data = cur.fetchall()
    data=data[0][1:]
    return data

def local_mysql_query(query):
    con = sqlite3.connect('data.db',check_same_thread=False)
    cur = con.cursor()

    cur.execute(query)
    con.commit()
    data = cur.fetchall()
    return data


#online mysql
def online_mysql_insertion(data_tuple):
    connection = mysql.connector.connect(
        host = os.environ['mysqlhost'],
        user = os.environ['mysqluser'],
        password=os.environ['mysqlpass'],
        database = os.environ['mysqldb']
    )
    cursor = connection.cursor()
    query = f"insert into info values {data_tuple}"
    cursor.execute(query)
    connection.commit()

def online_mysql_query(query):
    connection = mysql.connector.connect(
        host = os.environ['mysqlhost'],
        user = os.environ['mysqluser'],
        password=os.environ['mysqlpass'],
        database = os.environ['mysqldb']
    )
    cursor = connection.cursor()
    cursor.execute(query)
    try:
        connection.commit()
    except:
        data = cursor.fetchall()
        return data
    return "no commit"

