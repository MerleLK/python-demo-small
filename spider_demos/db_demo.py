# coding=utf-8

import MySQLdb
import spider_setting

HOST = spider_setting.HOST
USER = spider_setting.USER
PASSWORD = spider_setting.PASSWORD
DB_NAME = spider_setting.DB


class MyDatabase(object):

    def __init__(self):
        self.db = MySQLdb.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            db=DB_NAME,
            charset='utf8',
        )
        # self.cur = self.db.cursor()

    def create_table(self):
        cur = self.db.cursor()
        sql = """
        CREATE TABLE music_info(
          id INTEGER PRIMARY KEY,
          name VARCHAR(255) NOT NULL ,
          music_id VARCHAR(255) NOT NULL ,
          singer VARCHAR(255) NOT NULL ,
          total INTEGER 
        )
        """
        m = cur.execute(sql)
        cur.close()
        if m != 0:
            return False
        else:
            return True

    def insert_data(self, name, music_id, singer, total):
        cur = self.db.cursor()
        sql = """
        INSERT INTO music_info VALUES (%s, %s, %s, %s, %s)
        """
        m = cur.execute(sql, (0, name, music_id, singer, total))
        cur.close()
        self.db.commit()
        return m

    def select_data(self):
        pass

    def _close(self):
        # 关闭数据库连接
        self.db.close()


db = MyDatabase()


if __name__ == '__main__':
    db.create_table()
    # print(db.insert_data("TEST", "123", "merle", 123))
