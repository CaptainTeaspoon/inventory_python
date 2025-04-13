-- inventory.users definition

CREATE TABLE users (
  ID int(11) NOT NULL AUTO_INCREMENT,
  Password varchar(100) DEFAULT NULL COMMENT 'SHA256',
  Name varchar(100) DEFAULT NULL,
  Email varchar(100) NOT NULL,
  Usergroup_ID int(11) DEFAULT NULL,
  PRIMARY KEY (ID),
  UNIQUE KEY Users_unique (Email),
  KEY Users_Usergroups_FK (Usergroup_ID),
  CONSTRAINT Users_Usergroups_FK FOREIGN KEY (Usergroup_ID) REFERENCES usergroups (ID) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;