import sqlite3


class CFDataBaseCategories:
    def __init__(self):
        self.db = sqlite3.connect('DataBase/data_base/categories.sql', check_same_thread=False)
        self.cur = self.db.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            category_name TEXT
        )
        """)
        self.db.commit()

    def getCategories(self):
        self.cur.execute("SELECT * FROM categories")

        find_categories = self.cur.fetchall()

        _temp_categories = []

        for category in find_categories:
            _temp_categories.append({
                "id": category[0],
                "name": category[1]
            })

        return _temp_categories
