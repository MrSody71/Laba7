import sqlite3


db = sqlite3.connect("my.db")

cur = db.cursor()

cur.execute("""CREATE TABLE ФИО(
    Фамилия text,
    Имя text,
    Отчество text
)""")

db.commit()

db.close()

print("Код успешно выполнен!")