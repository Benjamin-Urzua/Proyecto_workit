import json, requests
from datetime import datetime
from msilib.schema import Billboard
from flask import Blueprint, make_response, render_template, request, jsonify, url_for, redirect, session
from controllers.register import  SelectRubro

especialistas = Blueprint('especialistas', __name__)

@especialistas.route("/especialistas/registrarse", methods=['POST', 'GET'])
def registrarse():
    rubros = SelectRubro()
    return render_template('/especialista/register.html' , rubros = rubros)

@especialistas.route("/especialistas/registrarse/guardar", methods=['GET', 'POST'])
def guardar_registro():
    try:
        response = request.form.to_dict()
        images = request.files.to_dict()
        
        #response.update(images)
        print('images: {} '.format(images["images"]))
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        return '/'
