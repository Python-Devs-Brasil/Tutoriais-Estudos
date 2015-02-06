# Author: Jonatas Freitas (https://github.com/jonatasfreitasv)
# Código do artigo
# https://jonatasfreiitas.wordpress.com/2015/02/01/python-3-x-sqlalchemy-orm-mysql/

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:

    def session():

        connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
            "db_user",
            "db_pass",
            "db_host",
            "db_port",
            "db_name"
        )

        # echo = True, ativa debug
        engine = create_engine(connection_string, echo=False)
        Session = sessionmaker(bind=engine)

        return Session()
