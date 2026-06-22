from flask import render_template
from . import auth_bp

@public_bp.route('/login')
def login():
    return render_template('auth/login.html')

@public_bp.route('/registro')
def tienda():
    return render_template('auth/registro.html')
