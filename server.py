#!/usr/bin/python
#
# Flask server, woo!
#

from flask import Flask, request, redirect, url_for, send_from_directory, jsonify

# THIS IS THE ONLY PY CODE FOR THE HOME------

# Setup Flask app.
app = Flask(__name__, static_url_path='', template_folder="bigApps")
# app = Flask(__name__, static_url_path='') # if assets in in static root, no quotes like this
app.debug = True


# DATA
from flask_sqlalchemy import SQLAlchemy
deceptronDB = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# Create the deceptron tables 
def makeDeceptronDB():
    """ A helper function to create our tables 
    """
    deceptronDB.create_all()



class Doc(deceptronDB.Model):
    id = deceptronDB.Column(deceptronDB.Integer, primary_key=True)
    resultantString = deceptronDB.Column(deceptronDB.String(500))
    negativeSubconsiousFactor = deceptronDB.Column(deceptronDB.Integer)
    storyExaggerationFactor = deceptronDB.Column(deceptronDB.Integer)
    cognitiveLoadFactor = deceptronDB.Column(deceptronDB.Integer)
    selfAvoidanceFactor = deceptronDB.Column(deceptronDB.Integer)


    def __init__(self, resultantString, input):
        self.resultantString = resultantString
        self.input = input


    #def __init__(self, resultantString, negativeSubconsiousFactor, storyExaggerationFactor, cognitiveLoadFactor, selfAvoidanceFactor):
    #    self.resultantString = resultantString
    #    self.negativeSubconsiousFactor = negativeSubconsiousFactor
    #    self.storyExaggerationFactor = storyExaggerationFactor
    #    self.cognitiveLoadFactor = cognitiveLoadFactor
    #    self.selfAvoidanceFactor = selfAvoidanceFactor

    def __repr__(self):
        return '<Doc %r>' % self.resultantString
        

        
        
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
        
        stringtoInt = [int(s) for s in result.split() if s.isdigit()]
        
        #add to db
        deceptronDB.session.add(Doc(result,text))
        deceptronDB.session.commit()
		
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