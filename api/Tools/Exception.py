from fastapi import HTTPException, status


class UserExeption(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User Not Found!"


class PhoneNumberInNotCorrect(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User Not Found!"


class SmsNotCorrect(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "SMS Not Correct!"


class SmsSended(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_200_OK
        self.detail = "Already provided"
