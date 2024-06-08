from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, Token
from Tools.Exeptions import UserNotFound
from Users.models import User


def AccessTokenCustom(phone_number):
    user = User.objects.get(phone_number=phone_number)
    if not user:
        raise UserNotFound

    accsesstoken = AccessToken.for_user(user)
    refreshtoken = RefreshToken.for_user(user)

    return {
        "accesstoken": str(accsesstoken),
        "refreshtoken": str(refreshtoken),
    }


def VerifyToken(token, test):
    try:
        if Token(token).check_exp():
            return {"detail": token}
        else:
            raise UserNotFound
    except UserNotFound:
        # در صورت بروز خطا در توکن، خطای احراز هویت را برگردانید
        raise UserNotFound
