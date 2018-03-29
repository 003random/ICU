CREATE TABLE crlf
(
CRLFID int NOT NULL AUTO_INCREMENT,
DomainID int NOT NULL,
Payload varchar(255) not null,
Active bit NOT NULL DEFAULT 0,
PRIMARY KEY (CRLFID),
FOREIGN KEY (DomainID) REFERENCES domains(DomainID)
);

