from pydantic import BaseModel


# Create User
class UserCreate(BaseModel):
    phone_number: str
    username: str


class DeleteUser(BaseModel):
    id: int
    code: str


class JWTResponsePaylad(BaseModel):
    Access: str


class JWTRespons(BaseModel):
    phone_number: str
    ExpTime: int
