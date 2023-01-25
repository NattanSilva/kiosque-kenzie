import unittest

from management.product_handler import add_product

from tests.data.original_menu import original_products


class TestAddProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "add_product"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."

    def test_can_add_product(self):
        """
        Testa se a função `add_product` 
        adiciona e retorna o produto adicionado corretamente.
        """
        new_product = {
            "title": "Bolinho JS",
            "price": 1.0,
            "rating": 2,
            "description": "Bolinho de JS com cenoura",
            "type": "bakery",
        }

        result = add_product(original_products, **new_product)
        expected = {
            "_id": 51,
            "title": "Bolinho JS",
            "price": 1.0,
            "rating": 2,
            "description": "Bolinho de JS com cenoura",
            "type": "bakery",
        }

        msg = self.base_msg % "retornando um dicionário"
        self.assertIsInstance(result, dict, msg)

        msg = self.base_msg % ("retornando corretamente o produto adicionado",)
        self.assertDictEqual(result, expected, msg)

        msg = self.base_msg % ("adicionando corretamente o produto ao menu",)
        self.assertDictEqual(original_products[-1], expected, msg)

    def test_add_product_with_empty_menu(self):
        """
        Testa se a função `add_product` gera um id, 
        adiciona e retorna corretamente com um menu vazio.
        """
        new_product = {
            "title": "Suco de React",
            "price": 5.0,
            "rating": 4,
            "description": "Suco de React com Limao",
            "type": "drink",
        }
        empty_list = []
        result = add_product(empty_list, **new_product)
        expected = {
            "_id": 1,
            "title": "Suco de React",
            "price": 5.0,
            "rating": 4,
            "description": "Suco de React com Limao",
            "type": "drink",
        }

        msg = self.base_msg % "adicionando corretamente o produto ao menu vazio"
        self.assertDictEqual(empty_list[-1], expected, msg)
