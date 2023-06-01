
import random
import sqlite3 as sl



def sql_create():
    global db, cursor
    db = sl.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "full_name VARCHAR (150),"
               "phone_number INTEGER,"
               "city VARCHAR (150),"
               "address TEXT)")

    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO anketa "
            "(full_name, phone_number, city, address) "
            "VALUES (?, ?, ?, ?)",
            tuple(data.values())
        )
    db.commit()

async def sql_command_random():
    users = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(users)
    return random_user

async def sql_command_delete(id: str):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id,))
    db.commit()


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()

