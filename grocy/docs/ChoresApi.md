# openapi_client.ChoresApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chores_chore_id_execute_post**](ChoresApi.md#chores_chore_id_execute_post) | **POST** /chores/{choreId}/execute | Tracks an execution of the given chore
[**chores_chore_id_get**](ChoresApi.md#chores_chore_id_get) | **GET** /chores/{choreId} | Returns details of the given chore
[**chores_executions_calculate_next_assignments_post**](ChoresApi.md#chores_executions_calculate_next_assignments_post) | **POST** /chores/executions/calculate-next-assignments | (Re)calculates all next user assignments of all chores
[**chores_executions_execution_id_undo_post**](ChoresApi.md#chores_executions_execution_id_undo_post) | **POST** /chores/executions/{executionId}/undo | Undoes a chore execution
[**chores_get**](ChoresApi.md#chores_get) | **GET** /chores | Returns all chores incl. the next estimated execution time per chore


# **chores_chore_id_execute_post**
> ChoreLogEntry chores_chore_id_execute_post(chore_id, inline_object20)

Tracks an execution of the given chore

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import chores_api
from openapi_client.model.chore_log_entry import ChoreLogEntry
from openapi_client.model.error400 import Error400
from openapi_client.model.inline_object20 import InlineObject20
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
    api_instance = chores_api.ChoresApi(api_client)
    chore_id = 1 # int | A valid chore id
    inline_object20 = InlineObject20(
        tracked_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        done_by=1,
    ) # InlineObject20 | 

    # example passing only required values which don't have defaults set
    try:
        # Tracks an execution of the given chore
        api_response = api_instance.chores_chore_id_execute_post(chore_id, inline_object20)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChoresApi->chores_chore_id_execute_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chore_id** | **int**| A valid chore id |
 **inline_object20** | [**InlineObject20**](InlineObject20.md)|  |

### Return type

[**ChoreLogEntry**](ChoreLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing chore) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chores_chore_id_get**
> ChoreDetailsResponse chores_chore_id_get(chore_id)

Returns details of the given chore

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import chores_api
from openapi_client.model.chore_details_response import ChoreDetailsResponse
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
    api_instance = chores_api.ChoresApi(api_client)
    chore_id = 1 # int | A valid chore id

    # example passing only required values which don't have defaults set
    try:
        # Returns details of the given chore
        api_response = api_instance.chores_chore_id_get(chore_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChoresApi->chores_chore_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chore_id** | **int**| A valid chore id |

### Return type

[**ChoreDetailsResponse**](ChoreDetailsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A ChoreDetailsResponse object |  -  |
**400** | The operation was not successful (possible errors are: Not existing chore) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chores_executions_calculate_next_assignments_post**
> chores_executions_calculate_next_assignments_post()

(Re)calculates all next user assignments of all chores

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import chores_api
from openapi_client.model.inline_object21 import InlineObject21
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
    api_instance = chores_api.ChoresApi(api_client)
    inline_object21 = InlineObject21(
        chore_id=1,
    ) # InlineObject21 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # (Re)calculates all next user assignments of all chores
        api_instance.chores_executions_calculate_next_assignments_post(inline_object21=inline_object21)
    except openapi_client.ApiException as e:
        print("Exception when calling ChoresApi->chores_executions_calculate_next_assignments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object21** | [**InlineObject21**](InlineObject21.md)|  | [optional]

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

# **chores_executions_execution_id_undo_post**
> chores_executions_execution_id_undo_post(execution_id)

Undoes a chore execution

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import chores_api
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
    api_instance = chores_api.ChoresApi(api_client)
    execution_id = 1 # int | A valid chore execution id

    # example passing only required values which don't have defaults set
    try:
        # Undoes a chore execution
        api_instance.chores_executions_execution_id_undo_post(execution_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChoresApi->chores_executions_execution_id_undo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **int**| A valid chore execution id |

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

# **chores_get**
> [CurrentChoreResponse] chores_get()

Returns all chores incl. the next estimated execution time per chore

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import chores_api
from openapi_client.model.current_chore_response import CurrentChoreResponse
from openapi_client.model.error500 import Error500
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
    api_instance = chores_api.ChoresApi(api_client)
    query = [
        "query[]_example",
    ] # [str] | An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for (optional)
    order = "order_example" # str | A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted) (optional)
    limit = 1 # int | The maximum number of objects to return (optional)
    offset = 1 # int | The number of objects to skip (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all chores incl. the next estimated execution time per chore
        api_response = api_instance.chores_get(query=query, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChoresApi->chores_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **[str]**| An array of filter conditions, each of them is a string in the form of &#x60;&lt;field&gt;&lt;condition&gt;&lt;value&gt;&#x60; where&lt;br&gt;&#x60;&lt;field&gt;&#x60; is a valid field name&lt;br&gt;&#x60;&lt;condition&gt;&#x60; is a comparison operator, one of&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&#x3D;&#x60; equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!&#x3D;&#x60; not equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;~&#x60; LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!~&#x60; not LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x60; less&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x60; greater&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x3D;&#x60; less or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x3D;&#x60; greater or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;§&#x60; regular expression&lt;br&gt;&#x60;&lt;value&gt;&#x60; is the value to search for | [optional]
 **order** | **str**| A valid field name by which the response should be ordered, use the separator &#x60;:&#x60; to specify the sort order (&#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; when omitted) | [optional]
 **limit** | **int**| The maximum number of objects to return | [optional]
 **offset** | **int**| The number of objects to skip | [optional]

### Return type

[**[CurrentChoreResponse]**](CurrentChoreResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of CurrentChoreResponse objects |  -  |
**500** | The operation was not successful (possible errors are invalid field names or conditions in filter parameters provided) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

