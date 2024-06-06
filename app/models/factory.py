from ..database import db


class Factory(db.Model):

    __tablename__ = "factory"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    private_id = db.Column(db.String(36), unique=True, nullable=False)
    incomes = db.Column(db.String, nullable=False, default=0)


    def __repr__(self):
        return (
            f"<User login={self.email}, cookies={self.cookies}>"
        )

    @classmethod
    def find_by_private_id(cls, private_id):
        return cls.query.filter_by(private_id=private_id).first()

