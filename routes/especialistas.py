import json, requests
from datetime import datetime
from msilib.schema import Billboard
from flask import Blueprint, make_response, render_template, request, jsonify, url_for, redirect, session

especialistas = Blueprint('especialistas', __name__)

@especialistas.route("/especialistas/registrarse", methods=['POST', 'GET'])
def registrarse():
    return render_template('/especialista/register.html')
