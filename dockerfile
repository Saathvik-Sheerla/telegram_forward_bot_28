FROM python:3.11-slim

COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]