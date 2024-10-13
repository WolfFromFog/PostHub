import sqlite3


class CFDataBasePosts:
    def __init__(self):
        self.db = sqlite3.connect('DataBase/data_base/users.sql', check_same_thread=False)
        self.cur = self.db.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nickname TEXT,
            password TEXT,
            date TEXT
        )
        """)
        self.db.commit()

    def getUser(self, user_id):
        self.cur.execute(f"SELECT * FROM users WHERE user_id = '{str(user_id)}'")
        find_user = self.cur.fetchone()

        if find_user is not None:
            return {
                "user_id": find_user[0],
                "nickname": find_user[1],
                "date": find_user[3],
            }
        else:
            return {
                "error": {
                    "message": "Простите, но нам не удалось найти пользователя :(",
                    "code": "404"
                }
            }
