import sqlite3


class CFDataBasePosts:
    def __init__(self):
        self.db = sqlite3.connect('DataBase/data_base/posts.sql', check_same_thread=False)
        self.cur = self.db.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS posts (
            post_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            user_nickname,
            header TEXT,
            main_text TEXT,
            image TEXT,
            date INTEGER,
            likes INTEGER DEFAULT 0,
            dislikes INTEGER DEFAULT 0,
            categories TEXT
        )
        """)
        self.db.commit()

    def getPosts(self):
        self.cur.execute("SELECT * FROM posts ORDER BY date DESC")
        find_post = self.cur.fetchall()

        _temp_posts = []

        for post in find_post:
            _temp_posts.append({
                "post_id": post[0],
                "user_nickname": post[1],
                "header": post[2],
                "main_text": post[3],
                "image": post[4],
                "date": post[5],
                "likes": post[6],
                "dislikes": post[7],
                "categories": post[8]
            })

        return _temp_posts

    def getPost(self, post_id):
        self.cur.execute(f"SELECT * FROM posts WHERE post_id = '{str(post_id)}'")
        find_post = self.cur.fetchone()

        if find_post is not None:
            return {
                "post_id": find_post[0],
                "user_nickname": find_post[1],
                "header": find_post[2],
                "main_text": find_post[3],
                "image": find_post[4],
                "date": find_post[5],
                "likes": find_post[6],
                "dislikes": find_post[7],
                "categories": find_post[8]
            }
        else:
            return {
                "error": {
                    "message": "Простите, но нам не удалось найти статью :(",
                    "code": "404"
                }
            }

    def addPost(self, post_info):
        try:
            self.cur.execute("INSERT INTO posts "
                             "(user_nickname, header, main_text, image, date, categories) "
                             "VALUES (?, ?, ?, ?, ?, ?)",
                             (post_info['user_nickname'],
                              post_info['header'],
                              post_info['main_text'],
                              post_info['image'],
                              post_info['date'],
                              post_info['categories']))
            self.db.commit()

            return True
        except Exception as e:
            return e
