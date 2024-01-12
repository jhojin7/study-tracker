from config import Config
import json
import pymysql
from typing import Dict, List, Union, Optional


class DB:
    def __init__(self, config):
        self.connection = pymysql.connect(**config)
        self.cursor = self.connection.cursor()

    def myquery(self):
        # self.cursor.execute("drop table if exists submission;")
        self.cursor.execute(
            """
            create table if not exists submission (
                sid int primary key, uid varchar(100),
                pid int, result varchar(100), timestamp int,
                index time_idx (timestamp)
            );
            """)

        for uid in Config.uids:
            subs = json.load(open(f"{uid}.json", 'r'))
            self.cursor.executemany(
                """insert into submission (sid, uid, pid, result, timestamp)
                values (%(sid)s, %(uid)s, %(pid)s, %(result)s, %(timestamp)s)""",
                subs
            )
            self.connection.commit()

        self.cursor.execute("select * from submission")
        res = self.cursor.fetchall()
        print(*res, sep='\n')


if __name__ == "__main__":
    db = DB(config=Config.db_local)
    db.myquery()
