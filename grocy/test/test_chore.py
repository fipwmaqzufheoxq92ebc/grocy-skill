"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.chore import Chore


class TestChore(unittest.TestCase):
    """Chore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChore(self):
        """Test Chore"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Chore()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
