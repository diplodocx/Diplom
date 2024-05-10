DROP TABLE IF EXISTS Scenario;
CREATE TABLE Scenario (
    scen_id SERIAL,
    scen_desc TEXT,
    scen_name TEXT,
    PRIMARY KEY (scen_id)
);

DROP TABLE IF EXISTS Button;
CREATE TABLE Button (
    button_id SERIAL,
    button_name TEXT,
    scen_id INTEGER,
    PRIMARY KEY (button_id),
    FOREIGN KEY (scen_id) REFERENCES Scenario(scen_id)
);

DROP TABLE IF EXISTS Var;
CREATE TABLE Var (
    variable_id SERIAL,
    var_name TEXT,
    var_type TEXT,
    config_id TEXT,
    PRIMARY KEY (variable_id)
);

DROP TABLE IF EXISTS Config;
CREATE TABLE Config (
    variable_id SERIAL,
    button_id INTEGER NOT NULL,
    config_id TEXT NOT NULL,
    PRIMARY KEY (config_id),
    FOREIGN KEY (variable_id) REFERENCES Var(variable_id),
    FOREIGN KEY (button_id) REFERENCES Button(button_id)
);

DROP TABLE IF EXISTS Action;
CREATE TABLE Action (
    action_id SERIAL,
    action_name TEXT,
    action_desc TEXT,
    PRIMARY KEY (action_id)
);

DROP TABLE IF EXISTS Analytics;
CREATE TABLE Analytics (
    log_id SERIAL,
    insert_time TIMESTAMP,
    action_id INTEGER,
    PRIMARY KEY (log_id),
    FOREIGN KEY (action_id) REFERENCES Action(action_id)
);

INSERT INTO Action
VALUES (1, 'floor move', 'Move up to a specific floor');
