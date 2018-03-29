CREATE TABLE ports
(
PortID int NOT NULL AUTO_INCREMENT,
DomainID int NOT NULL,
Port int NOT NULL,
PortInfo varchar(255),
Active bit NOT NULL DEFAULT 0,
PRIMARY KEY (PortID),
FOREIGN KEY (DomainID) REFERENCES domains(DomainID)
);

