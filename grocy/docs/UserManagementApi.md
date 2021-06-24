# openapi_client.UserManagementApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UserManagementApi.md#users_get) | **GET** /users | Returns all users
[**users_post**](UserManagementApi.md#users_post) | **POST** /users | Creates a new user
[**users_user_id_delete**](UserManagementApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Deletes the given user
[**users_user_id_permissions_get**](UserManagementApi.md#users_user_id_permissions_get) | **GET** /users/{userId}/permissions | Returns the assigned permissions of the given user
[**users_user_id_permissions_post**](UserManagementApi.md#users_user_id_permissions_post) | **POST** /users/{userId}/permissions | Adds a permission to the given user
[**users_user_id_permissions_put**](UserManagementApi.md#users_user_id_permissions_put) | **PUT** /users/{userId}/permissions | Replaces the assigned permissions of the given user
[**users_user_id_put**](UserManagementApi.md#users_user_id_put) | **PUT** /users/{userId} | Edits the given user


# **users_get**
> [UserDto] users_get()

Returns all users

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import user_management_api
from openapi_client.model.user_dto import UserDto
from openapi_client.model.error500 import Error500
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
    api_instance = user_management_api.UserManagementApi(api_client)
    query = [
        "query[]_example",
    ] # [str] | An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for (optional)
    order = "order_example" # str | A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted) (optional)
    limit = 1 # int | The maximum number of objects to return (optional)
    offset = 1 # int | The number of objects to skip (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all users
        api_response = api_instance.users_get(query=query, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserManagementApi->users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **[str]**| An array of filter conditions, each of them is a string in the form of &#x60;&lt;field&gt;&lt;condition&gt;&lt;value&gt;&#x60; where&lt;br&gt;&#x60;&lt;field&gt;&#x60; is a valid field name&lt;br&gt;&#x60;&lt;condition&gt;&#x60; is a comparison operator, one of&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&#x3D;&#x60; equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!&#x3D;&#x60; not equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;~&#x60; LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!~&#x60; not LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x60; less&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x60; greater&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x3D;&#x60; less or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x3D;&#x60; greater or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;§&#x60; regular expression&lt;br&gt;&#x60;&lt;value&gt;&#x60; is the value to search for | [optional]
 **order** | **str**| A valid field name by which the response should be ordered, use the separator &#x60;:&#x60; to specify the sort order (&#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; when omitted) | [optional]
 **limit** | **int**| The maximum number of objects to return | [optional]
 **offset** | **int**| The number of objects to skip | [optional]

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
**200** | A list of user objects |  -  |
**400** | The operation was not successful |  -  |
**500** | The operation was not successful (possible errors are invalid field names or conditions in filter parameters provided) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> users_post(user)

Creates a new user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import user_management_api
from openapi_client.model.user import User
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
    api_instance = user_management_api.UserManagementApi(api_client)
    user = User(
        id=1,
        username="username_example",
        first_name="first_name_example",
        last_name="last_name_example",
        password="password_example",
        picture_file_name="picture_file_name_example",
        row_created_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # User | A valid user object

    # example passing only required values which don't have defaults set
    try:
        # Creates a new user
        api_instance.users_post(user)
    except openapi_client.ApiException as e:
        print("Exception when calling UserManagementApi->users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| A valid user object |

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

# **users_user_id_delete**
> users_user_id_delete(user_id)

Deletes the given user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import user_management_api
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
    api_instance = user_management_api.UserManagementApi(api_client)
    user_id = 1 # int | A valid user id

    # example passing only required values which don't have defaults set
    try:
        # Deletes the given user
        api_instance.users_user_id_delete(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling UserManagementApi->users_user_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| A valid user id |

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

# **users_user_id_permissions_get**
> [InlineResponse2002] users_user_id_permissions_get(user_id)

Returns the assigned permissions of the given user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import user_management_api
from openapi_client.model.error400 import Error400
from openapi_client.model.inline_response2002 import InlineResponse2002
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
    api_instance = user_management_api.UserManagementApi(api_client)
    user_id = 1 # int | A valid user id

    # example passing only required values which don't have defaults set
    try:
        # Returns the assigned permissions of the given user
        api_response = api_instance.users_user_id_permissions_get(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserManagementApi->users_user_id_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| A valid user id |

### Return type

[**[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of user permission objects |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_permissions_post**
> users_user_id_permissions_post(user_id, inline_object1)

Adds a permission to the given user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import user_management_api
from openapi_client.model.inline_object1 import InlineObject1
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
    api_instance = user_management_api.UserManagementApi(api_client)
    user_id = 1 # int | A valid user id
    inline_object1 = InlineObject1(
        permissions_id=1,
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Adds a permission to the given user
        api_instance.users_user_id_permissions_post(user_id, inline_object1)
    except openapi_client.ApiException as e:
        print("Exception when calling UserManagementApi->users_user_id_permissions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| A valid user id |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

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

# **users_user_id_permissions_put**
> users_user_id_permissions_put(user_id, inline_object)

Replaces the assigned permissions of the given user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import user_management_api
from openapi_client.model.inline_object import InlineObject
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
    api_instance = user_management_api.UserManagementApi(api_client)
    user_id = 1 # int | A valid user id
    inline_object = InlineObject(
        permissions=[
            1,
        ],
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Replaces the assigned permissions of the given user
        api_instance.users_user_id_permissions_put(user_id, inline_object)
    except openapi_client.ApiException as e:
        print("Exception when calling UserManagementApi->users_user_id_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| A valid user id |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

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

# **users_user_id_put**
> users_user_id_put(user_id, user)

Edits the given user

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import user_management_api
from openapi_client.model.user import User
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
    api_instance = user_management_api.UserManagementApi(api_client)
    user_id = 1 # int | A valid user id
    user = User(
        id=1,
        username="username_example",
        first_name="first_name_example",
        last_name="last_name_example",
        password="password_example",
        picture_file_name="picture_file_name_example",
        row_created_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # User | A valid user object

    # example passing only required values which don't have defaults set
    try:
        # Edits the given user
        api_instance.users_user_id_put(user_id, user)
    except openapi_client.ApiException as e:
        print("Exception when calling UserManagementApi->users_user_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| A valid user id |
 **user** | [**User**](User.md)| A valid user object |

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

