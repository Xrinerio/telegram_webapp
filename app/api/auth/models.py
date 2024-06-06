from flask_restx import fields, Model

register_model: dict = {
    "email": fields.String(description="User's email address.", example="test@test.test"),
    "password": fields.String(description="User's password", min_lenght=6, max_lenght=64, example="test")
}

login_model: dict = {
    "email": fields.String(description="User's email address.", example="test@test.test"),
    "password": fields.String(description="User's password", min_lenght=6, max_lenght=64, example="test")
}

gettoken_model: dict = {
    "token": fields.String(description="User's web token.", example="user.token"),
}

user_model = Model(
    "User",
    {
        "email": fields.String,
        "public_id": fields.String,
        "admin": fields.Boolean,
        "registered_on": fields.String(attribute="datetime_str"),
        "token_expires_in": fields.String,
    }
)