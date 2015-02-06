# Author: Jonatas Freitas (https://github.com/jonatasfreitasv)
# Código do artigo
# https://jonatasfreiitas.wordpress.com/2015/02/02/arquivo-de-configuracao-com-python/

from config import Config

db_host = Config.database['host']
debug = Config.test['debug']

print(db_host)
print(debug)
