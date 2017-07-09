import json
import psycopg2
import redis
import time

def run():
    r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
    while True:
        task = r.brpop('task')
        if task:
            consumeRedisRecord(task[1])

def consumeRedisRecord(task):
    # task_json = {
    #     'token': 'eyJhbGciOiJSmtaysOrwuOm14HrFP6R0802kQA',
    #     'schema': 'a,b,c,d,e',
    #     'meta': [
    #         {
    #             'key': 'b8143253-2b36-4187-adac-e28dfecc5a3b',
    #             'piece': '1/1',
    #             'md5': '946f8138b7a2e4fb655c9396d16dbedd'
    #         }
    #     ]
    # }
    # task = """
    #      {"token": "eyJhbGciOiJSmtaysOrwuOm14HrFP6R0802kQA", "meta": [{"piece": "1/1", "key": "b8143253-2b36-4187-adac-e28dfecc5a3b", "md5": "946f8138b7a2e4fb655c9396d16dbedd"}], "schema": "a,b,c,d,e"}
    # """
    task_json = json.loads(task)

    for meta_obj in task_json['meta']:
        file_name = meta_obj['md5']
        insert2Database(file_name)

def connect2Database():
    conn = 'dbname=flask user=postgres password=postgres host=localhost'
    try:
        return psycopg2.connect(conn)
    except:
        print('Failed to connect to database..')

def insert2Database(file_name):
    conn = connect2Database()
    cur = conn.cursor()
    with open(file_name, 'r') as f:
        for line in f:
            line = line.split(',')
            try:
                cur.execute("INSERT INTO data(A, B, C, D, E) VALUES (%s, %s, %s, %s, %s);", (line[0], line[1], line[2], line[3], line[4]))
                conn.commit()
            except:
                print("Failed to insert record, rolling back..")
                conn.rollback()
    cur.close()
    conn.close()

if __name__ == '__main__':
    run()
