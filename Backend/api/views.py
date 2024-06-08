from Users.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import sys

sys.path.append("..")
from Tools.JwtTokens import VerifyToken
from Tools.Exeptions import UserNotFound
from cache.cachTools import SmsCode, Check_code


# برای نمایش این که آیا همچین کاربری وجود داره یا نه
class QueryForGetUser(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        rq_phoneNB = self.kwargs.get("phone_number")
        if rq_phoneNB:
            queryset = User.objects.filter(phone_number=rq_phoneNB)
            if not queryset:
                raise UserNotFound
            return queryset


@api_view(["GET"])
@permission_classes([AllowAny])
def UserSendCode(request, phone_number) -> dict:
    return Response(SmsCode(phone_number))


@api_view(["GET"])
@permission_classes([AllowAny])
def Check_CodeView(request, phone_number, code) -> dict:
    return Response(Check_code(phone_number, code))


@api_view(["GET"])
@permission_classes([AllowAny])
def Verify_token(request, token) -> dict:
    return Response(VerifyToken(token, request))
