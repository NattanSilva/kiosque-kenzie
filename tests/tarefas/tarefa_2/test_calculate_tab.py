import unittest

from management.tab_handler import calculate_tab


class TestCalculateTab(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "calculate_tab"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."
        cls.tables_set = [
            {
                "expected": {"subtotal": "$188.29"},
                "input": [
                    {"_id": 10, "amount": 3},
                    {"_id": 20, "amount": 2},
                    {"_id": 21, "amount": 5},
                ],
            },
            {
                "expected": {"subtotal": "$183.69"},
                "input": [
                    {"_id": 40, "amount": 4},
                    {"_id": 19, "amount": 5},
                    {"_id": 10, "amount": 3},
                ],
            },
            {
                "expected": {"subtotal": "$113.83"},
                "input": [
                    {"_id": 30, "amount": 1},
                    {"_id": 13, "amount": 3},
                    {"_id": 11, "amount": 2},
                ],
            },
        ]

    def test_calculate_tab_success(self):
        """
        Testa se a função `calculate_tab` 
        retorna adequadamente.
        """
        table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
        result = calculate_tab(table_1)

        msg = self.base_msg % "retornando uma dicionário"
        self.assertIsInstance(result, dict, msg)

        msg = self.base_msg % "retornando corretamente a chave `subtotal`"
        self.assertIsNotNone(result.get("subtotal"), msg)

        expected = {"subtotal": "$216.1"}
        msg = self.base_msg % "retornando corretamente o valor do subtotal"
        self.assertDictEqual(result, expected, msg)

        for index, table in enumerate(self.tables_set, 1):
            with self.subTest(f"Testing table {index}"):
                table_input = table["input"]
                expected = table["expected"]
                result = calculate_tab(table_input)

                msg = self.base_msg % "retornando corretamente o valor do subtotal"
                self.assertDictEqual(result, expected, msg)
