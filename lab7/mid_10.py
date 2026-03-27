from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///lab7.db")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

session.add(User(name="Иван", age=25))
session.add(User(name="Мария", age=30))
session.commit()

users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Имя: {user.name}, Возраст: {user.age}")

session.close()
