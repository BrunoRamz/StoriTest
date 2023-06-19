import os
import pandas as pd
import smtplib


from datetime import datetime
from collections import Counter
from email.mime.text import MIMEText
from dotenv import (
    load_dotenv,
    find_dotenv
)


class Transaction:
    def __init__(self, csv_file):
        self.csv_file = pd.read_csv(csv_file)
        self.total_balance = 0
        self.debit_amount = 0
        self.credit_amout = 0
        self.debit_amout_counter = 0
        self.credit_amout_counter = 0
        self.debit_amount_average = 0
        self.credit_amout_average = 0
        self.sender = 'testSender@email.com'
        self.receivers = ['testReciver@.com']
        self.localhost = 'localhost'
        self.port = 1025

    def process_transaction(self):
        self.date_column = self.csv_file.get(
            'Date', 'Key Not Found'
        )
        self.transaction_column = self.csv_file.get(
            'Transaction', 'Key Not Found'
        )
        self.date_list = [
            datetime.strptime(date, '%m/%d').strftime(
            '%b') for date in self.date_column
        ]
        self.months_collection = dict(Counter(self.date_list))
        self.total_balance = sum(self.transaction_column)

        for transaction in self.transaction_column:
            if transaction < 0:
                self.debit_amount += transaction
                self.debit_amout_counter += 1
            elif transaction > 0:
                self.credit_amout += transaction
                self.credit_amout_counter += 1

        self.debit_amount_average = self.debit_amount/self.debit_amout_counter
        self.credit_amout_average = self.credit_amout/self.credit_amout_counter

    def send_summary_to_email(self):

        message = f"""
            From: BankTest <{self.sender}>
            To: PersonTest <{self.receivers}>
            Subject: Total Balance Account

            Total Balance is: {self.total_balance}

        """
        for key_month, value_month in self.months_collection.items():
            message += f"Number of transactions in {key_month}: {value_month}\n"
        
        message += f"Average debit Amount: {self.debit_amount_average}\n"
        message += f"Average credit Amount: {self.credit_amout_average}"
        print(message)
        """
        try:
            smtpObj = smtplib.SMTP('localhost', 1025)
            smtpObj.sendmail(self.sender, self.receivers, message)
            print("Successfully sent email")
        except Exception as SMTPException:
            print(SMTPException)
        """


csv_file = 'txns.csv'

transaction = Transaction(csv_file)
transaction.process_transaction()
transaction.send_summary_to_email()