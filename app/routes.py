from flask import Blueprint, render_template, url_for, redirect, request, make_response

from app.models.user import User

index = Blueprint("main", __name__, url_prefix='/')

@index.route('index.js')
@index.route('/')
def index_page():
    tg_id = request.cookies.get("telegram_id")
    if tg_id:
        return render_template('index.html')
    else:
        return render_template('test.html')

@index.route('/setid')
def set_id():
    mr= make_response(redirect("/"))
    mr.set_cookie("telegram_id","123456", max_age=12, samesite=None)
    return mr