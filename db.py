import sqlite3
import os


from dotenv import (
    load_dotenv,
    find_dotenv
)


load_dotenv(find_dotenv())


class DB:
    def __init__(self):
        self.database = os.getenv('DATABASE')
    
    def start_database(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transaction
            ([transaction_id] INTEGER PRIMARY KEY,
             [date] TEXT,
             [debit_amount] FLOAT,
             [redit_amount] FLOAT,
             [total_balance] FLOAT
            )
            """
        )
    
    def insert_data(self):
        self.cursor.executemany(
            """
            INSERT INTO transaction(?,?,?,?,?)
            """
        )
        