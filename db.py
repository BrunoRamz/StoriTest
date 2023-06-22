import sqlite3
import os


from dotenv import (
    load_dotenv,
    find_dotenv
)


load_dotenv(find_dotenv())


class DB:
    def start_database(self):
        self.connection = sqlite3.connect(os.getenv('DATABASE'))
        self.cursor = self.connection.cursor()
        print("Connection Established...")

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions
            ([transactions_id] INTEGER PRIMARY KEY,
             [date] TEXT,
             [transaction] FLOAT
            )
            """
        )

    def store_data(self):
        pass

    def show_table(self):
        pass

    def drop_table(self):
        self.cursor.execute(
            """
            DROP TABLE IF EXISTS transactions
            """
        )
