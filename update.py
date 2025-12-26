import sqlite3


db = sqlite3.connect("my.db")

cur = db.cursor()

cur.execute("UPDATE ФИО SET Имя = 'Крутой' WHERE Имя = 'Ярослав'")
db.commit()

db.close()

print("Код успешно выполнен!")