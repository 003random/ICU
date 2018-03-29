CREATE TABLE directories
(
DirectoryID int NOT NULL AUTO_INCREMENT,
DomainID int NOT NULL,
Directory varchar(255) not null,
File bit NOT NULL DEFAULT 0,
Active bit NOT NULL DEFAULT 0,
PRIMARY KEY (DirectoryID),
FOREIGN KEY (DomainID) REFERENCES domains(DomainID)
);
