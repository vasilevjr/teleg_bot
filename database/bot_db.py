# SQL - Structured Querry Language
# СУБД - Система Управления Базой Данных

import sqlite3 as sl

def sql_create():
    global db, cursor
    db = sl.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена! ")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "telegram_id INTEGER UNIQUE,"
               "username VARCHAR (100),"
               "full_name VARCHAR (150),"
               "phone_number INTEGER,"
               "city VARCHAR (150),"
               "address TEXT)")


    db.commit()


sql_create()