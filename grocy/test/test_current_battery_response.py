"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.current_battery_response import CurrentBatteryResponse


class TestCurrentBatteryResponse(unittest.TestCase):
    """CurrentBatteryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrentBatteryResponse(self):
        """Test CurrentBatteryResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CurrentBatteryResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()