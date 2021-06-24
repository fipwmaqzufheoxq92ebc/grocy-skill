# openapi_client.CurrentUserApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get**](CurrentUserApi.md#user_get) | **GET** /user | Returns the currently authenticated user
[**user_settings_get**](CurrentUserApi.md#user_settings_get) | **GET** /user/settings | Returns all settings of the currently logged in user
[**user_settings_setting_key_delete**](CurrentUserApi.md#user_settings_setting_key_delete) | **DELETE** /user/settings/{settingKey} | Deletes the given setting of the currently logged in user
[**user_settings_setting_key_get**](CurrentUserApi.md#user_settings_setting_key_get) | **GET** /user/settings/{settingKey} | Returns the given setting of the currently logged in user
[**user_settings_setting_key_put**](CurrentUserApi.md#user_settings_setting_key_put) | **PUT** /user/settings/{settingKey} | Sets the given setting of the currently logged in user


# **user_get**
> [UserDto] user_get()

Returns the currently authenticated user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import current_user_api
from openapi_client.model.user_dto import UserDto
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
    api_instance = current_user_api.CurrentUserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the currently authenticated user
        api_response = api_instance.user_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentUserApi->user_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserDto]**](UserDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A user object |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} user_settings_get()

Returns all settings of the currently logged in user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import current_user_api
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
    api_instance = current_user_api.CurrentUserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all settings of the currently logged in user
        api_response = api_instance.user_settings_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentUserApi->user_settings_get: %s\n" % e)
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
**200** | Key/value pairs of user settings |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_setting_key_delete**
> user_settings_setting_key_delete(setting_key)

Deletes the given setting of the currently logged in user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import current_user_api
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
    api_instance = current_user_api.CurrentUserApi(api_client)
    setting_key = "settingKey_example" # str | The key of the user setting

    # example passing only required values which don't have defaults set
    try:
        # Deletes the given setting of the currently logged in user
        api_instance.user_settings_setting_key_delete(setting_key)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentUserApi->user_settings_setting_key_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_key** | **str**| The key of the user setting |

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
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_setting_key_get**
> UserSetting user_settings_setting_key_get(setting_key)

Returns the given setting of the currently logged in user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import current_user_api
from openapi_client.model.user_setting import UserSetting
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
    api_instance = current_user_api.CurrentUserApi(api_client)
    setting_key = "settingKey_example" # str | The key of the user setting

    # example passing only required values which don't have defaults set
    try:
        # Returns the given setting of the currently logged in user
        api_response = api_instance.user_settings_setting_key_get(setting_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentUserApi->user_settings_setting_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_key** | **str**| The key of the user setting |

### Return type

[**UserSetting**](UserSetting.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A UserSetting object |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_setting_key_put**
> user_settings_setting_key_put(setting_key, user_setting)

Sets the given setting of the currently logged in user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import current_user_api
from openapi_client.model.user_setting import UserSetting
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
    api_instance = current_user_api.CurrentUserApi(api_client)
    setting_key = "settingKey_example" # str | The key of the user setting
    user_setting = UserSetting(
        value="value_example",
    ) # UserSetting | A valid UserSetting object

    # example passing only required values which don't have defaults set
    try:
        # Sets the given setting of the currently logged in user
        api_instance.user_settings_setting_key_put(setting_key, user_setting)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentUserApi->user_settings_setting_key_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_key** | **str**| The key of the user setting |
 **user_setting** | [**UserSetting**](UserSetting.md)| A valid UserSetting object |

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

