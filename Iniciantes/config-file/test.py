from config import Config

db_host = Config.database['host']
debug = Config.test['debug']

print(db_host)
print(debug)
