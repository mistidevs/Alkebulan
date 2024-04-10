-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: alkebulan_db
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `user_name` varchar(128) NOT NULL,
  `full_name` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumers`
--

DROP TABLE IF EXISTS `consumers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumers` (
  `picture` varchar(128) DEFAULT NULL,
  `user_name` varchar(128) NOT NULL,
  `full_name` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone_number` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumers`
--

LOCK TABLES `consumers` WRITE;
/*!40000 ALTER TABLE `consumers` DISABLE KEYS */;
INSERT INTO `consumers` VALUES ('/defaults/default_consumer.jpg','samar','Samantha Roberts','samantha.roberts@example.co.uk','b8d2f7ddebe880a0f8cf1634ec818f39','+176543210987','07cc5d8b-98ac-458c-acd4-5d5354c6bb18','2024-04-10 12:13:45','2024-04-10 12:13:45'),('/defaults/default_consumer.jpg','ryaand','Ryan Anderson','ryan.anderson@domain.ca','0e145df74722de6981774db6904a960a','+155577788899','097be9ae-c579-4d2d-bcab-e9a48a561d31','2024-04-10 12:14:29','2024-04-10 12:14:29'),('/defaults/default_consumer.jpg','wiljon','William Jones','william.jones@domain.io','ac116f50d90015c613dfebad0c4136c4','+188877766655','13bc35a7-85bc-43ce-9bdb-0678f21807e6','2024-04-10 12:13:51','2024-04-10 12:13:51'),('/defaults/default_consumer.jpg','katbro','Katherine Brown','katherine.brown@domain.us','769a5307b0f303707b7deecff40762ee','+166688899900','2034224b-5c6e-4e0d-bba5-b7c75f173dd6','2024-04-10 12:14:22','2024-04-10 12:14:22'),('/defaults/default_consumer.jpg','patmur','Patrick Murray','patrick.murray@domain.de','ea7971c3f53fae0cf8b54a8033ab27ad','+188899922233','24171a82-7224-4efd-aafd-ae3a367fef62','2024-04-10 12:14:42','2024-04-10 12:14:42'),('/defaults/default_consumer.jpg','jasjam','Jason James','jason.james@domain.ru','8f0c8aa2af08ebcb8f7d44d0e29fb4e9','+155566677788','3d3bb37f-845f-4512-8d97-f215a9abccc1','2024-04-10 12:15:21','2024-04-10 12:15:21'),('/defaults/default_consumer.jpg','chrlar','Charlie Larkin','charlie.larkin@example.biz','71bb0237e152b050d0878158f9dc5e62','+199988877766','4afc1845-c16a-40ae-bc0c-81b4e61d8d27','2024-04-10 12:13:57','2024-04-10 12:13:57'),('/defaults/default_consumer.jpg','alfwri','Alfred Wright','alfred.wright@example.net','ccc581d7408847d0ec6d9d35782419ca','+155512345678','844331ec-2250-4e6c-b584-e9dfdcb51164','2024-04-10 12:13:30','2024-04-10 12:13:30'),('/defaults/default_consumer.jpg','annwil','Anna Wilkinson','anna.wilkinson@domain.jp','cf17e2013bd41648d94a617b18894555','+188899933322','911e2b8d-9369-4fe5-b5b4-d134252fe69e','2024-04-10 12:15:29','2024-04-10 12:15:29'),('/defaults/default_consumer.jpg','alival','Alice Valentine','alice.valentine@domain.nl','827fd78389492f08536a26f5c56781ac','+144477766655','9b184c51-d73e-4e62-b9c4-ab71513a2017','2024-04-10 12:14:48','2024-04-10 12:14:48'),('/defaults/default_consumer.jpg','lisrob','Lisa Robinson','lisa.robinson@domain.info','c8de6ae892e52af3dc647bcd3d931c7a','+144433322211','bcd3c955-2257-4992-b5ab-64a9b502fff5','2024-04-10 12:14:10','2024-04-10 12:14:10'),('/defaults/default_consumer.jpg','davmil','David Miller','david.miller@domain.br','0fc212a8d8043fb27a96d02ee0a9ba05','+199933322211','c48bec33-139a-4844-a6ef-5855d5cc6de3','2024-04-10 12:15:07','2024-04-10 12:15:07'),('/defaults/default_consumer.jpg','sarcla','Sarah Clark','sarah.clark@domain.mx','ac21fed15df2279989c7b74764ae9f55','+177788855544','ced15bb7-4275-48d0-8114-f794d6ba33fb','2024-04-10 12:15:15','2024-04-10 12:15:15'),('/defaults/default_consumer.jpg','katpau','Katherine Paul','katherine.paul@domain.it','73746d85b3ba9314ee8b322727960acf','+122233344455','db41a411-09a7-475a-a77f-d1efa8e9652e','2024-04-10 12:15:01','2024-04-10 12:15:01'),('/defaults/default_consumer.jpg','johmar','John Martin','john.martin@domain.org','118ccf20b5a4b47f0d866fc98d97c5bf','+112233445566','e6c85e27-4a84-41a2-9358-dc958ed5004d','2024-04-10 12:13:37','2024-04-10 12:13:37'),('/defaults/default_consumer.jpg','misan','Misaki Nakamura','misaki.nakamura@example.com','79de0b3fd35dc7dd52795d14161366ac','+123456789012','e744839d-4f56-4a5e-ae96-3082da45a805','2024-04-10 12:13:16','2024-04-10 12:13:16'),('/defaults/default_consumer.jpg','mignev','Mignon Everett','mignon.everett@domain.com','f2fee44d55228f1b0f2f4cfd61a85c2a','+198765432109','e87337f2-f5b8-4eca-8ade-7896b380b1bd','2024-04-10 12:13:24','2024-04-10 12:13:24'),('/defaults/default_consumer.jpg','petwes','Peter West','peter.west@domain.au','8ac01ef481d383751b0abeb454d23b20','+133322211144','ec09fcd0-c149-4516-9860-a37e4fcf174a','2024-04-10 12:14:55','2024-04-10 12:14:55'),('/defaults/default_consumer.jpg','andrwi','Andrew Williams','andrew.williams@example.co','1737c4250f147b8f5f26712b039e7846','+199944455566','f2523af4-b85f-4584-94b4-a2e89380223c','2024-04-10 12:14:17','2024-04-10 12:14:17'),('/defaults/default_consumer.jpg','marjac','Maria Jackson','maria.jackson@domain.edu','7068473658767a17208d62f0c3f09983','+177788899911','f7c127f6-334a-405d-b0a6-cf4e1bcb8372','2024-04-10 12:14:35','2024-04-10 12:14:35');
/*!40000 ALTER TABLE `consumers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmer_products`
--

DROP TABLE IF EXISTS `farmer_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_products` (
  `farmer_id` varchar(60) NOT NULL,
  `product_id` varchar(60) NOT NULL,
  `price` int NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farmer_id` (`farmer_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `farmer_products_ibfk_1` FOREIGN KEY (`farmer_id`) REFERENCES `farmers` (`id`),
  CONSTRAINT `farmer_products_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_products`
--

LOCK TABLES `farmer_products` WRITE;
/*!40000 ALTER TABLE `farmer_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `farmer_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmers`
--

DROP TABLE IF EXISTS `farmers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmers` (
  `picture` varchar(128) DEFAULT NULL,
  `user_name` varchar(128) NOT NULL,
  `full_name` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone_number` varchar(128) NOT NULL,
  `location` varchar(128) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_farmers_picture` (`picture`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmers`
--

LOCK TABLES `farmers` WRITE;
/*!40000 ALTER TABLE `farmers` DISABLE KEYS */;
INSERT INTO `farmers` VALUES ('/defaults/default_farmer.jpg','davie','David Wilson','farmer5@gmail.com','db0edd04aaac4506f7edab03ac855d56','+12223334455','Phoenix',33.4484,-112.074,'125b5430-068a-4613-beac-19a75d2f14cd','2024-04-10 11:56:13','2024-04-10 11:56:13'),('/defaults/default_farmer.jpg','dannie','Daniel Anderson','farmer9@gmail.com','5d69dd95ac183c9643780ed7027d128a','+12223334444','Dallas',32.7767,-96.797,'2eb353be-a25b-472d-81c1-feb1d7589eae','2024-04-10 11:56:35','2024-04-10 11:56:35'),('/defaults/default_farmer.jpg','mills','Sarah Miller','farmer6@gmail.com','218dd27aebeccecae69ad8408d9a36bf','+18887776655','Philadelphia',39.9526,-75.1652,'30096781-c98e-41c2-a5d3-7604fd39c6dd','2024-04-10 11:56:19','2024-04-10 11:56:19'),('/defaults/default_farmer.jpg','jackie','Ava Jackson','farmer10@gmail.com','87e897e3b54a405da144968b2ca19b45','+19998887766','San Jose',37.3382,-121.886,'34911e0d-4d26-40c1-b8f5-ab0b53f05b0d','2024-04-10 11:56:39','2024-04-10 11:56:39'),('/defaults/default_farmer.jpg','bella','Isabella Martin','farmer14@gmail.com','8ee736784ce419bd16554ed5677ff35b','+18889992211','San Francisco',37.7749,-122.419,'35f51737-f6e1-4d02-8f56-d2e60f108ddd','2024-04-10 11:57:02','2024-04-10 11:57:02'),('/defaults/default_farmer.jpg','sophie','Sophia White','farmer12@gmail.com','c24a542f884e144451f9063b79e7994e','+18886667755','Jacksonville',30.3322,-81.6557,'3dd185bb-358e-42d4-b813-05f53f4cd062','2024-04-10 11:56:51','2024-04-10 11:56:51'),('/defaults/default_farmer.jpg','willy','William Martinez','farmer17@gmail.com','a63f9709abc75bf8bd8f6e1ba9992573','+14446665555','Fort Worth',32.7555,-97.3308,'57f397cb-27ae-4d7e-934c-399b7aa149d0','2024-04-10 11:57:17','2024-04-10 11:57:17'),('/defaults/default_farmer.jpg','harry','Ethan Harris','farmer13@gmail.com','ee684912c7e588d03ccb40f17ed080c9','+12225556677','Indianapolis',39.7684,-86.1581,'642d812d-d621-41d1-85c0-ab76478afd1b','2024-04-10 11:56:56','2024-04-10 11:56:56'),('/defaults/default_farmer.jpg','mikey','Michael Johnson','farmer3@gmail.com','819b0643d6b89dc9b579fdfc9094f28e','+1555123456','Chicago',41.8781,-87.6298,'6d643b87-5623-470c-a0eb-f9a16c6f41e6','2024-04-10 11:56:02','2024-04-10 11:56:02'),('/defaults/default_farmer.jpg','jonnie','John Doe','farmer1@gmail.com','7c6a180b36896a0a8c02787eeafb0e4c','+1234567890','New York',40.7128,-74.006,'8a79e02c-8f2b-4e8f-a3d8-b005aed5b90b','2024-04-10 11:55:51','2024-04-10 11:55:51'),('/defaults/default_farmer.jpg','benji','Benjamin Clark','farmer19@gmail.com','e532ae6f28f4c2be70b500d3d34724eb','+16669998877','El Paso',31.7619,-106.485,'8b69f7a0-3ed9-4a5b-bcea-31d7fea407f7','2024-04-10 11:57:28','2024-04-10 11:57:28'),('/defaults/default_farmer.jpg','ema','Emily Brown','farmer4@gmail.com','34cc93ece0ba9e3f6f235d4af979b16c','+17702223344','Houston',29.7604,-95.3698,'8b898409-f2c8-48a0-afed-4bf1e16334d6','2024-04-10 11:56:07','2024-04-10 11:56:07'),('/defaults/default_farmer.jpg','alex','Alexander Thompson','farmer15@gmail.com','9141fea0574f83e190ab7479d516630d','+13337778899','Columbus',39.9612,-82.9988,'8daf6c31-d426-4924-9893-6586f85a8fb5','2024-04-10 11:57:07','2024-04-10 11:57:07'),('/defaults/default_farmer.jpg','jamie','James Taylor','farmer7@gmail.com','00cdb7bb942cf6b290ceb97d6aca64a3','+16665554433','San Antonio',29.4241,-98.4936,'904e034c-dca7-4ad7-bb27-b6b79eb33da4','2024-04-10 11:56:24','2024-04-10 11:56:24'),('/defaults/default_farmer.jpg','robi','Charlotte Robinson','farmer18@gmail.com','80b8bdceb474b5127b6aca386bb8ce14','+12224446688','Detroit',42.3314,-83.0458,'a8fa6696-f73c-442b-9a94-68d87efeca9a','2024-04-10 11:57:23','2024-04-10 11:57:23'),('/defaults/default_farmer.jpg','mel','Amelia Rodriguez','farmer20@gmail.com','aee67d9bb569ad1562f7b67cfccbd2ef','+12223339988','Memphis',35.1495,-90.049,'af0ab467-4641-4feb-8112-34a3b1b67d3b','2024-04-10 11:57:42','2024-04-10 11:57:42'),('/defaults/default_farmer.jpg','smithy','Jane Smith','farmer2@gmail.com','6cb75f652a9b52798eb6cf2201057c73','+1987654321','Los Angeles',34.0522,-118.244,'b56b1002-d153-4053-bc92-0e5953649821','2024-04-10 11:55:57','2024-04-10 11:55:57'),('/defaults/default_farmer.jpg','olive','Olivia Moore','farmer8@gmail.com','b25ef06be3b6948c0bc431da46c2c738','+13334445566','San Diego',32.7157,-117.161,'cbc8610a-53ac-4ea0-8609-ec5d40e8a392','2024-04-10 11:56:29','2024-04-10 11:56:29'),('/defaults/default_farmer.jpg','garcie','Mia Garcia','farmer16@gmail.com','2b40aaa979727c43411c305540bbed50','+15554443322','Charlotte',35.2271,-80.8431,'ea74029e-9d06-4e58-9539-32e06015b998','2024-04-10 11:57:12','2024-04-10 11:57:12'),('/defaults/default_farmer.jpg','matt','Matthew Thompson','farmer11@gmail.com','1e5c2776cf544e213c3d279c40719643','+17778889900','Austin',30.2672,-97.7431,'f1976904-797b-4b17-9d7c-53c93b656f2b','2024-04-10 11:56:44','2024-04-10 11:56:44');
/*!40000 ALTER TABLE `farmers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invalid_logins`
--

DROP TABLE IF EXISTS `invalid_logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invalid_logins` (
  `user_name` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `reason` varchar(128) NOT NULL,
  `login_date` datetime DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invalid_logins`
--

LOCK TABLES `invalid_logins` WRITE;
/*!40000 ALTER TABLE `invalid_logins` DISABLE KEYS */;
/*!40000 ALTER TABLE `invalid_logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `consumer_id` varchar(60) NOT NULL,
  `farmer_id` varchar(60) NOT NULL,
  `product_id` varchar(60) NOT NULL,
  `order_date` datetime DEFAULT NULL,
  `order_verification_pin` int DEFAULT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  `in_cart` tinyint(1) DEFAULT NULL,
  `quantity` int NOT NULL,
  `unit_price` int NOT NULL,
  `total_price` int NOT NULL,
  `farmer_review` varchar(1024) DEFAULT NULL,
  `consumer_review` varchar(1024) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `consumer_id` (`consumer_id`),
  KEY `farmer_id` (`farmer_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`consumer_id`) REFERENCES `consumers` (`id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`farmer_id`) REFERENCES `farmers` (`id`),
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `picture` varchar(128) DEFAULT NULL,
  `name` varchar(128) NOT NULL,
  `recommended_price` int NOT NULL,
  `max_price` int NOT NULL,
  `min_price` int NOT NULL,
  `description` varchar(1024) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_products_picture` (`picture`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valid_logins`
--

DROP TABLE IF EXISTS `valid_logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valid_logins` (
  `user_name` varchar(128) NOT NULL,
  `login_date` datetime DEFAULT NULL,
  `consumer_id` varchar(128) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `consumer_id` (`consumer_id`),
  CONSTRAINT `valid_logins_ibfk_1` FOREIGN KEY (`consumer_id`) REFERENCES `consumers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valid_logins`
--

LOCK TABLES `valid_logins` WRITE;
/*!40000 ALTER TABLE `valid_logins` DISABLE KEYS */;
/*!40000 ALTER TABLE `valid_logins` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-10 15:19:04
