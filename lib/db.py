# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-7'


from config import db_config, global_settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

Base = declarative_base()

MYSQL_ENGINE_STRING = "mysql+mysqldb://%s:%s@%s:%d/%s" % \
    (db_config.get('USER'), db_config.get('PASSWD'),
     db_config.get('MASTER_HOST'), db_config.get('PORT'),
     db_config.get('DB_NAME'))

db_engine = create_engine(MYSQL_ENGINE_STRING, encoding='utf-8', echo=global_settings.get('DEBUG'))
db_session = scoped_session(sessionmaker(bind=db_engine))


if "__main__" == __name__:
    from lib.app_model import *
    from workflow.models import *

    Base.metadata.create_all(db_engine)