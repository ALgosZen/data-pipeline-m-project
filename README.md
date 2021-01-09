Getting Started

To get a local copy up and running follow these simple steps.

Prerequisites
1. mySQL - Install and run mySQL . even better install Docker and get mySQL up and running using the
following script. easy ..1.2..3...

this docker run will install mysql and mount disk volume . change directory appropriately
docker run --restart always --name mysql:latest --net dev-network \
        && -v /Users/<mac-user/mysql-data-volume>:/var/lib/mysql \
        && -p 3306:3306 -d -e MYSQL_ROOT_PASSWORD=<password>  mysql:latest

2. Clone the repo
git clone

3. run source/datapipeline py file. input mysql connection string. code will load CSV file to mySQL db. If the script fails to create db run sql command
create database

For more info, please refer to the Documentation under docs folder.



