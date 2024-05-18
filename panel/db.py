from db_connect import connect_db
from models import Config, Button, Scenario, Var


# config
def get_configs():
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
            SELECT * FROM Config;
            """
    cur.execute(select_statement)
    configs = cur.fetchall()
    return configs
    # return [
    #     {'id': 1, 'button_name': 'button_floor_move_1', 'variable': 'set_lift_1_floor'},
    #     {'id': 2, 'button_name': 'button_floor_move_2', 'variable': 'set_lift_2_floor'}
    # ]


def create_config(config: Config):
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
        SELECT MAX(config_id) FROM Config;
        """
    cur.execute(select_statement)
    max_id = cur.fetchone()[0]
    cur_id = max_id + 1 if max_id else 1
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
    select_statement = """
        SELECT MAX(button_id) FROM Button;
        """
    cur.execute(select_statement)
    max_id = cur.fetchone()[0]
    cur_id = max_id + 1 if max_id else 1
    insert_statement = """
        INSERT INTO Button (button_id, button_name, scen_id) VALUES (%s, %s, %s);
        """
    cur.execute(insert_statement, (cur_id, button.button_name, button.scen_id))
    conn.commit()
    conn.close()


def get_buttons():
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
                SELECT * FROM Button;
                """
    cur.execute(select_statement)
    buttons = cur.fetchall()
    return buttons


# scenario
def create_scen(scen: Scenario):
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
        SELECT MAX(scen_id) FROM Scenario;
        """
    cur.execute(select_statement)
    max_id = cur.fetchone()[0]
    cur_id = max_id + 1 if max_id else 1
    insert_statement = """
        INSERT INTO Scenario (scen_id, scen_desc, scen_name) VALUES (%s, %s, %s);
        """
    cur.execute(insert_statement, (cur_id, scen.scen_desc, scen.scen_name))
    conn.commit()
    conn.close()


def get_scens():
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
                SELECT * FROM Scenario;
                """
    cur.execute(select_statement)
    scens = cur.fetchall()
    return scens


# variable
def create_var(var: Var):
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
        SELECT MAX(variable_id) FROM Var;
        """
    cur.execute(select_statement)
    max_id = cur.fetchone()[0]
    cur_id = max_id + 1 if max_id else 1
    insert_statement = """
        INSERT INTO Var (variable_id, var_name, var_type) VALUES (%s, %s, %s);
        """
    cur.execute(insert_statement, (cur_id, var.var_name, var.var_type))
    conn.commit()
    conn.close()


def get_vars():
    conn = connect_db()
    cur = conn.cursor()
    select_statement = """
                SELECT * FROM Var;
                """
    cur.execute(select_statement)
    vars = cur.fetchall()
    return vars
