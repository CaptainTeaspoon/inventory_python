-- inventory.items definition

CREATE TABLE items (
  ID int(11) NOT NULL AUTO_INCREMENT,
  Name varchar(100) DEFAULT NULL,
  Barcode int(11) DEFAULT NULL,
  Cost int(11) DEFAULT NULL,
  Expiration_Date date DEFAULT NULL,
  Warehouse_ID int(11) DEFAULT NULL,
  PRIMARY KEY (ID),
  KEY Items_warehouse_FK (Warehouse_ID),
  CONSTRAINT Items_warehouse_FK FOREIGN KEY (Warehouse_ID) REFERENCES warehouse (ID) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;