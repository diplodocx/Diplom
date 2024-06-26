import psycopg2
from db_connect import connect_db
from datetime import datetime


def get_command(button_name: str, param):
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
        SELECT var_name FROM Config
        INNER JOIN Var
        ON Var.variable_id = Config.variable_id
        INNER JOIN Button
        ON Button.button_id = Config.button_id
        WHERE button_name = (%s);
        """
    cur.execute(select_statement, (button_name, ))
    var = cur.fetchone()[0]
    conn.close()
    print(var)
    return (var, param)


def insert_action_data(action_type_id: int):
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
    SELECT MAX(log_id) FROM Analytics;
    """
    cur.execute(select_statement)
    max_id = cur.fetchone()[0]
    cur_id = max_id + 1 if max_id else 1
    insert_statement = """
    INSERT INTO Analytics VALUES (%s, %s, %s)
    """
    cur.execute(insert_statement, (cur_id, datetime.now(), action_type_id))
    conn.commit()
    conn.close()

insert_action_data(1)
