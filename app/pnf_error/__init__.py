from flask import render_template
import flask

pnf = flask.Blueprint('pnf_error', __name__)

@pnf.app_pnf_error(404)
def page_not_found(e):
    return render_template("404.html"), 404