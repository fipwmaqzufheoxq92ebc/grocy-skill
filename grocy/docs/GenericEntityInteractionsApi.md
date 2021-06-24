# openapi_client.GenericEntityInteractionsApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**objects_entity_get**](GenericEntityInteractionsApi.md#objects_entity_get) | **GET** /objects/{entity} | Returns all objects of the given entity
[**objects_entity_object_id_delete**](GenericEntityInteractionsApi.md#objects_entity_object_id_delete) | **DELETE** /objects/{entity}/{objectId} | Deletes a single object of the given entity
[**objects_entity_object_id_get**](GenericEntityInteractionsApi.md#objects_entity_object_id_get) | **GET** /objects/{entity}/{objectId} | Returns a single object of the given entity
[**objects_entity_object_id_put**](GenericEntityInteractionsApi.md#objects_entity_object_id_put) | **PUT** /objects/{entity}/{objectId} | Edits the given object of the given entity
[**objects_entity_post**](GenericEntityInteractionsApi.md#objects_entity_post) | **POST** /objects/{entity} | Adds a single object of the given entity
[**userfields_entity_object_id_get**](GenericEntityInteractionsApi.md#userfields_entity_object_id_get) | **GET** /userfields/{entity}/{objectId} | Returns all userfields with their values of the given object of the given entity
[**userfields_entity_object_id_put**](GenericEntityInteractionsApi.md#userfields_entity_object_id_put) | **PUT** /userfields/{entity}/{objectId} | Edits the given userfields of the given object of the given entity


# **objects_entity_get**
> [dict] objects_entity_get(entity)

Returns all objects of the given entity

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import generic_entity_interactions_api
from openapi_client.model.exposed_entity_not_including_not_listable import ExposedEntityNotIncludingNotListable
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
    api_instance = generic_entity_interactions_api.GenericEntityInteractionsApi(api_client)
    entity = ExposedEntityNotIncludingNotListable("products") # ExposedEntityNotIncludingNotListable | A valid entity name
    query = [
        "query[]_example",
    ] # [str] | An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for (optional)
    order = "order_example" # str | A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted) (optional)
    limit = 1 # int | The maximum number of objects to return (optional)
    offset = 1 # int | The number of objects to skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns all objects of the given entity
        api_response = api_instance.objects_entity_get(entity)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->objects_entity_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all objects of the given entity
        api_response = api_instance.objects_entity_get(entity, query=query, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->objects_entity_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **ExposedEntityNotIncludingNotListable**| A valid entity name |
 **query** | **[str]**| An array of filter conditions, each of them is a string in the form of &#x60;&lt;field&gt;&lt;condition&gt;&lt;value&gt;&#x60; where&lt;br&gt;&#x60;&lt;field&gt;&#x60; is a valid field name&lt;br&gt;&#x60;&lt;condition&gt;&#x60; is a comparison operator, one of&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&#x3D;&#x60; equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!&#x3D;&#x60; not equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;~&#x60; LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!~&#x60; not LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x60; less&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x60; greater&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x3D;&#x60; less or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x3D;&#x60; greater or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;§&#x60; regular expression&lt;br&gt;&#x60;&lt;value&gt;&#x60; is the value to search for | [optional]
 **order** | **str**| A valid field name by which the response should be ordered, use the separator &#x60;:&#x60; to specify the sort order (&#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; when omitted) | [optional]
 **limit** | **int**| The maximum number of objects to return | [optional]
 **offset** | **int**| The number of objects to skip | [optional]

### Return type

**[dict]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An entity object |  -  |
**400** | The operation was not successful |  -  |
**500** | The operation was not successful (possible errors are invalid field names or conditions in filter parameters provided) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **objects_entity_object_id_delete**
> objects_entity_object_id_delete(entity, object_id)

Deletes a single object of the given entity

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import generic_entity_interactions_api
from openapi_client.model.exposed_entity_not_including_not_deletable import ExposedEntityNotIncludingNotDeletable
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
    api_instance = generic_entity_interactions_api.GenericEntityInteractionsApi(api_client)
    entity = ExposedEntityNotIncludingNotDeletable("products") # ExposedEntityNotIncludingNotDeletable | A valid entity name
    object_id = 1 # int | A valid object id of the given entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a single object of the given entity
        api_instance.objects_entity_object_id_delete(entity, object_id)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->objects_entity_object_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **ExposedEntityNotIncludingNotDeletable**| A valid entity name |
 **object_id** | **int**| A valid object id of the given entity |

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

# **objects_entity_object_id_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} objects_entity_object_id_get(entity, object_id)

Returns a single object of the given entity

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import generic_entity_interactions_api
from openapi_client.model.exposed_entity_not_including_not_listable import ExposedEntityNotIncludingNotListable
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
    api_instance = generic_entity_interactions_api.GenericEntityInteractionsApi(api_client)
    entity = ExposedEntityNotIncludingNotListable("products") # ExposedEntityNotIncludingNotListable | A valid entity name
    object_id = 1 # int | A valid object id of the given entity

    # example passing only required values which don't have defaults set
    try:
        # Returns a single object of the given entity
        api_response = api_instance.objects_entity_object_id_get(entity, object_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->objects_entity_object_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **ExposedEntityNotIncludingNotListable**| A valid entity name |
 **object_id** | **int**| A valid object id of the given entity |

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
**200** | An entity object |  -  |
**400** | The operation was not successful |  -  |
**404** | Object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **objects_entity_object_id_put**
> objects_entity_object_id_put(entity, object_id, unknown_base_type)

Edits the given object of the given entity

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import generic_entity_interactions_api
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.exposed_entity_not_including_not_editable import ExposedEntityNotIncludingNotEditable
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
    api_instance = generic_entity_interactions_api.GenericEntityInteractionsApi(api_client)
    entity = ExposedEntityNotIncludingNotEditable("products") # ExposedEntityNotIncludingNotEditable | A valid entity name
    object_id = 1 # int | A valid object id of the given entity
    unknown_base_type =  # UNKNOWN_BASE_TYPE | A valid entity object of the entity specified in parameter *entity*

    # example passing only required values which don't have defaults set
    try:
        # Edits the given object of the given entity
        api_instance.objects_entity_object_id_put(entity, object_id, unknown_base_type)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->objects_entity_object_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **ExposedEntityNotIncludingNotEditable**| A valid entity name |
 **object_id** | **int**| A valid object id of the given entity |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| A valid entity object of the entity specified in parameter *entity* |

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

# **objects_entity_post**
> InlineResponse2001 objects_entity_post(entity, unknown_base_type)

Adds a single object of the given entity

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import generic_entity_interactions_api
from openapi_client.model.inline_response2001 import InlineResponse2001
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.exposed_entity_not_including_not_editable import ExposedEntityNotIncludingNotEditable
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
    api_instance = generic_entity_interactions_api.GenericEntityInteractionsApi(api_client)
    entity = ExposedEntityNotIncludingNotEditable("products") # ExposedEntityNotIncludingNotEditable | A valid entity name
    unknown_base_type =  # UNKNOWN_BASE_TYPE | A valid entity object of the entity specified in parameter *entity*

    # example passing only required values which don't have defaults set
    try:
        # Adds a single object of the given entity
        api_response = api_instance.objects_entity_post(entity, unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->objects_entity_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **ExposedEntityNotIncludingNotEditable**| A valid entity name |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| A valid entity object of the entity specified in parameter *entity* |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfields_entity_object_id_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} userfields_entity_object_id_get(entity, object_id)

Returns all userfields with their values of the given object of the given entity

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import generic_entity_interactions_api
from openapi_client.model.exposed_entity import ExposedEntity
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
    api_instance = generic_entity_interactions_api.GenericEntityInteractionsApi(api_client)
    entity = ExposedEntity("products") # ExposedEntity | A valid entity name
    object_id = 1 # int | A valid object id of the given entity

    # example passing only required values which don't have defaults set
    try:
        # Returns all userfields with their values of the given object of the given entity
        api_response = api_instance.userfields_entity_object_id_get(entity, object_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->userfields_entity_object_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **ExposedEntity**| A valid entity name |
 **object_id** | **int**| A valid object id of the given entity |

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
**200** | Key/value pairs of userfields |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userfields_entity_object_id_put**
> userfields_entity_object_id_put(entity, object_id, body)

Edits the given userfields of the given object of the given entity

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import generic_entity_interactions_api
from openapi_client.model.exposed_entity_not_including_not_editable import ExposedEntityNotIncludingNotEditable
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
    api_instance = generic_entity_interactions_api.GenericEntityInteractionsApi(api_client)
    entity = ExposedEntityNotIncludingNotEditable("products") # ExposedEntityNotIncludingNotEditable | A valid entity name
    object_id = 1 # int | A valid object id of the given entity
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | A valid entity object of the entity specified in parameter *entity*

    # example passing only required values which don't have defaults set
    try:
        # Edits the given userfields of the given object of the given entity
        api_instance.userfields_entity_object_id_put(entity, object_id, body)
    except openapi_client.ApiException as e:
        print("Exception when calling GenericEntityInteractionsApi->userfields_entity_object_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **ExposedEntityNotIncludingNotEditable**| A valid entity name |
 **object_id** | **int**| A valid object id of the given entity |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| A valid entity object of the entity specified in parameter *entity* |

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

