# Flask app

# How to run the flask app:
1. $ export FLASK_APP=app.py <br>
   $ flask run
2. Drop a post chunk request thru POSTMAN:
<pre>
POST /chunk HTTP 1.1
Host: localhost:5050
Authorization: bearer eyJhbGciOiJSmtaysOrwuOm14HrFP6R0802kQA
agent-id: b8143253-2b36-4187-adac-e28dfecc5a3b
md5: 946f8138b7a2e4fb655c9396d16dbedd
feature: <feature-name>
piece: <current>/<total>
timestamp: <expected-time-stamp>
Content-Type: multipart/form-data

1,2,3,4,5
11,12,13,14,15
</pre>
A csv named 946f8138b7a2e4fb655c9396d16dbedd is generated including the raw data


# A daemon service to pull data from Redis and push to Postgres

# How to install daemon without install script
<pre>
1. initialize the database: 
e.g.
  "/Applications/Postgres.app/Contents/Versions/9.6/bin/psql" -U postgres -h localhost
  \i data.sql
2. start the daemon by:
  python server.py &
 </pre>

# How to push task to Redis list
<pre>
Redis task schema,
{
    "token": "eyJhbGciOiJSmtaysOrwuOm14HrFP6R0802kQA",
    "schema": "a,b,c,d,e",
    "meta": [
        {
            "key": “b8143253-2b36-4187-adac-e28dfecc5a3b",
            "piece": "1/1",
            "md5": "<md5 chechsum of raw data created in #1>"
        }
    ]
}

LPUSH task '{"token": "eyJhbGciOiJSmtaysOrwuOm14HrFP6R0802kQA", "meta": [{"piece": "1/1", "key": "b8143253-2b36-4187-adac-e28dfecc5a3b", "md5": "946f8138b7a2e4fb655c9396d16dbedd"}], "schema": "a,b,c,d,e"}'
</pre>
