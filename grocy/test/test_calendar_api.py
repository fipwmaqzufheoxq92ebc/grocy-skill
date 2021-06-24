"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.calendar_api import CalendarApi  # noqa: E501


class TestCalendarApi(unittest.TestCase):
    """CalendarApi unit test stubs"""

    def setUp(self):
        self.api = CalendarApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_calendar_ical_get(self):
        """Test case for calendar_ical_get

        Returns the calendar in iCal format  # noqa: E501
        """
        pass

    def test_calendar_ical_sharing_link_get(self):
        """Test case for calendar_ical_sharing_link_get

        Returns a (public) sharing link for the calendar in iCal format  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
