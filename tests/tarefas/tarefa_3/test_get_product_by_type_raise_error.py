import unittest

from management.product_handler import get_product_by_id, get_products_by_type

class TestGetProductByTypeRaiseError(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "get_product_by_id"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."

    def test_get_product_by_type_raises_type_error(self):
        """
        Testa se a função `get_product_by_type` levanta um TypeError caso o tipo do parâmetro passado não seja uma string [0 pts].
        """

        msg = self.base_msg % (
            "levantando um `TypeError` caso o parâmetro passado não seja uma string",
        )
        with self.assertRaises(TypeError, msg=msg) as err:
            get_products_by_type([1, 2, 3])

        msg = self.base_msg % ("retornando a mensagem apropriada com o TypeError",)
        self.assertEqual(*err.exception.args, "product type must be a str", msg=msg)
