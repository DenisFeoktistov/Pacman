import sqlite3
import datetime as dt


class DataBaseResponder:
    def __init__(self):
        self.db_name = "casino_db.db"
        self.con = sqlite3.connect(self.db_name)

    def get_time_list(self):
        cur = self.con.cursor()

        result = cur.execute("""SELECT * FROM records""").fetchall()

        return sorted(list(map(lambda x: dt.time(second=x), result)))

    def add_time_to_table(self, time):
        cur = self.con.cursor()

        cur.execute("""INSERT into records VALUES(?)""", (time.seconds))
