import unittest
# from app import app
import sys
sys.path.append("..")
from address_parser.app import app



class ParserTestCase(unittest.TestCase):

    def test_parser_endpoint_simple_case_1(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': 'Winterallee 3'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        print(f"response = {response.get_json()}")
        self.assertDictEqual(response.json, {"street": "Winterallee", "housenumber": "3"})

    def test_parser_endpoint_simple_case_2(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': 'Musterstrasse 45'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "Musterstrasse", "housenumber": "45"})

    def test_parser_endpoint_simple_case_3(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': 'Blaufeldweg 123B'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "Blaufeldweg", "housenumber": "123B"})

    def test_parser_endpoint_medium_case_1(self):
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': 'Am Bächle 23'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "Am Bächle", "housenumber": "23"})

    def test_parser_endpoint_medium_case_2(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': 'Auf der Vogelwiese 23 b'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "Auf der Vogelwiese", "housenumber": "23 b"})


    def test_parser_endpoint_complex_case_1(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': '4, rue de la revolution'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "rue de la revolution", "housenumber": "4"})

    def test_parser_endpoint_complex_case_2(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': '200 Broadway Av'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "Broadway Av", "housenumber": "200"})

    def test_parser_endpoint_complex_case_3(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': 'Calle Aduana, 29'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "Calle Aduana", "housenumber": "29"})

    def test_parser_endpoint_complex_case_4(self):
        app.testing = True
        client = app.test_client()
        response = client.post('/parser-complex/', data={'input_address': 'Calle 39 No 1540'})  # Use the client instance, not self.client
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, {"street": "Calle 39", "housenumber": "No 1540"})

    def test_parser_endpoint_with_incorrect_format(self):
        client = app.test_client()  # Create a new client instance
        response = client.post('/parser-complex/', data={'input_address': 'Invalid Address'})  # Use the client instance
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()