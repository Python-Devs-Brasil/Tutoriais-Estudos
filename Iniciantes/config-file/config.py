# Author: Jonatas Freitas (https://github.com/jonatasfreitasv)
# Código do artigo
# https://jonatasfreiitas.wordpress.com/2015/02/02/arquivo-de-configuracao-com-python/


class Config:
    test = dict(
        debug=True
    )

    database = dict(
        host='jonatasfreiitas.wordpress.com',
        database='db_name',
        port='3306',
        user='user',
        password='password'
    )
