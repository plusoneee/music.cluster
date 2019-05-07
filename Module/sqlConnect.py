
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

class SQLConnect(object):
    def __init__(self, table_name):
        self.host = os.getenv("SQL_HOST")
        self.user = os.getenv("SQL_USER_NAME")
        self.passwd = os.getenv("SQL_PASSWORD")
        self.database = os.getenv("DATABASE_NAME")

        self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.database)
        self.cursor = self.db.cursor()
        self.table_name = table_name

    def insert_into_table(self, data_dic):
        try:
            insert_query = "INSERT INTO {tablename} ({columns}) VALUES {values};" .format(
                tablename=self.table_name,
                columns=', '.join(data_dic.keys()),
                values=tuple(data_dic.values())
            )
            print(insert_query)
            self.cursor.execute(insert_query)
            self.db.commit()
            print("Inserted completely")
        except:
            print('Duplicate')

    def delete_table_data_from_id(self, id):
        '''
        For Example: 
            table.delete_table_data_from_id('6WeDO4GynFmK4OxwkBzMW8')
        '''
        delete_query = "DELETE FROM {tablename} where id = '{values}';" .format(
            tablename=self.table_name,
            values=id
        )
        print(delete_query)
        self.cursor.execute(delete_query)
        self.db.commit()

    def create_table(self, col_name_list):
        self.cursor.execute("CREATE TABLE {} (name VARCHAR(255), url VARCHAR(255), no VARCHAR(255))".format(self.table_name))

    def create_db(self, db_name):
        self.cursor.execute("CREATE DATABASE {}".format(db_name))
    