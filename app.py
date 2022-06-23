from flask import Flask
from routes.clientes import clientes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://workitadmin:workitadminuser@www.db4free.net/proyecto_workit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/bd_workit2.1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(clientes)



    