# openapi_client.PrintApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**print_shoppinglist_thermal_get**](PrintApi.md#print_shoppinglist_thermal_get) | **GET** /print/shoppinglist/thermal | Prints the shoppinglist with a thermal printer


# **print_shoppinglist_thermal_get**
> InlineResponse2004 print_shoppinglist_thermal_get()

Prints the shoppinglist with a thermal printer

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import print_api
from openapi_client.model.inline_response2004 import InlineResponse2004
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
    api_instance = print_api.PrintApi(api_client)
    list = 1 # int | Shopping list id (optional) if omitted the server will use the default value of 1
    print_header = True # bool | Prints grocy logo if true (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Prints the shoppinglist with a thermal printer
        api_response = api_instance.print_shoppinglist_thermal_get(list=list, print_header=print_header)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PrintApi->print_shoppinglist_thermal_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **int**| Shopping list id | [optional] if omitted the server will use the default value of 1
 **print_header** | **bool**| Prints grocy logo if true | [optional] if omitted the server will use the default value of True

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns OK if the printing was successful |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

