CREATE TABLE IF NOT EXISTS customer (
    dni VARCHAR NOT NULL PRIMARY KEY,
    nombre VARCHAR,
    apellido1 VARCHAR,
    apellido2 VARCHAR,
    fecha_nacimiento DATE DEFAULT CURRENT_DATE,
    telefono VARCHAR,
    email VARCHAR,
    calle VARCHAR,
    portal int,
    puerta VARCHAR,
    CP INT,
    ciudad VARCHAR,
    IBAN VARCHAR,
    alta DATE DEFAULT CURRENT_DATE,
    baja DATE DEFAULT NULL,
    cuota NUMERIC DEFAULT 0.0,
    activo BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS charge (
    id VARCHAR NOT NULL PRIMARY KEY
    dni VARCHAR NOT NULL FOREIGN KEY,
    date DATETIME NOT NULL,
    cost NUMBER NOT NULL DEFAULT 0.0,
    FOREIGN KEY(dni) REFERENCES Customers(dni)
);

CREATE TABLE IF NOT EXISTS charge_monthly_charge (
    id INT PRIMARY KEY AUTOINCREMENT NOT NULL,
    charge_id VARCHAR NOT NULL,
    monthly_charge_id VARCHAR NOT NULL,
    FOREIGN KEY(charge_id) REFERENCES charge(id),
    FOREIGN KEY(monthly_charge_id) REFERENCES monthly_charge(id)
);

CREATE TABLE IF NOT EXISTS monthly_charge (
    id VARCHAR NOT NULL PRIMARY KEY
    dni VARCHAR NOT NULL FOREIGN KEY,
    date DATETIME NOT NULL,
    total_charge NUMBER NOT NULL,
    FOREIGN KEY(dni) REFERENCES Customers(dni)
);