CREATE TABLE domains
(
DomainID int NOT NULL AUTO_INCREMENT,
Program varchar(255) not null,
TopDomainID int default null,
Active bit NOT NULL DEFAULT 0,
InScope bit NOT NULL DEFAULT 0,
Domain varchar(100) not null,
PRIMARY KEY (DomainID),
FOREIGN KEY (TopDomainID) REFERENCES domains(DomainID),
UNIQUE (Domain)
);

