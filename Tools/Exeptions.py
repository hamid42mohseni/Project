from rest_framework.exceptions import APIException


class SmsSended(APIException):
    status_code = 409
    default_detail = "already sended!"


class UserNotFound(APIException):
    status_code = 400
    default_detail = " User Not Found!"


class CodeErr(APIException):
    status_code = 400
    default_detail = "Somthing is Wrong!"
