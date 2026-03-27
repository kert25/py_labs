import os
import shutil
from alembic.config import Config
from alembic import command
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer)


def create_alembic_config():
    cfg = Config()
    cfg.set_main_option("script_location", "alembic")
    cfg.set_main_option("sqlalchemy.url", "sqlite:///lab7_migrations.db")
    return cfg


if os.path.exists("alembic"):
    shutil.rmtree("alembic")

cfg = create_alembic_config()
command.init(cfg, "alembic")

engine = create_engine("sqlite:///lab7_migrations.db")
Base.metadata.create_all(engine)

print("Alembic инициализирован.")
print("Таблица products создана с колонками: id, name, price")

if os.path.exists("alembic"):
    shutil.rmtree("alembic")
