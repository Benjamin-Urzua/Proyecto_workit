from sqlalchemy import create_engine

try:
    #engine = create_engine('mysql://root:root@localhost:3306/proyecto2.3')
    engine = create_engine('mysql://root@localhost:3306/proyecto2.1')
except Exception as err:
    print(err)

'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
'''