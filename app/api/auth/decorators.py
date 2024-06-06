from functools import wraps

from flask import request, jsonify

from ...models.user import User


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token(admin_only=False)
        print(token_payload)
        for name, val in token_payload.items():
            setattr(decorated, name, val)
        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token(admin_only=True)
        if not token_payload["admin"]:
            raise PermissionError
        for name, val in token_payload.items():
            setattr(decorated, name, val)
        return f(*args, **kwargs)

    return decorated


def _check_access_token(admin_only):
    token = request.headers.get('token')
    if not token:
        raise ModuleNotFoundError
    result = User.decode_access_token(token)
    if result.failure:
        raise TimeoutError
    return result.value
