#-*- coding: utf-8 -*-
from flask.blueprints import Blueprint
from werkzeug.exceptions import abort


collection = Blueprint("collection", __name__)

DOMAIN = {"usuarios": "", "objetos": "", "emprestimos":""}
@collection.route('/<collection>')
def _collection(collection):
    print(collection)
    if collection in DOMAIN.keys():
        return collection
    
    abort(404)
    
