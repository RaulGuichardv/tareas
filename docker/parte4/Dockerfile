FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
COPY app.py .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
