# Author: Jonatas Freitas (https://github.com/jonatasfreitasv)
# Código do artigo
# https://jonatasfreiitas.wordpress.com/2015/02/01/python-3-x-sqlalchemy-orm-mysql/

from connect import Connection
from users import Users

connection = Connection.session()

# insert
new_user = Users('David Gilmour', 'pinkfloyd', '77@77')
connection.add(new_user)
connection.commit()

# select
user = connection.query(Users).filter_by(id=1).first()
print(user)

# update
user.name = "Richard Wright"
connection.commit()
print(user)

# delete
connection.delete(user)
connection.commit()
