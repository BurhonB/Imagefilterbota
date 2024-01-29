import sqlite3 as sql


async def sql_connector():
    con = sql.connect('bot.db')
    cur = con.cursor()
    return con, cur


async def create_tables():
    con, cur = await sql_connector()

    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id BIGINT,
        username VARCHAR(255)
    )''')


async def add_user(user_id: int, username: str):
    con, cur = await sql_connector()

    user = cur.execute('''SELECT * FROM users WHERE user_id = ?''', (user_id,)).fetchone()

    if not user:
        cur.execute('''INSERT INTO users(user_id, username) VALUES(?,?)''', (user_id, username))

    con.commit()


async def get_all_users():
    con, cur = await sql_connector()

    users = cur.execute("SELECT COUNT(*) FROM users").fetchone()
    return users[0]


