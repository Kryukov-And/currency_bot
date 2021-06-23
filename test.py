import unittest

from Parser import Parser


class ParserTest(unittest.TestCase):
    parser = Parser()

    def test_parse_city_found(self):
        self.parser.parse_city("проверка на абакан распознание города в предложении.")
        self.assertEqual(self.parser.get_city_name(), "Абакан")
        self.parser.clear()

    def test_parse_city_not_found(self):
        self.parser.parse_city("проверка на не распознание города в предложении.")
        self.assertEqual(self.parser.get_city_name(), None)
        self.parser.clear()

    def test_parse_currency_found(self):
        self.parser.parse_currency("проверка на распознание фунты валюты в предложении.")
        self.assertEqual(self.parser.get_currency(), "gbp")
        self.parser.clear()

    def test_parse_currency_not_found(self):
        self.parser.parse_city("проверка на не распознание валюты в предложении.")
        self.assertEqual(self.parser.get_city_name(), None)
        self.parser.clear()

    def test_parse_date_found(self):
        self.parser.parse_date("проверка на 20.12.2009 распознание числа в предложении.")
        self.assertEqual(self.parser.get_date(), "20")
        self.parser.clear()

    def test_parse_date_not_found(self):
        self.parser.parse_date("проверка на не распознание числа в предложении.")
        self.assertEqual(self.parser.get_date(), None)
        self.parser.clear()

    def test_parse_month_found(self):
        self.parser.parse_month("проверка на 20.12.2009 распознание месяца в предложении.")
        self.assertEqual(self.parser.get_month(), "12")
        self.parser.clear()

    def test_parse_month_not_found(self):
        self.parser.parse_date("проверка на не распознание месяца в предложении.")
        self.assertEqual(self.parser.get_month(), None)
        self.parser.clear()

    def test_parse_year_found(self):
        self.parser.parse_year("проверка на 20.12.2009 распознание года в предложении.")
        self.assertEqual(self.parser.get_year(), "2009")
        self.parser.clear()

    def test_parse_year_not_found(self):
        self.parser.parse_year("проверка на не распознание года в предложении.")
        self.assertEqual(self.parser.get_year(), None)
        self.parser.clear()


if __name__ == '__main__':
    unittest.main()
