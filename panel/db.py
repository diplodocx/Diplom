from db_connect import connect_db
from models import Config, Button, Scenario, Var


def get(table_name):
    conn = connect_db()
    cur = conn.cursor()
    select_statement = f"""
                SELECT * FROM {table_name};
                """
    cur.execute(select_statement)
    res = cur.fetchall()
    return res


def get_first(cur, var, table_name):
    select_statement = f"""
            SELECT MAX({var}) FROM {table_name};
            """
    cur.execute(select_statement)
    max_id = cur.fetchone()[0]
    cur_id = max_id + 1 if max_id else 1
    return cur_id


# config
def get_configs():
    return get('Config')


def create_config(config: Config):
    conn = connect_db()
    cur = conn.cursor()
    cur_id = get_first(cur, 'config_id', 'Config')
    insert_statement = """
        INSERT INTO Config (config_id, variable_id, button_id) VALUES (%s, %s, %s);
        """
    cur.execute(insert_statement, (cur_id, config.var_id, config.button_id))
    conn.commit()
    conn.close()


# button
def create_button(button: Button):
    conn = connect_db()
    cur = conn.cursor()
    cur_id = get_first(cur, 'button_id', 'Button')
    insert_statement = """
        INSERT INTO Button (button_id, button_name, scen_id) VALUES (%s, %s, %s);
        """
    cur.execute(insert_statement, (cur_id, button.button_name, button.scen_id))
    conn.commit()
    conn.close()


def get_buttons():
    return get('Button')


# scenario
def create_scen(scen: Scenario):
    conn = connect_db()
    cur = conn.cursor()
    cur_id = get_first(cur, 'scen_id', 'Scenario')
    insert_statement = """
        INSERT INTO Scenario (scen_id, scen_desc, scen_name) VALUES (%s, %s, %s);
        """
    cur.execute(insert_statement, (cur_id, scen.scen_desc, scen.scen_name))
    conn.commit()
    conn.close()


def get_scens():
    return get('Scenario')


# variable
def create_var(var: Var):
    conn = connect_db()
    cur = conn.cursor()
    cur_id = get_first(cur, 'variable_id', 'Var')
    insert_statement = """
        INSERT INTO Var (variable_id, var_name, var_type) VALUES (%s, %s, %s);
        """
    cur.execute(insert_statement, (cur_id, var.var_name, var.var_type))
    conn.commit()
    conn.close()


def get_vars():
    return get('Var')
