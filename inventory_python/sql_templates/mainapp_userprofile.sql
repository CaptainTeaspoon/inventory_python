-- inventory.mainapp_userprofile definition

CREATE TABLE `mainapp_userprofile` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Usergroup_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `mainapp_userprofile_Usergroup_id_15db21b4_fk_usergroups_ID` (`Usergroup_id`),
  CONSTRAINT `mainapp_userprofile_Usergroup_id_15db21b4_fk_usergroups_ID` FOREIGN KEY (`Usergroup_id`) REFERENCES `usergroups` (`ID`),
  CONSTRAINT `mainapp_userprofile_user_id_c68a7d79_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;