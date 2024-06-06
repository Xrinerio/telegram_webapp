from ..models.user import User
from ..database import db

def take_user_info(private_id):
    user = User.find_by_private_id(private_id)
    info = {
        "login" : user.login,
        "admin" : user.admin,
        "private_id" : user.private_id,
        "cookies" : user.cookies,
        "income_1" : user.income_1,
        "income_2" : user.income_2,
        "income_3" : user.income_3,
        "income_4" : user.income_4,
        "income_5" : user.income_5,
        "game_trys" : user.game_trys
    }
    return info