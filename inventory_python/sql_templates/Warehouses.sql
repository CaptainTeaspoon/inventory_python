-- inventory.warehouse definition

CREATE TABLE warehouse (
  ID int(11) NOT NULL AUTO_INCREMENT,
  Name varchar(100) DEFAULT NULL,
  Usergroup_ID int(11) DEFAULT NULL,
  PRIMARY KEY (ID),
  KEY Warehouse_Usergroups_FK (Usergroup_ID),
  CONSTRAINT Warehouse_Usergroups_FK FOREIGN KEY (Usergroup_ID) REFERENCES usergroups (ID) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;