# openapi_client.RecipesApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recipes_fulfillment_get**](RecipesApi.md#recipes_fulfillment_get) | **GET** /recipes/fulfillment | Get stock fulfillment information for all recipe
[**recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post**](RecipesApi.md#recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post) | **POST** /recipes/{recipeId}/add-not-fulfilled-products-to-shoppinglist | Adds all missing products for the given recipe to the shopping list
[**recipes_recipe_id_consume_post**](RecipesApi.md#recipes_recipe_id_consume_post) | **POST** /recipes/{recipeId}/consume | Consumes all products of the given recipe
[**recipes_recipe_id_fulfillment_get**](RecipesApi.md#recipes_recipe_id_fulfillment_get) | **GET** /recipes/{recipeId}/fulfillment | Get stock fulfillment information for the given recipe


# **recipes_fulfillment_get**
> [RecipeFulfillmentResponse] recipes_fulfillment_get()

Get stock fulfillment information for all recipe

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import recipes_api
from openapi_client.model.recipe_fulfillment_response import RecipeFulfillmentResponse
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
    api_instance = recipes_api.RecipesApi(api_client)
    query = [
        "query[]_example",
    ] # [str] | An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for (optional)
    order = "order_example" # str | A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted) (optional)
    limit = 1 # int | The maximum number of objects to return (optional)
    offset = 1 # int | The number of objects to skip (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get stock fulfillment information for all recipe
        api_response = api_instance.recipes_fulfillment_get(query=query, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipes_fulfillment_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **[str]**| An array of filter conditions, each of them is a string in the form of &#x60;&lt;field&gt;&lt;condition&gt;&lt;value&gt;&#x60; where&lt;br&gt;&#x60;&lt;field&gt;&#x60; is a valid field name&lt;br&gt;&#x60;&lt;condition&gt;&#x60; is a comparison operator, one of&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&#x3D;&#x60; equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!&#x3D;&#x60; not equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;~&#x60; LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!~&#x60; not LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x60; less&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x60; greater&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x3D;&#x60; less or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x3D;&#x60; greater or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;§&#x60; regular expression&lt;br&gt;&#x60;&lt;value&gt;&#x60; is the value to search for | [optional]
 **order** | **str**| A valid field name by which the response should be ordered, use the separator &#x60;:&#x60; to specify the sort order (&#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; when omitted) | [optional]
 **limit** | **int**| The maximum number of objects to return | [optional]
 **offset** | **int**| The number of objects to skip | [optional]

### Return type

[**[RecipeFulfillmentResponse]**](RecipeFulfillmentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of RecipeFulfillmentResponse objects |  -  |
**400** | The operation was not successful |  -  |
**500** | The operation was not successful (possible errors are invalid field names or conditions in filter parameters provided) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post**
> recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post(recipe_id)

Adds all missing products for the given recipe to the shopping list

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import recipes_api
from openapi_client.model.inline_object19 import InlineObject19
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
    api_instance = recipes_api.RecipesApi(api_client)
    recipe_id = "recipeId_example" # str | A valid recipe id
    inline_object19 = InlineObject19(
        excluded_product_ids=[
            3.14,
        ],
    ) # InlineObject19 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds all missing products for the given recipe to the shopping list
        api_instance.recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post(recipe_id)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds all missing products for the given recipe to the shopping list
        api_instance.recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post(recipe_id, inline_object19=inline_object19)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **str**| A valid recipe id |
 **inline_object19** | [**InlineObject19**](InlineObject19.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The operation was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipes_recipe_id_consume_post**
> recipes_recipe_id_consume_post(recipe_id)

Consumes all products of the given recipe

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import recipes_api
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
    api_instance = recipes_api.RecipesApi(api_client)
    recipe_id = "recipeId_example" # str | A valid recipe id

    # example passing only required values which don't have defaults set
    try:
        # Consumes all products of the given recipe
        api_instance.recipes_recipe_id_consume_post(recipe_id)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipes_recipe_id_consume_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **str**| A valid recipe id |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The operation was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipes_recipe_id_fulfillment_get**
> RecipeFulfillmentResponse recipes_recipe_id_fulfillment_get(recipe_id)

Get stock fulfillment information for the given recipe

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import recipes_api
from openapi_client.model.recipe_fulfillment_response import RecipeFulfillmentResponse
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
    api_instance = recipes_api.RecipesApi(api_client)
    recipe_id = "recipeId_example" # str | A valid recipe id

    # example passing only required values which don't have defaults set
    try:
        # Get stock fulfillment information for the given recipe
        api_response = api_instance.recipes_recipe_id_fulfillment_get(recipe_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipesApi->recipes_recipe_id_fulfillment_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **str**| A valid recipe id |

### Return type

[**RecipeFulfillmentResponse**](RecipeFulfillmentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A RecipeFulfillmentResponse object |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

