#!/usr/bin/python

import MySQLdb
import sys

connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")

cursor = connection.cursor ()

cursor.execute ("""
CREATE TABLE domains
(
    DomainID int NOT NULL AUTO_INCREMENT,
    Program varchar(255) not null,
    TopDomainID int default null,
    Active bit NOT NULL DEFAULT 0,
    InScope bit NOT NULL DEFAULT 0,
    Domain varchar(100) not null,
    LastModified timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (DomainID),
    FOREIGN KEY (TopDomainID) REFERENCES domains(DomainID),
    UNIQUE (Domain)
);
""")

cursor.execute ("""
CREATE TABLE directories
(
    DirectoryID int NOT NULL AUTO_INCREMENT,
    DomainID int NOT NULL,
    Directory varchar(255) not null,
    File bit NOT NULL DEFAULT 0,
    Active bit NOT NULL DEFAULT 0,
    LastModified timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (DirectoryID),
    FOREIGN KEY (DomainID) REFERENCES domains(DomainID)
);
""")

cursor.execute ("""
CREATE TABLE crlf
(
    CRLFID int NOT NULL AUTO_INCREMENT,
    DomainID int NOT NULL,
    Payload varchar(255) not null,
    Active bit NOT NULL DEFAULT 0,
    LastModified timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (CRLFID),
    FOREIGN KEY (DomainID) REFERENCES domains(DomainID)
);

""")

cursor.execute ("""
CREATE TABLE ports
(
    PortID int NOT NULL AUTO_INCREMENT,
    DomainID int NOT NULL,
    Port int NOT NULL,
    PortInfo varchar(255),
    Active bit NOT NULL DEFAULT 0,
    LastModified timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (PortID),
    FOREIGN KEY (DomainID) REFERENCES domains(DomainID)
);

""")

cursor.execute ("""
CREATE TABLE errors
(
    ErrorID int NOT NULL AUTO_INCREMENT,
    Domain varchar(255),
    ErrorDescription varchar(255),
    Error varchar(255),
    Script varchar(255),
    ErrorDate timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (ErrorID)
);

""")


cursor.close ()
connection.close ()
sys.exit()
