from menu import products


def maior_id(menu_list):
    maior = 0
    # if len(menu_list) == 0:
    #     return 0
    for item in menu_list:
        if int(item["_id"]) > maior:
            maior = item["_id"]
    return maior


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for item in products:
        if item["_id"] == id:
            return item
    return {}


def get_products_by_type(item_type: str):
    items_list = []
    if type(item_type) != str:
        raise TypeError("product type must be a str")
    for item in products:
        if item["type"] == item_type:
            items_list.append(item)
    return items_list


def add_product(menu_list: list, **kwargs):
    new_item = {"_id": maior_id(menu_list) + 1, **kwargs}
    menu_list.append(new_item)
    return new_item


def includes(vetor, element):
    count = 0
    if len(vetor) == 0:
        return False
    for item in vetor:
        if item == element:
            count += 1
    return count > 0


def count_types(types):
    count = 0
    types_contados = {}
    for value in types:
        for item in products:
            if item["type"] == value:
                count += 1
        types_contados[value] = count
        count = 0
    return types_contados


def most_commom_type():
    types = []
    maior = 0
    maior_tipo = ""
    for item in products:
        if not includes(types, item["type"]):
            types.append(item["type"])

    tipos_contados = count_types(types)

    for key in tipos_contados:
        if tipos_contados[key] > maior:
            maior = tipos_contados[key]
            maior_tipo = key
    return maior_tipo


def menu_report():
    preco_total = 0
    for item in products:
        preco_total += item["price"]
    return f"Products Count: {len(products)} - Average Price: ${round(preco_total / len(products), 2)} - Most Common Type: {most_commom_type()}"
