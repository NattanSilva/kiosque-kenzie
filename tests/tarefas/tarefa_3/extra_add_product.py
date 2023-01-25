import unittest

from management.product_handler import add_product_extra

from ...data import original_products


class TestExtraAddProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "add_product_extra"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."

    def test_extra_can_add_product(self):
        """
        Testa se a função `add_product_extra` 
        adiciona e retorna o produto adicionado 
        corretamente.
        """
        required_keys = ("description", "price", "rating", "title", "type")
        new_product = {
            "title": "Bolinho JS",
            "price": 1.0,
            "rating": 2,
            "description": "Bolinho de JS com cenoura",
            "type": "bakery",
        }

        result = add_product_extra(original_products, *required_keys, **new_product)
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

    def test_extra_add_product_with_empty_menu(self):
        """
        Testa se a função `add_product_extra` gera um id, 
        adiciona e retorna corretamente com um menu vazio.
        """
        required_keys = ("description", "price", "rating", "title", "type")
        new_product = {
            "title": "Suco de React",
            "price": 5.0,
            "rating": 4,
            "description": "Suco de React com Limao",
            "type": "drink",
        }
        empty_list = []
        result = add_product_extra(empty_list, *required_keys, **new_product)
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

    def test_extra_add_product_required_keys(self):
        """
        Testa se a função `add_product_extra` 
        levanta um KeyError caso alguma chave obrigatória 
        não seja passada no produto.
        """

        required_keys = ["price", "rating", "title", "type", "description"]
        missing_description_product = {
            "title": "Suco de React",
            "price": 5.0,
            "rating": 4,
            "type": "drink",
        }
        empty_list = []

        msg = self.base_msg % (
            "levantando um `KeyError` caso alguma chave obrigatória nao seja passada",
        )

        for key in required_keys.copy():
            with self.subTest(f"Testing with required key: {key}"):
                with self.assertRaises(KeyError, msg=msg) as err:
                    add_product_extra(
                        empty_list,
                        *(key,),
                        **{},
                    )

                msg = self.base_msg % (
                    "retornando a mensagem apropriada com o KeyError",
                )
                self.assertEqual(
                    *err.exception.args, f"field {key} is required", msg=msg
                )
            required_keys.remove(key)

        msg = self.base_msg % (
            "deixando o menu intacto quando um KeyError é levantado",
        )
        self.assertListEqual(empty_list, [], msg=msg)

    def test_extra_add_product_with_extra_keys(self):
        """
        Testa se a função `add_product_extra` 
        exclui chaves não obrigatórias antes de adicionar o 
        produto ao menu.
        """
        required_keys = ("description", "price", "rating", "title", "type")
        new_product = {
            "title": "Suco de React",
            "price": 5.0,
            "rating": 4,
            "description": "Suco de React com Limao",
            "type": "drink",
            "extra_key_1": "value_1",
            "extra_key_2": "value_2",
        }
        empty_list = []
        result = add_product_extra(empty_list, *required_keys, **new_product)
        expected = {
            "_id": 1,
            "title": "Suco de React",
            "price": 5.0,
            "rating": 4,
            "description": "Suco de React com Limao",
            "type": "drink",
        }

        msg = (
            self.base_msg
            % "excluindo corretamente as chaves não obrigatórias antes de adicionar o produto ao menu"
        )
        self.assertDictEqual(empty_list[-1], expected, msg)
