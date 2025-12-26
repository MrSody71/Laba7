import psycopg2

conn = psycopg2.connect(
    database = "АИС",
    user = "postgres",
    password = "0000",
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()

cur.execute("SELECT * FROM users")

data = cur.fetchall()
for d in data:
    print(d)

conn.close()