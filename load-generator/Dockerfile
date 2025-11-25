FROM python:3.11-slim

WORKDIR /app

COPY load.py /app/load.py
RUN pip install psycopg2-binary

CMD ["python", "load.py"]
