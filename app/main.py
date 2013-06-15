'''
Created on 15/06/2013

@author: PC2
'''

from flask import Flask
from collection import collection
from util.regexConverter import RegexConverter

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter


app.register_blueprint(collection, url_prefix="/v1/collection")

if __name__ == "__main__":
    app.run(debug=True)