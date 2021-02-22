from fastapi import FastAPI

from mine_dns.routers import router

app = FastAPI()

app.include_router(router)
