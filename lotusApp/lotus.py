import os
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, make_response, jsonify, request

from flask import  Blueprint, abort
from jinja2 import TemplateNotFound

DIR = os.path.dirname(os.path.abspath(__file__))

lotus = Blueprint('lotus', __name__)
# 2nd lotus = Blueprint('lotus', __name__, static_folder='lotusApp/assets')
##no lotus._static_folder = '/lotus/static' 

def get_model():
    iris = datasets.load_iris()
    model = RandomForestClassifier(n_estimators=1000).fit(iris.data, iris.target)
    labels = list(iris.target_names)
    return model, labels


MODEL, LABELS = get_model()
 

@lotus.route('/lotus')
def index():
    return make_response(open(os.path.join(DIR, 'index.html')).read())
    


@lotus.route('/api/predict')
def predict():
    def getter(label):
        return float(request.args.get(label, 0))
    try:
        features = map(getter, ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth'])
        probs = MODEL.predict_proba(features)[0]
    except ValueError:
        probs = (1. / len(LABELS) for _ in LABELS)

    val = {"data": [{"label": label, "prob": prob} for label, prob in zip(LABELS, probs)]}
    return jsonify(val)








