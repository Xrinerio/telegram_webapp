from uuid import uuid4

from ..database import db


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    private_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid4()))
    cookies = db.Column(db.Integer, nullable=False, default=0)
    income_1 = db.Column(db.Integer, nullable=False, default=0)
    income_2 = db.Column(db.Integer, nullable=False, default=0)
    income_3 = db.Column(db.Integer, nullable=False, default=0)
    income_4 = db.Column(db.Integer, nullable=False, default=0)
    income_5 = db.Column(db.Integer, nullable=False, default=0)
    game_trys = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return (
            f"<User login={self.email}, cookies={self.cookies}>"
        )

    @classmethod
    def find_by_login(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_private_id(cls, private_id):
        return cls.query.filter_by(private_id=private_id).first()

