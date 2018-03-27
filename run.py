import psycopg2


def execute_query(query):
    db = psycopg2.connect('dbname=news')
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    colnames = [desc[0] for desc in c.description]
    print (colnames[0]+" -------- "+colnames[1])
    for row in rows:
        print (row[0], row[1])
    db.close()
    

query1 = ("select articles.title, count(log.path) as views from articles "  # NOQA
	"join log on replace(log.path, '/article/','')=articles.slug "  # NOQA
    "group by articles.title order by views desc limit 3;")


query2 = ("select authors.name, count(log.path) as views from (articles "  # NOQA
    "join log on replace(log.path, '/article/','')=articles.slug) join "  # NOQA
    "authors on articles.author = authors.id group by authors.name "  # NOQA
    "order by views desc;")

query3 = ("select date, percentage from daypercent where percentage>1;")

queries = [query1, query2, query3];

for quiery in queries:
    execute_query(quiery)
    print ('\n')