from menu import products


def find_product_price(id: int):
    for item in products:
        if int(item["_id"]) == id:
            return item["price"]


def calculate_tab(lista: list):
    subtotal = {"subtotal": 0}
    total = 0
    for item in lista:
        total += (
            find_product_price(int(item["_id"])) * int(item["amount"])
            )
    subtotal["subtotal"] = round(total, 2)
    return subtotal
