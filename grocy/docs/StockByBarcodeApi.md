# openapi_client.StockByBarcodeApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stock_products_by_barcode_barcode_add_post**](StockByBarcodeApi.md#stock_products_by_barcode_barcode_add_post) | **POST** /stock/products/by-barcode/{barcode}/add | Adds the given amount of the by its barcode given product to stock
[**stock_products_by_barcode_barcode_consume_post**](StockByBarcodeApi.md#stock_products_by_barcode_barcode_consume_post) | **POST** /stock/products/by-barcode/{barcode}/consume | Removes the given amount of the by its barcode given product from stock
[**stock_products_by_barcode_barcode_get**](StockByBarcodeApi.md#stock_products_by_barcode_barcode_get) | **GET** /stock/products/by-barcode/{barcode} | Returns details of the given product by its barcode
[**stock_products_by_barcode_barcode_inventory_post**](StockByBarcodeApi.md#stock_products_by_barcode_barcode_inventory_post) | **POST** /stock/products/by-barcode/{barcode}/inventory | Inventories the by its barcode given product (adds/removes based on the given new amount)
[**stock_products_by_barcode_barcode_open_post**](StockByBarcodeApi.md#stock_products_by_barcode_barcode_open_post) | **POST** /stock/products/by-barcode/{barcode}/open | Marks the given amount of the by its barcode given product as opened
[**stock_products_by_barcode_barcode_transfer_post**](StockByBarcodeApi.md#stock_products_by_barcode_barcode_transfer_post) | **POST** /stock/products/by-barcode/{barcode}/transfer | Transfers the given amount of the by its barcode given product from one location to another (this is currently not supported for tare weight handling enabled products)


# **stock_products_by_barcode_barcode_add_post**
> [StockLogEntry] stock_products_by_barcode_barcode_add_post(barcode, inline_object8)

Adds the given amount of the by its barcode given product to stock

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_by_barcode_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object8 import InlineObject8
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
    api_instance = stock_by_barcode_api.StockByBarcodeApi(api_client)
    barcode = "barcode_example" # str | Barcode
    inline_object8 = InlineObject8(
        amount=3.14,
        best_before_date=dateutil_parser('1970-01-01').date(),
        transaction_type=StockTransactionType("purchase"),
        price=3.14,
        location_id=3.14,
    ) # InlineObject8 | 

    # example passing only required values which don't have defaults set
    try:
        # Adds the given amount of the by its barcode given product to stock
        api_response = api_instance.stock_products_by_barcode_barcode_add_post(barcode, inline_object8)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockByBarcodeApi->stock_products_by_barcode_barcode_add_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode |
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  |

### Return type

[**[StockLogEntry]**](StockLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing product, invalid transaction type) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_by_barcode_barcode_consume_post**
> [StockLogEntry] stock_products_by_barcode_barcode_consume_post(barcode, inline_object9)

Removes the given amount of the by its barcode given product from stock

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_by_barcode_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object9 import InlineObject9
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
    api_instance = stock_by_barcode_api.StockByBarcodeApi(api_client)
    barcode = "barcode_example" # str | Barcode
    inline_object9 = InlineObject9(
        amount=3.14,
        transaction_type=StockTransactionType("purchase"),
        spoiled=True,
        stock_entry_id="stock_entry_id_example",
        recipe_id=3.14,
        location_id=3.14,
        exact_amount=True,
        allow_subproduct_substitution=True,
    ) # InlineObject9 | 

    # example passing only required values which don't have defaults set
    try:
        # Removes the given amount of the by its barcode given product from stock
        api_response = api_instance.stock_products_by_barcode_barcode_consume_post(barcode, inline_object9)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockByBarcodeApi->stock_products_by_barcode_barcode_consume_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode |
 **inline_object9** | [**InlineObject9**](InlineObject9.md)|  |

### Return type

[**[StockLogEntry]**](StockLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing product, invalid transaction type, given amount &gt; current stock amount) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_by_barcode_barcode_get**
> ProductDetailsResponse stock_products_by_barcode_barcode_get(barcode)

Returns details of the given product by its barcode

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_by_barcode_api
from openapi_client.model.product_details_response import ProductDetailsResponse
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
    api_instance = stock_by_barcode_api.StockByBarcodeApi(api_client)
    barcode = "barcode_example" # str | Barcode

    # example passing only required values which don't have defaults set
    try:
        # Returns details of the given product by its barcode
        api_response = api_instance.stock_products_by_barcode_barcode_get(barcode)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockByBarcodeApi->stock_products_by_barcode_barcode_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode |

### Return type

[**ProductDetailsResponse**](ProductDetailsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A ProductDetailsResponse object |  -  |
**400** | The operation was not successful (possible errors are: Unknown barcode) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_by_barcode_barcode_inventory_post**
> [StockLogEntry] stock_products_by_barcode_barcode_inventory_post(barcode, inline_object11)

Inventories the by its barcode given product (adds/removes based on the given new amount)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_by_barcode_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object11 import InlineObject11
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
    api_instance = stock_by_barcode_api.StockByBarcodeApi(api_client)
    barcode = "barcode_example" # str | Barcode
    inline_object11 = InlineObject11(
        new_amount=1,
        best_before_date=dateutil_parser('1970-01-01').date(),
        location_id=3.14,
        price=3.14,
    ) # InlineObject11 | 

    # example passing only required values which don't have defaults set
    try:
        # Inventories the by its barcode given product (adds/removes based on the given new amount)
        api_response = api_instance.stock_products_by_barcode_barcode_inventory_post(barcode, inline_object11)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockByBarcodeApi->stock_products_by_barcode_barcode_inventory_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode |
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  |

### Return type

[**[StockLogEntry]**](StockLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing product) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_by_barcode_barcode_open_post**
> [StockLogEntry] stock_products_by_barcode_barcode_open_post(barcode, inline_object12)

Marks the given amount of the by its barcode given product as opened

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_by_barcode_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object12 import InlineObject12
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
    api_instance = stock_by_barcode_api.StockByBarcodeApi(api_client)
    barcode = "barcode_example" # str | Barcode
    inline_object12 = InlineObject12(
        amount=3.14,
        stock_entry_id="stock_entry_id_example",
        allow_subproduct_substitution=True,
    ) # InlineObject12 | 

    # example passing only required values which don't have defaults set
    try:
        # Marks the given amount of the by its barcode given product as opened
        api_response = api_instance.stock_products_by_barcode_barcode_open_post(barcode, inline_object12)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockByBarcodeApi->stock_products_by_barcode_barcode_open_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode |
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  |

### Return type

[**[StockLogEntry]**](StockLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing product, given amount &gt; current unopened stock amount) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_by_barcode_barcode_transfer_post**
> [StockLogEntry] stock_products_by_barcode_barcode_transfer_post(barcode, inline_object10)

Transfers the given amount of the by its barcode given product from one location to another (this is currently not supported for tare weight handling enabled products)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_by_barcode_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.error400 import Error400
from openapi_client.model.inline_object10 import InlineObject10
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
    api_instance = stock_by_barcode_api.StockByBarcodeApi(api_client)
    barcode = "barcode_example" # str | Barcode
    inline_object10 = InlineObject10(
        amount=3.14,
        location_id_from=3.14,
        location_id_to=3.14,
        stock_entry_id="stock_entry_id_example",
    ) # InlineObject10 | 

    # example passing only required values which don't have defaults set
    try:
        # Transfers the given amount of the by its barcode given product from one location to another (this is currently not supported for tare weight handling enabled products)
        api_response = api_instance.stock_products_by_barcode_barcode_transfer_post(barcode, inline_object10)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockByBarcodeApi->stock_products_by_barcode_barcode_transfer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode |
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  |

### Return type

[**[StockLogEntry]**](StockLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing product, no existing from or to location, given amount &gt; current stock amount at the source location) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

