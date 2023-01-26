from menu import products


def maior_id(menu_list):
    maior = 0
    if len(menu_list) == 0:
        return 0
    for item in menu_list:
        if int(item["_id"]) > maior:
            maior = item["_id"]
    return maior


def get_product_by_id(id: int):
    for item in products:
        if item["_id"] == id:
            return item
    return {}


def get_products_by_type(type: str):
    items_list = []
    for item in products:
        if item["type"] == type:
            items_list.append(item)
    return items_list


def add_product(menu_list: list, **test):
    new_item = {"_id": maior_id(menu_list) + 1, **test}
    menu_list.append(new_item)
    return new_item
