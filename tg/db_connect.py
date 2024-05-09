import psycopg2


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="YourUsername",
        password="YourPassword"
    )
    return conn


def disconnect_db(conn: psycopg2.connection):
    conn.close()
    return 'Connection closed'
