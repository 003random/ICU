#!/usr/bin/python

import MySQLdb
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import credentials

connection = MySQLdb.connect (host = credentials.database_server, user = credentials.database_username, passwd = credentials.database_password)
cursor = connection.cursor ()

cursor.execute ("""
CREATE DATABASE recon;
""")

connection = MySQLdb.connect (host = credentials.database_server, user = credentials.database_username, passwd = credentials.database_password, db = credentials.database_name)
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
    scan_Id int,
    PRIMARY KEY (DomainID),
    FOREIGN KEY (TopDomainID) REFERENCES domains(DomainID),
    UNIQUE (Domain)
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
    scan_ID int,
    PRIMARY KEY (ErrorID)
);
""")


cursor.execute ("""
CREATE TABLE scans 
( 
	ScanID int NOT NULL AUTO_INCREMENT, 
	StartDate datetime NOT NULL, 
	EndDate datetime, 
	primary key (ScanID) 
);
""")

cursor.close ()
connection.close ()
sys.exit()
