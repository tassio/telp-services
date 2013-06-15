'''
Created on 15/06/2013

@author: PC2
'''
from flask import json

class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        #if isinstance(obj, datetime.datetime):
        #    return obj.format()
        #if isinstance(obj, ObjectId):
        #    return str(obj)
        return json.JSONEncoder.default(self, obj)

def json_renderer(**data):
    return json.dumps(data, cls=APIEncoder)