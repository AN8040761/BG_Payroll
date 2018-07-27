#!/bin/bash
#PASS=`pwgen -s 40 1`
PASS=''
db=BGPayroll
mysql -uroot <<MYSQL_SCRIPT
CREATE DATABASE IF NOT EXISTS $db;
USE $db;
CREATE USER IF NOT EXISTS '$db'@'localhost' IDENTIFIED BY '$PASS';
GRANT ALL PRIVILEGES ON $db.* TO '$db'@'localhost';
FLUSH PRIVILEGES;
CREATE TABLE danni_osiguren(
  id_n TINYINT PRIMARY KEY,
  egn CHAR(10),
  flag BOOLEAN,
  last_name VARCHAR(25),
  initials CHAR(2),
  gross_salary DOUBLE,
  experience_years TINYINT,
  b_year YEAR,
  type_ens TINYINT,
  proff_code CHAR(8),
  activity_code TINYINT
);
CREATE TABLE danni_osiguritel(
  name VARCHAR(50),
  code VARCHAR(13) PRIMARY KEY,
  ordinal_number TINYINT
);
CREATE TABLE danni_forma_76(
  year YEAR,
  month VARCHAR(2),
  id_n TINYINT PRIMARY KEY,
  r TINYINT,
  o TINYINT,
  m TINYINT,
  b TINYINT,
  d TINYINT,
  a TINYINT,
  s TINYINT,
  n TINYINT,
  baza_pgo DOUBLE
);
MYSQL_SCRIPT

echo "MySQL user created."
echo "Username:   $db"
echo "Password:   $PASS"
