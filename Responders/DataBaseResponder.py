import sqlite3
import datetime as dt


class DataBaseResponder:
    def __init__(self):
        self.db_name = "records.db"
        self.con = sqlite3.connect(self.db_name)

    def get_time_list(self):
        cur = self.con.cursor()

        result = cur.execute("""SELECT * FROM records""").fetchall()

        return sorted(list(map(lambda x: dt.time(minute=(x[0] // 60) % 60, second=x[0] % 60), result)))

    def add_time_to_table(self, time1):
        cur = self.con.cursor()
        cur.execute("""INSERT into records(time) VALUES(?)""", (int(time1.second),))

        self.con.commit()
