from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from Data.data import Vehicles
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/Data", StaticFiles(directory="Data"), name="data")

@app.get("/Videos")
async def get_videos():
    return Vehicles


@app.get("/Video/{id}")
async def get_video(id: int):
    return Vehicles[id]
