"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.stock_transaction_type import StockTransactionType
globals()['StockTransactionType'] = StockTransactionType
from openapi_client.model.inline_object3 import InlineObject3


class TestInlineObject3(unittest.TestCase):
    """InlineObject3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineObject3(self):
        """Test InlineObject3"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineObject3()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
