import sqlite3


db = sqlite3.connect("my.db")

cur = db.cursor()

cur.execute("INSERT INTO ФИО VALUES ('Артюх', 'Виталий', 'Валеривеич')")

db.commit()

db.close()

print("Код успешно выполнен!")