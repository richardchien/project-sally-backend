from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config as C

engine = create_engine('%s+%s://%s:%s@%s:%s/%s'
                       % (C.db_type, C.db_driver, C.db_user, C.db_pass, C.db_host, C.db_port, C.db_database))
Session = sessionmaker(bind=engine)
