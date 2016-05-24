__author__ = 'NatuMyers'

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound




#PAGES ---
# replace "test" with the name of this file

# test page blueprint
test = Blueprint('test', __name__, template_folder='templates')
# what the user needs to enter as an url to to get to this file
@test.route('/test', defaults={'page': 'index'})
# end page


#to work with pages and get suburls
@test.route('/test/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)




