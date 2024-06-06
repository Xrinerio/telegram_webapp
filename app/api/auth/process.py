from flask_restx import abort
from flask import current_app, jsonify

from ...database import db
from ...models.user import User
from .decorators import token_required, admin_token_required


def registration_process(email, password):
    if User.find_by_email(email):
        abort(401, f"{email} already registered", status="fail")
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    access_token = new_user.encode_access_token()
    return _create_auth_successful_response(token=access_token,
                                            status=201,
                                            message="successfully registered")


def login_process(email, password):
    user = User.find_by_email(email)
    if not user or not user.check_password(password):
        abort(401, "wrong email or password", status="fail")
    access_token = user.encode_access_token()
    return _create_auth_successful_response(token=access_token,
                                            status=200,
                                            message="successfully logged in")


def _create_auth_successful_response(token, status, message):
    response = dict(status="success",
                    message=message,
                    access_token=token,
                    expires_in=_token_expires_time())
    return response, status


def _token_expires_time():
    token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
    token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
    expires_in_seconds = token_age_h * 3600 + token_age_m * 60
    return expires_in_seconds


def get_token_process(token):
    return User.decode_access_token(token).value


@token_required
def get_logged_in_user():
    public_id = get_logged_in_user.public_id
    user = User.find_by_public_id(public_id)
    expires_at = get_logged_in_user.expires_at
    user.token_expires_in = expires_at
    return user
