FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && rm requirements.txt

COPY /app /app

CMD ["python", "main.py"]
