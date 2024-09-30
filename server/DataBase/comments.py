import sqlite3


class CFDataBaseComments:

    def __init__(self):
        self.db = sqlite3.connect('DataBase/data_base/comments.sql', check_same_thread=False)
        self.cur = self.db.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS comments (
            comment_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            post_id,
            nickname TEXT,
            text TEXT,
            date INTEGER
        )
        """)
        self.db.commit()

    def getComments(self, post_id):
        self.cur.execute(f"SELECT * FROM comments WHERE post_id = '{str(post_id)}' ORDER BY date DESC")
        find_post = self.cur.fetchall()

        _temp_comments = []
        for comment in find_post:
            _temp_comments.append({
                "id": comment[0],
                "post_id": comment[1],
                "nickname": comment[2],
                "text": comment[3],
                "date": comment[4]
            })

        return _temp_comments

    def addComment(self, comment_info):
        self.cur.execute("INSERT INTO comments (post_id, nickname, text, date) VALUES (?, ?, ?, ?)",
                         (comment_info['post_id'],
                          comment_info['nickname'],
                          comment_info['text'],
                          comment_info['date']))
        self.db.commit()

        return self.getComments(comment_info['post_id'])
