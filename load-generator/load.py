import psycopg2
import random
import time
import os

DB_HOST = os.environ.get("DB_HOST", "postgres")
DB_NAME = os.environ.get("DB_NAME", "observabilidade")
DB_USER = os.environ.get("DB_USER", "admin")
DB_PASS = os.environ.get("DB_PASS", "admin123")

def get_conn():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

def ensure_activity():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM logs")
        cnt = cur.fetchone()[0]
        if cnt < 10:
            cur.executemany("INSERT INTO logs(valor) VALUES (%s)", [(random.randint(1,1000),) for _ in range(10)])
            conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("ensure_activity error:", e)

def random_op():
    try:
        conn = get_conn()
        cur = conn.cursor()
        op = random.choice(["insert","select","update","delete"])
        if op == "insert":
            cur.execute("INSERT INTO logs(valor) VALUES (%s)", (random.randint(1,9999),))
        elif op == "select":
            cur.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 10")
            _ = cur.fetchall()
        elif op == "update":
            cur.execute("UPDATE logs SET valor = valor + 1 WHERE id IN (SELECT id FROM logs LIMIT 5)")
        else:
            cur.execute("DELETE FROM logs WHERE id IN (SELECT id FROM logs LIMIT 1)")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("op error:", e)

if __name__ == "__main__":
    ensure_activity()
    while True:
        random_op()
        time.sleep(random.uniform(0.5, 2.5))
