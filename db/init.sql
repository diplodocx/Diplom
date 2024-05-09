CREATE TABLE Config (
    id CHAR(18) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Scenario (
    scen_id INTEGER NOT NULL,
    scen_desc CHAR(18),
    scen_name CHAR(18),
    PRIMARY KEY (scen_id)
);

CREATE TABLE Button (
    button_id INTEGER NOT NULL,
    button_name CHAR(18),
    scen_id INTEGER,
    PRIMARY KEY (button_id),
    FOREIGN KEY (scen_id) REFERENCES Scenario(scen_id)
);

CREATE TABLE Var (
    variable_id INTEGER NOT NULL,
    var_name CHAR(18),
    var_type CHAR(18),
    config_id CHAR(18),
    PRIMARY KEY (variable_id),
    FOREIGN KEY (config_id) REFERENCES Config(id)
);

CREATE TABLE Action (
    action_id INTEGER NOT NULL,
    action_name CHAR(18),
    action_desc CHAR(18),
    PRIMARY KEY (action_id)
);

CREATE TABLE Analytics (
    log_id INTEGER NOT NULL,
    insert_time DATE,
    action_id INTEGER,
    PRIMARY KEY (log_id),
    FOREIGN KEY (action_id) REFERENCES Action(action_id)
);
