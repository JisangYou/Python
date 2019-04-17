import psycopg2 as pg2

# conn = pg2.connect("host = localhost dbname=test user=postgres password=1234 port=5432")
#
conn = pg2.connect(database="postgres", user="postgres", password="secret", host="127.0.0.1", port="5432")

# CREATE TABLE 명령 실행
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
# Placeholder를 통해 데이터를 전달한다.
# placeholder는 어떤 데이터 타입의 경우에도 %s만 사용한다!!
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# SELECT명령을 실행해서 결과를 얻는다
cur.execute("SELECT * FROM test;")

cur.fetchone()

# 데이터를 수정했을 경우 반드시 commit
conn.commit()

# 연결을 종료한다
cur.close()
conn.close()
