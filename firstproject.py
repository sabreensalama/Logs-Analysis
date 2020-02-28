import psycopg2

first_qu = """
            select articles.title , count(log.id)as num from articles,log
where log.path=('/article/' || articles.slug) group by  articles.title  order
by num desc limit 3;"""


second_qu = """
            select authors.name ,count(log.id) as num from authors,log,
articles where authors.id = articles.author and log.path=('/article/'
|| articles.slug) group by authors.name order by num desc;"""

third_qu = """
         select
            to_char(errors_by_day.date,'Month DD, YYYY') as date,
            to_char(((errors_by_day.count::decimal
                    /requests_by_day.count::decimal)*100)
                    ,'9.99')
                    || '%' as percentage
         from
            (select date(time),count(*) from log
                        group by date(time)) as requests_by_day,
            (select date(time),count(*) from log where status != '200 OK'
                        group by date(time)) as errors_by_day
         where
            requests_by_day.date = errors_by_day.date
            and ((errors_by_day.count::decimal
                    /requests_by_day.count::decimal)*100) > 1;"""


def get(comm):
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(comm)
    return cursor.fetchall()
    conn.close()


def most_popular_three_articles():
    return get(first_qu)


def most_popular_articl_author():
    return get(second_qu)


def more_than_one_percentage_request_error():
    return get(third_qu)
