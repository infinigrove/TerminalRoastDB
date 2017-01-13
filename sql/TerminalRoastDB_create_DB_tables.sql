-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: localhost    Database: terminalroastDB
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipe_master`
--

DROP TABLE IF EXISTS `recipe_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe_master` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `notes` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_master`
--

LOCK TABLES `recipe_master` WRITE;
/*!40000 ALTER TABLE `recipe_master` DISABLE KEYS */;
INSERT INTO `recipe_master` VALUES (1,'test_seq','used for debugging and testing roaster software'),(2,'French Roast','dark for espresso '),(3,'FR2','Other isn\'t dark enough it\'s just a little past full city');
/*!40000 ALTER TABLE `recipe_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_steps`
--

DROP TABLE IF EXISTS `recipe_steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe_steps` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `recipe_id` int(10) unsigned NOT NULL,
  `sectionTime` int(11) NOT NULL,
  `fanSpeed` int(11) NOT NULL,
  `targetTemp` int(11) NOT NULL,
  `seqNum` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `steps_recipe_index` (`recipe_id`),
  CONSTRAINT `recipe_steps_ibfk_1` FOREIGN KEY (`recipe_id`) REFERENCES `recipe_master` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_steps`
--

LOCK TABLES `recipe_steps` WRITE;
/*!40000 ALTER TABLE `recipe_steps` DISABLE KEYS */;
INSERT INTO `recipe_steps` VALUES (1,1,10,9,200,0),(2,1,20,8,0,1),(3,1,5,7,200,2),(4,1,20,6,0,3),(5,2,120,9,220,0),(6,2,30,9,250,1),(7,2,30,9,300,2),(8,2,60,8,320,3),(9,2,180,8,350,4),(10,2,150,7,370,5),(11,2,60,7,390,6),(12,2,30,6,420,7),(13,2,30,5,450,8),(14,2,30,4,480,9),(15,2,30,4,485,10),(16,2,60,4,490,11),(17,2,120,3,500,12),(18,2,180,9,0,13),(19,3,120,9,250,0),(20,3,30,9,280,1),(21,3,30,9,300,2),(22,3,30,9,320,3),(23,3,30,8,340,4),(24,3,60,8,360,5),(25,3,60,8,380,6),(26,3,60,8,400,7),(27,3,60,7,420,8),(28,3,60,7,440,9),(29,3,60,6,460,10),(30,3,60,6,470,11),(31,3,80,5,480,12),(32,3,80,4,490,13),(33,3,100,3,500,14),(34,3,180,9,0,15);
/*!40000 ALTER TABLE `recipe_steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roaster_recipe`
--

DROP TABLE IF EXISTS `roaster_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roaster_recipe` (
  `id` int(11) NOT NULL,
  `recipe_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roaster_recipe`
--

LOCK TABLES `roaster_recipe` WRITE;
/*!40000 ALTER TABLE `roaster_recipe` DISABLE KEYS */;
INSERT INTO `roaster_recipe` VALUES (1,3);
/*!40000 ALTER TABLE `roaster_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roaster_recipe_step`
--

DROP TABLE IF EXISTS `roaster_recipe_step`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roaster_recipe_step` (
  `id` int(11) NOT NULL,
  `recipe_step` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roaster_recipe_step`
--

LOCK TABLES `roaster_recipe_step` WRITE;
/*!40000 ALTER TABLE `roaster_recipe_step` DISABLE KEYS */;
INSERT INTO `roaster_recipe_step` VALUES (1,16);
/*!40000 ALTER TABLE `roaster_recipe_step` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'terminalroastDB'
--

--
-- Dumping routines for database 'terminalroastDB'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-13 16:18:46
