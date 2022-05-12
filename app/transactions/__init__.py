import csv
import logging
import os
import io

from flask import Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Transaction
from app.transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

transactions = Blueprint('transactions', __name__,
                                        template_folder = 'templates')

@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])
def transaction_browse(page):
    page = page
    per_page = 50
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)
        
@transactions.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transaction_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("request")
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join('./uploads', filename)
        form.file.data.save(filepath)
        user = current_user
        list_of_transactions = []
        with open(filepath, encoding = 'utf-8') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_transactions.append(Transaction(row['AMOUNT'], row['TYPE']))

        current_user.transactions = list_of_transactions
        db.session.commit()
        log.info(user, 'has uploaded a csv file' )
        return redirect(url_for('transactions.transaction_browse'))
    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)