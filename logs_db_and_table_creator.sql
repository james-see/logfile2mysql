CREATE SCHEMA `logs` DEFAULT CHARACTER SET utf8mb4 ;
CREATE TABLE `logs` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `logdate` datetime(6) NOT NULL,
  `logtype` varchar(11) NOT NULL DEFAULT '',
  `logcode` varchar(200) NOT NULL,
  `logdescription` mediumtext NOT NULL,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `idx_logs` (`logdescription`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
