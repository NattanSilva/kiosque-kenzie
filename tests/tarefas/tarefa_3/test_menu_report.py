import unittest

from management.product_handler import menu_report


class TestMenuReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "menu_report"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."

    def test_menu_report_success(self):
        """
        Testa se a função `menu_report` retorna os 
        logs corretamente.
        """
        result = menu_report()
        expected = "Products Count: 50 - Average Price: $20.8 - Most Common Type: fruit"

        msg = self.base_msg % "retornando a mensagem adequada com os valores corretos"
        self.assertEqual(result, expected, msg)
