from flask import Flask
from routes.especialistas import especialistas
from routes.clientes import clientes
from routes.home import index
#from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = '/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
app.secret_key = 'my_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://workitadmin:workitadminuser@www.db4free.net/proyecto_workit'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/bd_workit2.1'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/proyecto2.1'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

app.register_blueprint(index)
app.register_blueprint(especialistas)
app.register_blueprint(clientes)



    