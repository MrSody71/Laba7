import sqlite3

db = sqlite3.connect("university.db")
cur = db.cursor()

cur.executescript("""
    CREATE TABLE группы (
        id integer,
        название_группы text
    );

    CREATE TABLE students (
        id integer,
        фамилия text,
        имя text,
        group_id integer
    );
""")

db.commit()
db.close()
print("Все таблицы успешно созданы!")