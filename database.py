import sqlite3

class Database:

    def __init__(self, db_name = "tracker.db"):
        self.db_name = db_name

    def create_table(self):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query = "create table if not exists Tracker(id integer primary key autoincrement, title text not null, priority text not null)"

            cursor.execute(query)

            conn.commit()

    def add_task(self, title, priority_text):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query = "insert into Tracker(title, priority_text) values(?, ?)"

            cursor.execute(query, (title, priority_text))

            conn.commit()

    def edit_task(self, sl_no, title, priority_text):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query ="update Tracker set title, priority_text = ? , ? where id = ?"

            cursor.execute(query, (sl_no, title, priority_text))

            conn.commit()

    def delete_task(self, sl_no):

         with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query ="delete from Tracker where id = ?"

            cursor.execute(query, (sl_no,))

            conn.commit()

def show_tasks(self):

    with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query ="select id, title, priority_text from Tracker"

            cursor.execute(query)

            conn.commit()