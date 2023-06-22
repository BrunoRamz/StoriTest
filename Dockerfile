FROM Ubuntu
FROM python:3.8-slim-buster

RUN sudo apt-get update && \
    sudo apt-get upgrade

WORKDIR /storitest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "process_transactions.py"]