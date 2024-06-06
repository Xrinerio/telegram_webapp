from flask_restx import Api

from .auth.auth import api as ns1

api: Api = Api(doc="/api/doc", prefix="/api/", version="1.0", title="TicTacToe API", description="---")

api.add_namespace(ns1)