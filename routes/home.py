import json, requests
from datetime import datetime
from msilib.schema import Billboard
from flask import Blueprint, make_response, render_template, request, jsonify, url_for, redirect, session

index = Blueprint('index', __name__)

@index.route("/" , methods=['GET', 'POST'])
def home():
    if 'username' in session:
        username = session['username']
        
        return render_template('home.html', username = username)
    else:
        return render_template('home.html')