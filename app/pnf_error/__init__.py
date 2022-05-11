from flask import render_template
import flask

pnf_error = flask.Blueprint('pnf_error', __name__)

@pnf_error.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404