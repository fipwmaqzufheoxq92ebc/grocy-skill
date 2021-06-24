# openapi_client.CalendarApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_ical_get**](CalendarApi.md#calendar_ical_get) | **GET** /calendar/ical | Returns the calendar in iCal format
[**calendar_ical_sharing_link_get**](CalendarApi.md#calendar_ical_sharing_link_get) | **GET** /calendar/ical/sharing-link | Returns a (public) sharing link for the calendar in iCal format


# **calendar_ical_get**
> str calendar_ical_get()

Returns the calendar in iCal format

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import calendar_api
from openapi_client.model.error400 import Error400
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8111/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8111/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = calendar_api.CalendarApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the calendar in iCal format
        api_response = api_instance.calendar_ical_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CalendarApi->calendar_ical_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/calendar, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The iCal file contents |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_ical_sharing_link_get**
> InlineResponse2003 calendar_ical_sharing_link_get()

Returns a (public) sharing link for the calendar in iCal format

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import calendar_api
from openapi_client.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8111/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8111/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = calendar_api.CalendarApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a (public) sharing link for the calendar in iCal format
        api_response = api_instance.calendar_ical_sharing_link_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CalendarApi->calendar_ical_sharing_link_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The (public) sharing link for the calendar in iCal format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

