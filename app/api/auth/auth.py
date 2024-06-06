from flask_restx import Namespace, Resource
from flask import request
from marshmallow import ValidationError


from .schema import RegisterSchema, LoginSchema, GetTokenSchema
from .process import registration_process, login_process, get_token_process, get_logged_in_user
from .models import register_model, login_model, gettoken_model, user_model

api: Namespace = Namespace("Auth",
                           description="Authentication endpoints",
                           path="/auth/")
api.models[user_model.name] = user_model


@api.route("/reg")
class Register(Resource):

    @api.expect(api.model("Registration", register_model, strict=True))
    def post(self):
        try:
            payload: dict = RegisterSchema().load(request.get_json())
            email = payload.get("email")
            password = payload.get("password")

            return registration_process(email, password), 200
        except ValidationError:
            return {"zapros": "govno"}, 400


@api.route("/log")
class Login(Resource):

    @api.expect(api.model("Login", login_model, strict=True))
    def post(self):
        try:
            payload: dict = LoginSchema().load(request.get_json())
            email = payload.get("email")
            password = payload.get("password")

            return login_process(email, password), 200
        except ValidationError:
            return {"zapros": "govno"}, 400


@api.route("/dectok")
class GetToken(Resource):

    @api.expect(api.model("Check token", gettoken_model, strict=True))
    def post(self):
        try:
            payload: dict = GetTokenSchema().load(request.get_json())
            token = payload.get("token")

            return get_token_process(token), 200
        except ValidationError:
            return {"zapros": "govno"}, 400
        

@api.route("/users")
class GetUsers(Resource):
    @api.marshal_with(user_model)
    @api.response(401, "UNAUTHORIZED")
    
    def get(self):
        return get_logged_in_user()