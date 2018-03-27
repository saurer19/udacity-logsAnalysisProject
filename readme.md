#Logs Analysis Project
Python script that connects to a PostgreSQL DB and print the queries declared.

##Requeriments
*Python3
*PostgreSQL
*Vagrant

##How to run
1. Donwload the DB data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. Go into the vagrant directory and use the command
```
psql -d news -f newsdata.sql 
```
3. Connect to the database using
```
psql -d news
```
4. Create the following view
```
create view daypercent as select date(time) date, (count(*)filter(where status!='200 OK')*100.0/count(*)) as percentage  from log group by date(time) order by percentage desc;
```
5. Run the python scritp
```
python run.py
```
### Views Created
```
create view daypercent as select date(time) date, (count(*)filter(where status!='200 OK')*100.0/count(*)) as percentage  from log group by date(time) order by percentage desc;
```