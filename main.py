from fastapi import FastAPI
from controllers.userController import router as user_router
from controllers.plantController import router as plant_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace ["*"] with your frontend URL(s) in production
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(user_router, prefix="/api/v1")
app.include_router(plant_router, prefix="/api/v1")
