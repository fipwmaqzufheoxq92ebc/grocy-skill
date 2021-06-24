# openapi_client.SystemApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_config_get**](SystemApi.md#system_config_get) | **GET** /system/config | Returns all config settings
[**system_db_changed_time_get**](SystemApi.md#system_db_changed_time_get) | **GET** /system/db-changed-time | Returns the time when the database was last changed
[**system_info_get**](SystemApi.md#system_info_get) | **GET** /system/info | Returns information about the installed grocy, PHP and SQLite version
[**system_log_missing_localization_post**](SystemApi.md#system_log_missing_localization_post) | **POST** /system/log-missing-localization | Logs a missing localization string
[**system_time_get**](SystemApi.md#system_time_get) | **GET** /system/time | Returns the current server time


# **system_config_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} system_config_get()

Returns all config settings

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import system_api
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
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all config settings
        api_response = api_instance.system_config_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemApi->system_config_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key/value pairs of config settings |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_db_changed_time_get**
> DbChangedTimeResponse system_db_changed_time_get()

Returns the time when the database was last changed

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import system_api
from openapi_client.model.db_changed_time_response import DbChangedTimeResponse
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
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the time when the database was last changed
        api_response = api_instance.system_db_changed_time_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemApi->system_db_changed_time_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DbChangedTimeResponse**](DbChangedTimeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An DbChangedTimeResponse object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_info_get**
> InlineResponse200 system_info_get()

Returns information about the installed grocy, PHP and SQLite version

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import system_api
from openapi_client.model.inline_response200 import InlineResponse200
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
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns information about the installed grocy, PHP and SQLite version
        api_response = api_instance.system_info_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemApi->system_info_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An DbChangedTimeResponse object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_log_missing_localization_post**
> system_log_missing_localization_post(missing_localization_request)

Logs a missing localization string

Only when MODE == 'dev', so should only be called then

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import system_api
from openapi_client.model.missing_localization_request import MissingLocalizationRequest
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
    api_instance = system_api.SystemApi(api_client)
    missing_localization_request = MissingLocalizationRequest(
        text="text_example",
    ) # MissingLocalizationRequest | A valid MissingLocalizationRequest object

    # example passing only required values which don't have defaults set
    try:
        # Logs a missing localization string
        api_instance.system_log_missing_localization_post(missing_localization_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemApi->system_log_missing_localization_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **missing_localization_request** | [**MissingLocalizationRequest**](MissingLocalizationRequest.md)| A valid MissingLocalizationRequest object |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The operation was successful |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_get**
> TimeResponse system_time_get()

Returns the current server time

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import system_api
from openapi_client.model.time_response import TimeResponse
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
    api_instance = system_api.SystemApi(api_client)
    offset = 1 # int | Offset of timestamp in seconds. Can be positive or negative. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the current server time
        api_response = api_instance.system_time_get(offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemApi->system_time_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset of timestamp in seconds. Can be positive or negative. | [optional]

### Return type

[**TimeResponse**](TimeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A TimeResponse object |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

