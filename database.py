import sqlite3

class Database:

    def __init__(self, db_name = "tracker.db"):
        self.db_name = db_name

    def create_table(self):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query = "create table if not exists Tracker(id integer primary key , title text not null, priority text not null)"

            cursor.execute(query)

            conn.commit()
