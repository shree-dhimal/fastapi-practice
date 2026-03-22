from apps.db.session import engine
from apps.db.base import Base

def init_db():
    Base.metadata.create_all(bind=engine)