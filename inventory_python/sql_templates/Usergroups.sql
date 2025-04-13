-- inventory.usergroups definition

CREATE TABLE usergroups (
  ID int(11) NOT NULL AUTO_INCREMENT,
  Name varchar(100) DEFAULT NULL,
  PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;