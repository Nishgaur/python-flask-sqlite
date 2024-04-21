import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               id INTEGER PRIMARY KEY,
                               username TEXT UNIQUE,
                               email TEXT UNIQUE
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                               id INTEGER PRIMARY KEY,
                               title TEXT,
                               content TEXT,
                               author_id INTEGER,
                               FOREIGN KEY(author_id) REFERENCES users(id)
                            )''')

    def insert_user(self, username, email):
        self.cursor.execute('''INSERT INTO users (username, email) VALUES (?, ?)''', (username, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_post(self, title, content, author_id):
        self.cursor.execute('''INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)''', (title, content, author_id))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_posts_by_author(self, author_id):
        self.cursor.execute('''SELECT * FROM posts WHERE author_id = ?''', (author_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db_manager = DatabaseManager('sample.db')
    db_manager.create_tables()

    # Inserting users
    user1_id = db_manager.insert_user('user1', 'user1@example.com')
    user2_id = db_manager.insert_user('user2', 'user2@example.com')

    # Inserting posts
    post1_id = db_manager.insert_post('Post 1', 'Content of post 1', user1_id)
    post2_id = db_manager.insert_post('Post 2', 'Content of post 2', user2_id)

    # Retrieving posts by author
    user1_posts = db_manager.get_posts_by_author(user1_id)
    print("Posts by user 1:")
    for post in user1_posts:
        print(post)

    db_manager.close()
