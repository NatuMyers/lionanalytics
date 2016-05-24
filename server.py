#!/usr/bin/python
#
# Flask server, woo!
#

from flask import Flask, request, redirect, url_for, send_from_directory

# THIS IS THE ONLY PY CODE FOR THE HOME------

# Setup Flask app.
app = Flask(__name__, static_url_path='', template_folder="bigApps")
# app = Flask(__name__, static_url_path='') # if assets in in static root, no quotes like this
app.debug = True

# THE ANGULAR APP (GOES TO STATIC FOLDER)
# Routes
@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)



# THE OTHER PYTHON APPS (NOT WITH BLUEPRINT)--------

# DECEPTRON 
from flask import render_template, jsonify
from lib.deceptron import calcDeceptiveness

#MAKE SURE you update the post location (in the included js file) to 
#this route
@app.route('/deceptron', methods=['GET', 'POST'])
def deceptron():
    if request.method == 'POST':
        data = request.get_json()
        text = data[u'text']
        result = calcDeceptiveness(text)
        return result
    else:
        return render_template('deceptronHome.html')





# THE OTHER SMALLER PYTHON APPS (DONE WITH BLUEPRINT)--------

from icApp.ic import ic
app.register_blueprint(ic)
app.register_blueprint(ic, url_prefix='/static')

from testApp.test import test
app.register_blueprint(test)
app.register_blueprint(test, url_prefix='/pages')

from lotusApp.lotus import lotus
app.register_blueprint(lotus)
app.register_blueprint(lotus, url_prefix='/lotusApp/assets')



# RUN EVERYTHING!!!
if __name__ == '__main__':
  app.run()