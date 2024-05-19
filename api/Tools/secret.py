from passlib.context import CryptContext

PasswordManager = CryptContext(schemes=["bcrypt"], deprecated="auto")
