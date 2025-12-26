from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///fio_database.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)

    def __repr__(self):
        return f"{self.id} | {self.last_name} {self.first_name} {self.middle_name}"

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def display_table(title):
    print(f"\n--- {title} ---")
    users = session.query(User).all()
    if not users:
        print("Таблица пуста")
    else:
        print("ID | ФИО")
        print("-" * 30)
        for u in users:
            print(u)
    print("-" * 30)


user1 = User(last_name="Артюх", first_name="Виталий", middle_name="Валериевич")
user2 = User(last_name="Иванов", first_name="Иван", middle_name="Иванович")
session.add_all([user1, user2])
session.commit()

display_table("ТАБЛИЦА ДО ОБНОВЛЕНИЯ")


user_to_update = session.query(User).filter_by(last_name="Артюх").first()
if user_to_update:
    user_to_update.first_name = "Виктор"
    session.commit()
    print(f"\n[Система]: Имя пользователя с ID {user_to_update.id} успешно изменено.")


user_to_delete = session.query(User).filter_by(last_name="Иванов").first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print(f"[Система]: Пользователь {user_to_delete.last_name} удален.")

display_table("ТАБЛИЦА ПОСЛЕ ОБНОВЛЕНИЯ")

session.close()