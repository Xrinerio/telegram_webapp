from marshmallow import Schema, fields


class RegisterSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class LoginSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class GetTokenSchema(Schema):
    token = fields.String(required=True)
