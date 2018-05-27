#!/usr/bin/python

import MySQLdb
import sys

username = "rjp"
password = "1484"

connection = MySQLdb.connect (host = "localhost", user = username, passwd = password)

cursor = connection.cursor ()

cursor.execute ("""
CREATE DATABASE recon;
""")

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
