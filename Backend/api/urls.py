from django.urls import path, include
from .views import QueryForGetUser, UserSendCode, Check_CodeView, Verify_token
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/user/<str:phone_number>/", QueryForGetUser.as_view()),
    path("api/user/send/<str:phone_number>/", UserSendCode),
    path("api/user/check/<str:phone_number>/<str:code>/", Check_CodeView),
    path("api/user/verify/<str:token>/", Verify_token),
    path("api/user/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("api/auth/", include("rest_framework.urls")),
]
