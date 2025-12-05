from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "postgresql://root:agc123@localhost:5432/task_manager"
engine = create_engine(db_url)

session = sessionmaker(autocommit =False, autoflush=False, bind=engine)
