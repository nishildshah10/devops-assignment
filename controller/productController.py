from fastapi import Response
from models.productModel import Product

products = []
id = 0

def create_product_controller(product: Product, response: Response):
    global id
    id += 1
    product.id = id
    products.append(product)
    response.status_code = 201
    return {
        "isSuccess": True,
        "message": "Product created successfully",
        "product": product
    }

def get_products_controller():
    return {
        "isSuccess": True,
        "products": products
    }

def get_product_controller(product_id: int, response: Response):
    for product in products:
        if product.id == product_id:
            return {"isSuccess": True, "product": product}

    response.status_code = 404
    return {"isSuccess": False, "message": "Product not found"}

def update_product_controller(product_id: int, product: Product, response: Response):
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            product.id = product_id
            products[i] = product
            return {
                "isSuccess": True,
                "message": "Product updated successfully",
                "product": product
            }

    response.status_code = 404
    return {"isSuccess": False, "message": "Product not found"}

def delete_product_controller(product_id: int, response: Response):
    for i, product in enumerate(products):
        if product.id == product_id:
            deleted_product = products.pop(i)
            return {
                "isSuccess": True,
                "message": "Product deleted successfully",
                "product": deleted_product
            }

    response.status_code = 404
    return {"isSuccess": False, "message": "Product not found"}
