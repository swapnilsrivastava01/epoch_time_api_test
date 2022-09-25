import unittest
import requests
from test.config.constants import VALUE_NULL_MESSAGE, INCORRECT_VALUE_MESSAGE, INCORRECT_FORMAT_MESSAGE, ERROR, URL, \
     INVALID_URL
from test.config.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from test.test_data import invalid_epoch_time_value_request, invalid_format_epoch_time_request, valid_epoch_time_request


class ApiTesting(unittest.TestCase):

    # test success status code
    def test_case_1(self):
        payload = valid_epoch_time_request
        response = requests.get(url=URL, params=payload)
        self.assertTrue(response.status_code, HTTP_200_OK)

    # test request without query parameter
    def test_case_2(self):
        response = requests.get(url=URL)
        self.assertTrue(response.status_code == HTTP_400_BAD_REQUEST)
        self.assertIn(VALUE_NULL_MESSAGE, response.text)

    # test wrong input format for query parameter
    def test_case_3(self):
        payload = invalid_format_epoch_time_request
        response = requests.get(url=URL, params=payload)
        self.assertTrue(response.status_code == HTTP_400_BAD_REQUEST)
        self.assertIn(INCORRECT_FORMAT_MESSAGE, response.text)

    # test boundary value for epoch time
    def test_case_4(self):
        payload = invalid_epoch_time_value_request
        response = requests.get(url=URL, params=payload)
        self.assertTrue(response.status_code == HTTP_400_BAD_REQUEST)
        self.assertIn(INCORRECT_VALUE_MESSAGE, response.text)

    # test incorrect API URL
    def test_case_5(self):
        payload = valid_epoch_time_request
        response = requests.get(url=INVALID_URL, params=payload)
        self.assertTrue(response.status_code, HTTP_500_INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    unittest.main()
