from flask import Blueprints
public_bp('public', __name__, template_folder ='../../templates/public'
)

from . import routes

