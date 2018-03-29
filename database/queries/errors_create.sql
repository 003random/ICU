CREATE TABLE errors
(
    ErrorID int NOT NULL AUTO_INCREMENT,
    Domain varchar(255),
    ErrorDescription varchar(255),
    Error varchar(255),
    Script varchar(255),
    ErrorDate datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (ErrorID)
);
