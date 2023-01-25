import unittest

from management.product_handler import get_product_by_id

class TestGetProductByIdRaiseError(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "get_product_by_id"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."

    def test_get_product_by_id_raises_type_error(self):
        """
        Testa se a função `get_product_by_id` 
        levanta um TypeError caso o tipo do parâmetro passado 
        não seja um inteiro.
        """

        msg = self.base_msg % (
            "levantando um `TypeError` caso o parâmetro passado não seja um inteiro",
        )
        with self.assertRaises(TypeError, msg=msg) as err:
            get_product_by_id([1, 2, 3])

        msg = self.base_msg % ("retornando a mensagem apropriada com o TypeError",)
        self.assertEqual(*err.exception.args, "product id must be an int", msg=msg)
