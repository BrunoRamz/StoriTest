import os
import pandas as pd
import smtplib


from db import DB
from datetime import datetime
from collections import Counter
from email.message import EmailMessage
from dotenv import (
    load_dotenv,
    find_dotenv
)


load_dotenv(find_dotenv())


class Transaction():
    def __init__(self):
        self.csv_file = pd.read_csv(os.getenv('FILE_NAME'))
        self.total_balance = 0
        self.debit_amount = 0
        self.credit_amout = 0
        self.debit_amout_counter = 0
        self.credit_amout_counter = 0
        self.debit_amount_average = 0
        self.credit_amout_average = 0
        self.email_body = ''
        self.html_text = ''
        self.email = os.getenv('EMAIL')
        self.host = os.getenv('HOST')
        self.port = int(os.getenv('PORT'))
        self.password = os.getenv('PASSWORD')

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
        self.email_message = EmailMessage()
        self.email_message['Subject'] = 'Account Balance'
        self.email_message['From'] = self.email
        self.email_message['To'] = self.email

        for key_month, value_month in self.months_collection.items():
            self.email_body += (
                f"Number of transactions in {key_month}: {value_month}\n"
            )
            self.email_body += '\t'

        self.text = f"""\
            Hello:
            We hope you are fine! Here there is your Account Balance\n
            Total Balance is: {self.total_balance}
            {self.email_body}
        """
        self.text += \
            f"Average debit Amount: {self.debit_amount_average}\n"
        self.text += \
            f"\tAverage credit Amount: {self.credit_amout_average}"

        self.email_message.set_content(self.text)

        with smtplib.SMTP_SSL(self.host, self.port) as smtp:
            smtp.login(self.email, self.password)
            smtp.send_message(self.email_message)
            print("Successfully sent email")


transaction = Transaction()
transaction.process_transaction()
transaction.send_summary_to_email()
