-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: moroiu_eric
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `compozitori_compozitii`
--

DROP TABLE IF EXISTS `compozitori_compozitii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compozitori_compozitii` (
  `id_compozitor` int NOT NULL,
  `id_compozitie` int NOT NULL,
  `detalii` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_compozitor`,`id_compozitie`),
  KEY `id_compozitie` (`id_compozitie`),
  CONSTRAINT `compozitori_compozitii_ibfk_1` FOREIGN KEY (`id_compozitor`) REFERENCES `compozitori` (`id_compozitor`) ON DELETE CASCADE,
  CONSTRAINT `compozitori_compozitii_ibfk_2` FOREIGN KEY (`id_compozitie`) REFERENCES `compozitii` (`id_compozitie`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compozitori_compozitii`
--

LOCK TABLES `compozitori_compozitii` WRITE;
/*!40000 ALTER TABLE `compozitori_compozitii` DISABLE KEYS */;
INSERT INTO `compozitori_compozitii` VALUES (1,8,'O melodie rar ascultata de tineri dar iubita de adulti'),(2,2,'Ultima lucrare a lui Mozart, neterminata.'),(2,3,'das555555');
/*!40000 ALTER TABLE `compozitori_compozitii` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-27 23:11:03
