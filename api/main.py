from fastapi import FastAPI
from router.users import router as userrouter

App = FastAPI()


App.include_router(userrouter, prefix="/users")
