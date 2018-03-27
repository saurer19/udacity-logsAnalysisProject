# Logs Analysis Project
This project is a internal reporting tool that uses the information from a PostgreSQL database. The database News contains newspapper articles, authors and the web server log of the fictional website.

The python script connects to the database using psycopg2 and execute SQL queries to print out the answers the following questions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

## Requeriments
* Python3
* PostgreSQL
* Vagrant
* VirtualBox

## How to run
1. Donwload the DB data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Unzip and move the file to the project directory 
3. Go to the project directory to run `vagrant up`  to create a virtual machine and then `vagrant ssh` to enter.
4. Navigate to the directory `/vagrant`  and use the command:
```
psql -d news -f newsdata.sql 
```
5. Connect to the database using:
```
psql -d news
```
6. Create the following view
```sql
CREATE VIEW daypercent AS SELECT date(time) date, 
(count(*)filter(WHERE status!='200 OK')*100.0/count(*)) 
AS percentage FROM log GROUP BY date(time) 
ORDER BY percentage DESC;
```
5. Run the python script
```
python run.py
```
### Views Created
```sql
CREATE VIEW daypercent AS SELECT date(time) date, 
(count(*)filter(WHERE status!='200 OK')*100.0/count(*)) 
AS percentage FROM log GROUP BY date(time) 
ORDER BY percentage DESC;
```