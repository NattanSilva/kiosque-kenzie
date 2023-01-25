import unittest

from management.product_handler import get_products_by_type


class TestGetProductByType(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "get_product_by_type"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."

    def test_can_get_product_by_type(self):
        """
        Testa se a função `get_product_by_type` retorna 
        os produtos de determinado tipo corretamente.
        """
        result = get_products_by_type("drink")
        expected = [
            {
                "_id": 32,
                "description": "Mix of rum, lemon juice, mint, sugar and sparking water",
                "price": 27.61,
                "rating": 4,
                "title": "Mojito",
                "type": "drink",
            },
            {
                "_id": 37,
                "description": "Homemade cola drink with lemon juice and 2 ice cubes",
                "price": 28.96,
                "rating": 5,
                "title": "Fresh Nuka-Cola",
                "type": "drink",
            },
        ]

        msg = self.base_msg % "retornando uma lista"
        self.assertIsInstance(result, list, msg)

        msg = self.base_msg % ("retornando corretamente os produtos encontrados",)
        self.assertListEqual(result, expected, msg)

    def test_get_product_by_type_with_non_existing_type(self):
        """
        Testa se a função `get_product_by_type` retorna 
        uma lista vazia caso não exista nenhum produto do tipo.
        """
        result = get_products_by_type("non_existing_type_10000")
        expected = []

        msg = self.base_msg % "retornando uma lista"
        self.assertIsInstance(result, list, msg)

        msg = (
            self.base_msg
            % "retornando uma lista vazia caso não existam produtos do tipo passado",
        )

        self.assertListEqual(result, expected, msg)

    
