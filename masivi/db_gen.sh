#!/bin/bash
#set -x
FILE=("danni_osiguren.csv" "danni_osiguritel.csv" "danni_forma_76.csv")

for i in ${FILE[@]}; do
tail -n +2 $i > "$i.tmp"
done

for i in ${FILE[@]}; do
sqlite3 osnoven_masiv.db "DROP TABLE IF EXISTS ${i%.csv};"
done

sqlite3 osnoven_masiv.db << EOF
CREATE TABLE danni_osiguren(
  "id_n" INTEGER PRIMARY KEY,
  "egn" INTEGER,
  "flag" INTEGER,
  "last_name" TEXT,
  "initials" TEXT,
  "gross_salary" REAL,
  "experience_years" INTEGER,
  "b_year" INTEGER,
  "type_ens" INTEGER,
  "proff_code" INTEGER,
  "activity_code" INTEGER
);
CREATE TABLE danni_osiguritel(
  "name" TEXT,
  "code" INTEGER PRIMARY KEY,
  "ordinal_number" INTEGER
);
CREATE TABLE danni_forma_76(
  "year" INTEGER,
  "month" INTEGER,
  "id_n" INTEGER PRIMARY KEY,
  "r" INTEGER,
  "o" INTEGER,
  "m" INTEGER,
  "b" INTEGER,
  "d" INTEGER,
  "a" INTEGER,
  "s" INTEGER,
  "n" INTEGER,
  "baza_pgo" REAL
);
.mode csv
.headers on
.import danni_osiguren.csv.tmp danni_osiguren
.import danni_osiguritel.csv.tmp danni_osiguritel
.import danni_forma_76.csv.tmp danni_forma_76
.exit
EOF

for i in ${FILE[@]}; do
rm "$i.tmp"
done
result=$( sqlite3 osnoven_masiv.db "select * from danni_osiguren inner join danni_forma_76 on danni_osiguren.id_n=danni_forma_76.id_n;" )
echo -e "result=\n$result"



