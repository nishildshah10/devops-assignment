from fastapi import APIRouter, Response
from models.productModel import Product

from controller.productController import (
    create_product_controller,
    get_products_controller,
    get_product_controller,
    update_product_controller,
    delete_product_controller
)

ProductRouter = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@ProductRouter.post("/")
def create_product(product: Product, response: Response):
    return create_product_controller(product, response)

@ProductRouter.get("/")
def get_products():
    return get_products_controller()

@ProductRouter.get("/{product_id}")
def get_product(product_id: int, response: Response):
    return get_product_controller(product_id, response)

@ProductRouter.put("/{product_id}")
def update_product(product_id: int, product: Product, response: Response):
    return update_product_controller(product_id, product, response)

@ProductRouter.delete("/{product_id}")
def delete_product(product_id: int, response: Response):
    return delete_product_controller(product_id, response)
