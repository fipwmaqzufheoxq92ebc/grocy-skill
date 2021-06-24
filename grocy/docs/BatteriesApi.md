# openapi_client.BatteriesApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batteries_battery_id_charge_post**](BatteriesApi.md#batteries_battery_id_charge_post) | **POST** /batteries/{batteryId}/charge | Tracks a charge cycle of the given battery
[**batteries_battery_id_get**](BatteriesApi.md#batteries_battery_id_get) | **GET** /batteries/{batteryId} | Returns details of the given battery
[**batteries_charge_cycles_charge_cycle_id_undo_post**](BatteriesApi.md#batteries_charge_cycles_charge_cycle_id_undo_post) | **POST** /batteries/charge-cycles/{chargeCycleId}/undo | Undoes a battery charge cycle
[**batteries_get**](BatteriesApi.md#batteries_get) | **GET** /batteries | Returns all batteries incl. the next estimated charge time per battery


# **batteries_battery_id_charge_post**
> BatteryChargeCycleEntry batteries_battery_id_charge_post(battery_id, inline_object22)

Tracks a charge cycle of the given battery

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import batteries_api
from openapi_client.model.inline_object22 import InlineObject22
from openapi_client.model.battery_charge_cycle_entry import BatteryChargeCycleEntry
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
    api_instance = batteries_api.BatteriesApi(api_client)
    battery_id = 1 # int | A valid battery id
    inline_object22 = InlineObject22(
        tracked_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # InlineObject22 | 

    # example passing only required values which don't have defaults set
    try:
        # Tracks a charge cycle of the given battery
        api_response = api_instance.batteries_battery_id_charge_post(battery_id, inline_object22)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BatteriesApi->batteries_battery_id_charge_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **battery_id** | **int**| A valid battery id |
 **inline_object22** | [**InlineObject22**](InlineObject22.md)|  |

### Return type

[**BatteryChargeCycleEntry**](BatteryChargeCycleEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing battery) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batteries_battery_id_get**
> BatteryDetailsResponse batteries_battery_id_get(battery_id)

Returns details of the given battery

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import batteries_api
from openapi_client.model.battery_details_response import BatteryDetailsResponse
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
    api_instance = batteries_api.BatteriesApi(api_client)
    battery_id = 1 # int | A valid battery id

    # example passing only required values which don't have defaults set
    try:
        # Returns details of the given battery
        api_response = api_instance.batteries_battery_id_get(battery_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BatteriesApi->batteries_battery_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **battery_id** | **int**| A valid battery id |

### Return type

[**BatteryDetailsResponse**](BatteryDetailsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A BatteryDetailsResponse object |  -  |
**400** | The operation was not successful (possible errors are: Not existing battery) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batteries_charge_cycles_charge_cycle_id_undo_post**
> batteries_charge_cycles_charge_cycle_id_undo_post(charge_cycle_id)

Undoes a battery charge cycle

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import batteries_api
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
    api_instance = batteries_api.BatteriesApi(api_client)
    charge_cycle_id = 1 # int | A valid charge cycle id

    # example passing only required values which don't have defaults set
    try:
        # Undoes a battery charge cycle
        api_instance.batteries_charge_cycles_charge_cycle_id_undo_post(charge_cycle_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BatteriesApi->batteries_charge_cycles_charge_cycle_id_undo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_cycle_id** | **int**| A valid charge cycle id |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing booking) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batteries_get**
> [CurrentBatteryResponse] batteries_get()

Returns all batteries incl. the next estimated charge time per battery

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import batteries_api
from openapi_client.model.error500 import Error500
from openapi_client.model.current_battery_response import CurrentBatteryResponse
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
    api_instance = batteries_api.BatteriesApi(api_client)
    query = [
        "query[]_example",
    ] # [str] | An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for (optional)
    order = "order_example" # str | A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted) (optional)
    limit = 1 # int | The maximum number of objects to return (optional)
    offset = 1 # int | The number of objects to skip (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all batteries incl. the next estimated charge time per battery
        api_response = api_instance.batteries_get(query=query, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BatteriesApi->batteries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **[str]**| An array of filter conditions, each of them is a string in the form of &#x60;&lt;field&gt;&lt;condition&gt;&lt;value&gt;&#x60; where&lt;br&gt;&#x60;&lt;field&gt;&#x60; is a valid field name&lt;br&gt;&#x60;&lt;condition&gt;&#x60; is a comparison operator, one of&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&#x3D;&#x60; equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!&#x3D;&#x60; not equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;~&#x60; LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!~&#x60; not LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x60; less&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x60; greater&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x3D;&#x60; less or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x3D;&#x60; greater or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;§&#x60; regular expression&lt;br&gt;&#x60;&lt;value&gt;&#x60; is the value to search for | [optional]
 **order** | **str**| A valid field name by which the response should be ordered, use the separator &#x60;:&#x60; to specify the sort order (&#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; when omitted) | [optional]
 **limit** | **int**| The maximum number of objects to return | [optional]
 **offset** | **int**| The number of objects to skip | [optional]

### Return type

[**[CurrentBatteryResponse]**](CurrentBatteryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of CurrentBatteryResponse objects |  -  |
**500** | The operation was not successful (possible errors are invalid field names or conditions in filter parameters provided) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

