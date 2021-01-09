Getting Started

To get a local copy up and running follow these simple steps.

Prerequisites
1. mySQL - Install and run mySQL . even better install Docker and get mySQL up and running using the
following script. easy ..1.2..3...

this docker run will install mysql and mount disk volume . change directory appropriately.1


docker run --restart always --name mysql:latest --net dev-network \
        && -v /Users/<user/mysql-data-volume>:/var/lib/mysql \
        && -p 3306:3306 -d -e MYSQL_ROOT_PASSWORD=<<password>>  mysql:latest

2. Clone the repo

git clone <repo>

3. run source/datapipeline py file. input mysql connection string command line . assuming database and table already exits.1


4. code will load CSV file to mySQL db. rerun deleting records on safe mode for any issues.


For more info, please refer to the Documentation under docs folder.



