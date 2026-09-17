from fastapi import FastAPI
from routers.productRouter import ProductRouter

app = FastAPI()

app.include_router(ProductRouter)
