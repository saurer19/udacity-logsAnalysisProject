#!/usr/bin/env python3
import psycopg2
import decimal


def execute_query(query):
    db = psycopg2.connect('dbname=news')
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    colnames = [desc[0] for desc in c.description]
    for row in rows:
        if colnames[1] == "errors":
            print("{} - {}% {}".format(
                row[0], decimal.Decimal(str(round(row[1], 2))), colnames[1]
                ))
        else:
            print("{} - {} {}".format(row[0], row[1], colnames[1]))
    db.close()


query1 = (
    "SELECT articles.title, count(log.path) AS VIEWS FROM articles "
    "JOIN log ON replace(log.path, '/article/','')=articles.slug "
    "GROUP BY articles.title ORDER BY views DESC LIMIT 3;"
    )


query2 = (
    "SELECT authors.name, count(log.path) AS views FROM (articles "
    "JOIN log ON replace(log.path, '/article/','')=articles.slug) JOIN "
    "authors ON articles.author = authors.id GROUP BY authors.name "
    "ORDER BY views DESC;"
    )

query3 = (
    "SELECT date, percentage AS errors"
    " FROM daypercent WHERE percentage>1;"
    )

queries = [query1, query2, query3]
questions = [
    "What are the most popular three articles of all time?",
    "Who are the most popular article authors of all time?",
    "On which days did more than 1% of requests lead to errors?"
    ]

for i in range(len(queries)):
    print(questions[i])
    execute_query(queries[i])
    print ('\n')
