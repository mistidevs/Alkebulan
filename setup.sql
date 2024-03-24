-- Setting up the alkebulan database with users for it on MySQL
CREATE DATABASE IF NOT EXISTS alkebulan_db;
CREATE USER IF NOT EXISTS 'alkebulan_dev'@'localhost' IDENTIFIED BY 'alkebulan_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'alkebulan_dev'@'localhost';
GRANT ALL PRIVILEGES ON alkebulan_db.* TO 'alkebulan_dev'@'localhost';
FLUSH PRIVILEGES;