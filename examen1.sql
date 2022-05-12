-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: examen1
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `job_traveler`
--

DROP TABLE IF EXISTS `job_traveler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_traveler` (
  `id_traveler` int(11) NOT NULL,
  `Serial_number` varchar(30) DEFAULT NULL,
  `Panel_Number` varchar(30) DEFAULT NULL,
  `Job_Number` varchar(30) DEFAULT NULL,
  `Job_Name` varchar(30) DEFAULT NULL,
  `Seal` varchar(1) DEFAULT NULL,
  `Type` varchar(30) DEFAULT NULL,
  `Modbus_id` int(11) DEFAULT NULL,
  `Meter_No` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_traveler`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_traveler`
--

LOCK TABLES `job_traveler` WRITE;
/*!40000 ALTER TABLE `job_traveler` DISABLE KEYS */;
INSERT INTO `job_traveler` VALUES (0,'asddf','asd','asd','asd','1','asd',1,2),(1,'PCB-J-2017-1','2DMP-2DPEA','19-207-2954','ECLRT - SCIENC CENTRE STATION','X','MF6',3,1),(2,'PCB-J-2017-2','2DMP-2DPEA','19-207-2954','ECLRT - SCIENC CENTRE STATION','X','MF6',3,2);
/*!40000 ALTER TABLE `job_traveler` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-12 10:49:04
