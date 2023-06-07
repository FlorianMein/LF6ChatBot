USE DATABASE solutions_it_support;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `Abteilung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `telefon` varchar(25) DEFAULT NULL,
  PRIMARY KEY(`id`),
  UNIQUE(`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `Anfragen` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `datum` date NOT NULL,
  `abteilung` int(11) NOT NULL,
  `verlauf` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`abteilung`) REFERENCES Abteilung(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO abteilung (name, mail, telefon)
VALUES ("Buchhaltung", "buchhaltung@itsolution.de", "0123/456789"),
("Systemintegration", "sysint@itsolution.de", "0123/987654"),
("Netzwerkbetreuung", "network@itsolution.de", "0123/456827"),
("Softwareentwicklung", "software@itsolution.de", "0123/159753")