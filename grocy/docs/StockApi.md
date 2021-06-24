# openapi_client.StockApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stock_barcodes_external_lookup_barcode_get**](StockApi.md#stock_barcodes_external_lookup_barcode_get) | **GET** /stock/barcodes/external-lookup/{barcode} | Executes an external barcode lookoup via the configured plugin with the given barcode
[**stock_bookings_booking_id_get**](StockApi.md#stock_bookings_booking_id_get) | **GET** /stock/bookings/{bookingId} | Returns the given stock booking
[**stock_bookings_booking_id_undo_post**](StockApi.md#stock_bookings_booking_id_undo_post) | **POST** /stock/bookings/{bookingId}/undo | Undoes a booking
[**stock_entry_entry_id_get**](StockApi.md#stock_entry_entry_id_get) | **GET** /stock/entry/{entryId} | Returns details of the given stock
[**stock_entry_entry_id_printlabel_get**](StockApi.md#stock_entry_entry_id_printlabel_get) | **GET** /stock/entry/{entryId}/printlabel | Prints the label of the given stock entry
[**stock_entry_entry_id_put**](StockApi.md#stock_entry_entry_id_put) | **PUT** /stock/entry/{entryId} | Edits the stock entry
[**stock_get**](StockApi.md#stock_get) | **GET** /stock | Returns all products which are currently in stock incl. the next due date per product
[**stock_products_product_id_add_post**](StockApi.md#stock_products_product_id_add_post) | **POST** /stock/products/{productId}/add | Adds the given amount of the given product to stock
[**stock_products_product_id_consume_post**](StockApi.md#stock_products_product_id_consume_post) | **POST** /stock/products/{productId}/consume | Removes the given amount of the given product from stock
[**stock_products_product_id_entries_get**](StockApi.md#stock_products_product_id_entries_get) | **GET** /stock/products/{productId}/entries | Returns all stock entries of the given product in order of next use (Opened first, then first due first, then first in first out)
[**stock_products_product_id_get**](StockApi.md#stock_products_product_id_get) | **GET** /stock/products/{productId} | Returns details of the given product
[**stock_products_product_id_inventory_post**](StockApi.md#stock_products_product_id_inventory_post) | **POST** /stock/products/{productId}/inventory | Inventories the given product (adds/removes based on the given new amount)
[**stock_products_product_id_locations_get**](StockApi.md#stock_products_product_id_locations_get) | **GET** /stock/products/{productId}/locations | Returns all locations where the given product currently has stock
[**stock_products_product_id_open_post**](StockApi.md#stock_products_product_id_open_post) | **POST** /stock/products/{productId}/open | Marks the given amount of the given product as opened
[**stock_products_product_id_price_history_get**](StockApi.md#stock_products_product_id_price_history_get) | **GET** /stock/products/{productId}/price-history | Returns the price history of the given product
[**stock_products_product_id_printlabel_get**](StockApi.md#stock_products_product_id_printlabel_get) | **GET** /stock/products/{productId}/printlabel | Prints the product label of the given product
[**stock_products_product_id_to_keep_merge_product_id_to_remove_post**](StockApi.md#stock_products_product_id_to_keep_merge_product_id_to_remove_post) | **POST** /stock/products/{productIdToKeep}/merge/{productIdToRemove} | Merges two products into one
[**stock_products_product_id_transfer_post**](StockApi.md#stock_products_product_id_transfer_post) | **POST** /stock/products/{productId}/transfer | Transfers the given amount of the given product from one location to another (this is currently not supported for tare weight handling enabled products)
[**stock_shoppinglist_add_expired_products_post**](StockApi.md#stock_shoppinglist_add_expired_products_post) | **POST** /stock/shoppinglist/add-expired-products | Adds expired products to the given shopping list
[**stock_shoppinglist_add_missing_products_post**](StockApi.md#stock_shoppinglist_add_missing_products_post) | **POST** /stock/shoppinglist/add-missing-products | Adds currently missing products (below defined min. stock amount) to the given shopping list
[**stock_shoppinglist_add_overdue_products_post**](StockApi.md#stock_shoppinglist_add_overdue_products_post) | **POST** /stock/shoppinglist/add-overdue-products | Adds overdue products to the given shopping list
[**stock_shoppinglist_add_product_post**](StockApi.md#stock_shoppinglist_add_product_post) | **POST** /stock/shoppinglist/add-product | Adds the given amount of the given product to the given shopping list
[**stock_shoppinglist_clear_post**](StockApi.md#stock_shoppinglist_clear_post) | **POST** /stock/shoppinglist/clear | Removes all items from the given shopping list
[**stock_shoppinglist_remove_product_post**](StockApi.md#stock_shoppinglist_remove_product_post) | **POST** /stock/shoppinglist/remove-product | Removes the given amount of the given product from the given shopping list, if it is on it
[**stock_transactions_transaction_id_get**](StockApi.md#stock_transactions_transaction_id_get) | **GET** /stock/transactions/{transactionId} | Returns all stock bookings of the given transaction id
[**stock_transactions_transaction_id_undo_post**](StockApi.md#stock_transactions_transaction_id_undo_post) | **POST** /stock/transactions/{transactionId}/undo | Undoes a transaction
[**stock_volatile_get**](StockApi.md#stock_volatile_get) | **GET** /stock/volatile | Returns all products which are due soon, overdue, expired or currently missing


# **stock_barcodes_external_lookup_barcode_get**
> ExternalBarcodeLookupResponse stock_barcodes_external_lookup_barcode_get(barcode)

Executes an external barcode lookoup via the configured plugin with the given barcode

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.external_barcode_lookup_response import ExternalBarcodeLookupResponse
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
    api_instance = stock_api.StockApi(api_client)
    barcode = "barcode_example" # str | The barcode to lookup up
    add = False # bool | When true, the product is added to the database on a successful lookup and the new product id is in included in the response (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Executes an external barcode lookoup via the configured plugin with the given barcode
        api_response = api_instance.stock_barcodes_external_lookup_barcode_get(barcode)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_barcodes_external_lookup_barcode_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Executes an external barcode lookoup via the configured plugin with the given barcode
        api_response = api_instance.stock_barcodes_external_lookup_barcode_get(barcode, add=add)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_barcodes_external_lookup_barcode_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| The barcode to lookup up |
 **add** | **bool**| When true, the product is added to the database on a successful lookup and the new product id is in included in the response | [optional] if omitted the server will use the default value of False

### Return type

[**ExternalBarcodeLookupResponse**](ExternalBarcodeLookupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExternalBarcodeLookupResponse object or null, when nothing was found for the given barcode |  -  |
**400** | The operation was not successful (possible errors are: Plugin error) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_bookings_booking_id_get**
> StockLogEntry stock_bookings_booking_id_get(booking_id)

Returns the given stock booking

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_log_entry import StockLogEntry
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
    api_instance = stock_api.StockApi(api_client)
    booking_id = 1 # int | A valid stock booking id

    # example passing only required values which don't have defaults set
    try:
        # Returns the given stock booking
        api_response = api_instance.stock_bookings_booking_id_get(booking_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_bookings_booking_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_id** | **int**| A valid stock booking id |

### Return type

[**StockLogEntry**](StockLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A StockLogEntry object |  -  |
**400** | The operation was not successful (possible errors are: Invalid stock booking id) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_bookings_booking_id_undo_post**
> stock_bookings_booking_id_undo_post(booking_id)

Undoes a booking

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
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
    api_instance = stock_api.StockApi(api_client)
    booking_id = 1 # int | A valid stock booking id

    # example passing only required values which don't have defaults set
    try:
        # Undoes a booking
        api_instance.stock_bookings_booking_id_undo_post(booking_id)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_bookings_booking_id_undo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **booking_id** | **int**| A valid stock booking id |

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

# **stock_entry_entry_id_get**
> StockEntry stock_entry_entry_id_get(entry_id)

Returns details of the given stock

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_entry import StockEntry
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
    api_instance = stock_api.StockApi(api_client)
    entry_id = 1 # int | A valid stock entry id

    # example passing only required values which don't have defaults set
    try:
        # Returns details of the given stock
        api_response = api_instance.stock_entry_entry_id_get(entry_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_entry_entry_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**| A valid stock entry id |

### Return type

[**StockEntry**](StockEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A StockEntry Response object |  -  |
**400** | The operation was not successful (possible errors are: Not existing product) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_entry_entry_id_printlabel_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} stock_entry_entry_id_printlabel_get(entry_id)

Prints the label of the given stock entry

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
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
    api_instance = stock_api.StockApi(api_client)
    entry_id = 1 # int | A valid stock entry id

    # example passing only required values which don't have defaults set
    try:
        # Prints the label of the given stock entry
        api_response = api_instance.stock_entry_entry_id_printlabel_get(entry_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_entry_entry_id_printlabel_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**| A valid stock entry id |

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
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing stock entry, error on WebHook execution) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_entry_entry_id_put**
> [StockLogEntry] stock_entry_entry_id_put(entry_id, inline_object2)

Edits the stock entry

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object2 import InlineObject2
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
    api_instance = stock_api.StockApi(api_client)
    entry_id = 1 # int | A valid stock entry id
    inline_object2 = InlineObject2(
        amount=3.14,
        best_before_date=dateutil_parser('1970-01-01').date(),
        price=3.14,
        open=True,
        location_id=3.14,
        shopping_location_id=3.14,
        purchased_date=dateutil_parser('1970-01-01').date(),
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        # Edits the stock entry
        api_response = api_instance.stock_entry_entry_id_put(entry_id, inline_object2)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_entry_entry_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**| A valid stock entry id |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  |

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

# **stock_get**
> [CurrentStockResponse] stock_get()

Returns all products which are currently in stock incl. the next due date per product

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.current_stock_response import CurrentStockResponse
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
    api_instance = stock_api.StockApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all products which are currently in stock incl. the next due date per product
        api_response = api_instance.stock_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[CurrentStockResponse]**](CurrentStockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of CurrentStockResponse objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_product_id_add_post**
> [StockLogEntry] stock_products_product_id_add_post(product_id, inline_object3)

Adds the given amount of the given product to stock

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.inline_object3 import InlineObject3
from openapi_client.model.stock_log_entry import StockLogEntry
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id
    inline_object3 = InlineObject3(
        amount=3.14,
        best_before_date=dateutil_parser('1970-01-01').date(),
        transaction_type=StockTransactionType("purchase"),
        price=3.14,
        location_id=3.14,
        shopping_location_id=3.14,
        print_stock_label=True,
    ) # InlineObject3 | 

    # example passing only required values which don't have defaults set
    try:
        # Adds the given amount of the given product to stock
        api_response = api_instance.stock_products_product_id_add_post(product_id, inline_object3)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_add_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  |

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

# **stock_products_product_id_consume_post**
> [StockLogEntry] stock_products_product_id_consume_post(product_id, inline_object4)

Removes the given amount of the given product from stock

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object4 import InlineObject4
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id
    inline_object4 = InlineObject4(
        amount=3.14,
        transaction_type=StockTransactionType("purchase"),
        spoiled=True,
        stock_entry_id="stock_entry_id_example",
        recipe_id=3.14,
        location_id=3.14,
        exact_amount=True,
        allow_subproduct_substitution=True,
    ) # InlineObject4 | 

    # example passing only required values which don't have defaults set
    try:
        # Removes the given amount of the given product from stock
        api_response = api_instance.stock_products_product_id_consume_post(product_id, inline_object4)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_consume_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  |

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

# **stock_products_product_id_entries_get**
> [StockEntry] stock_products_product_id_entries_get(product_id)

Returns all stock entries of the given product in order of next use (Opened first, then first due first, then first in first out)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_entry import StockEntry
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id
    include_sub_products = True # bool | If sub products should be included (if the given product is a parent product and in addition to the ones of the given product) (optional)
    query = [
        "query[]_example",
    ] # [str] | An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for (optional)
    order = "order_example" # str | A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted) (optional)
    limit = 1 # int | The maximum number of objects to return (optional)
    offset = 1 # int | The number of objects to skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns all stock entries of the given product in order of next use (Opened first, then first due first, then first in first out)
        api_response = api_instance.stock_products_product_id_entries_get(product_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_entries_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all stock entries of the given product in order of next use (Opened first, then first due first, then first in first out)
        api_response = api_instance.stock_products_product_id_entries_get(product_id, include_sub_products=include_sub_products, query=query, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_entries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |
 **include_sub_products** | **bool**| If sub products should be included (if the given product is a parent product and in addition to the ones of the given product) | [optional]
 **query** | **[str]**| An array of filter conditions, each of them is a string in the form of &#x60;&lt;field&gt;&lt;condition&gt;&lt;value&gt;&#x60; where&lt;br&gt;&#x60;&lt;field&gt;&#x60; is a valid field name&lt;br&gt;&#x60;&lt;condition&gt;&#x60; is a comparison operator, one of&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&#x3D;&#x60; equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!&#x3D;&#x60; not equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;~&#x60; LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!~&#x60; not LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x60; less&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x60; greater&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x3D;&#x60; less or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x3D;&#x60; greater or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;§&#x60; regular expression&lt;br&gt;&#x60;&lt;value&gt;&#x60; is the value to search for | [optional]
 **order** | **str**| A valid field name by which the response should be ordered, use the separator &#x60;:&#x60; to specify the sort order (&#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; when omitted) | [optional]
 **limit** | **int**| The maximum number of objects to return | [optional]
 **offset** | **int**| The number of objects to skip | [optional]

### Return type

[**[StockEntry]**](StockEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of StockEntry objects |  -  |
**400** | The operation was not successful (possible errors are: Not existing product) |  -  |
**500** | The operation was not successful (possible errors are invalid field names or conditions in filter parameters provided) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_product_id_get**
> ProductDetailsResponse stock_products_product_id_get(product_id)

Returns details of the given product

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id

    # example passing only required values which don't have defaults set
    try:
        # Returns details of the given product
        api_response = api_instance.stock_products_product_id_get(product_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |

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
**400** | The operation was not successful (possible errors are: Not existing product) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_product_id_inventory_post**
> [StockLogEntry] stock_products_product_id_inventory_post(product_id, inline_object6)

Inventories the given product (adds/removes based on the given new amount)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.error400 import Error400
from openapi_client.model.inline_object6 import InlineObject6
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id
    inline_object6 = InlineObject6(
        new_amount=1,
        best_before_date=dateutil_parser('1970-01-01').date(),
        shopping_location_id=3.14,
        location_id=3.14,
        price=3.14,
    ) # InlineObject6 | 

    # example passing only required values which don't have defaults set
    try:
        # Inventories the given product (adds/removes based on the given new amount)
        api_response = api_instance.stock_products_product_id_inventory_post(product_id, inline_object6)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_inventory_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  |

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

# **stock_products_product_id_locations_get**
> [StockLocation] stock_products_product_id_locations_get(product_id)

Returns all locations where the given product currently has stock

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_location import StockLocation
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id
    include_sub_products = True # bool | If sub product locations should be included (if the given product is a parent product and in addition to the ones of the given product) (optional)
    query = [
        "query[]_example",
    ] # [str] | An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for (optional)
    order = "order_example" # str | A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted) (optional)
    limit = 1 # int | The maximum number of objects to return (optional)
    offset = 1 # int | The number of objects to skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns all locations where the given product currently has stock
        api_response = api_instance.stock_products_product_id_locations_get(product_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_locations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all locations where the given product currently has stock
        api_response = api_instance.stock_products_product_id_locations_get(product_id, include_sub_products=include_sub_products, query=query, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_locations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |
 **include_sub_products** | **bool**| If sub product locations should be included (if the given product is a parent product and in addition to the ones of the given product) | [optional]
 **query** | **[str]**| An array of filter conditions, each of them is a string in the form of &#x60;&lt;field&gt;&lt;condition&gt;&lt;value&gt;&#x60; where&lt;br&gt;&#x60;&lt;field&gt;&#x60; is a valid field name&lt;br&gt;&#x60;&lt;condition&gt;&#x60; is a comparison operator, one of&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&#x3D;&#x60; equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!&#x3D;&#x60; not equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;~&#x60; LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;!~&#x60; not LIKE&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x60; less&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x60; greater&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&lt;&#x3D;&#x60; less or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;&gt;&#x3D;&#x60; greater or equal&lt;br&gt;&amp;nbsp;&amp;nbsp;&#x60;§&#x60; regular expression&lt;br&gt;&#x60;&lt;value&gt;&#x60; is the value to search for | [optional]
 **order** | **str**| A valid field name by which the response should be ordered, use the separator &#x60;:&#x60; to specify the sort order (&#x60;asc&#x60; or &#x60;desc&#x60;, defaults to &#x60;asc&#x60; when omitted) | [optional]
 **limit** | **int**| The maximum number of objects to return | [optional]
 **offset** | **int**| The number of objects to skip | [optional]

### Return type

[**[StockLocation]**](StockLocation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of StockLocation objects |  -  |
**400** | The operation was not successful (possible errors are: Not existing product) |  -  |
**500** | The operation was not successful (possible errors are invalid field names or conditions in filter parameters provided) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_product_id_open_post**
> [StockLogEntry] stock_products_product_id_open_post(product_id, inline_object7)

Marks the given amount of the given product as opened

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object7 import InlineObject7
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id
    inline_object7 = InlineObject7(
        amount=3.14,
        stock_entry_id="stock_entry_id_example",
        allow_subproduct_substitution=True,
    ) # InlineObject7 | 

    # example passing only required values which don't have defaults set
    try:
        # Marks the given amount of the given product as opened
        api_response = api_instance.stock_products_product_id_open_post(product_id, inline_object7)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_open_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  |

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

# **stock_products_product_id_price_history_get**
> [ProductPriceHistory] stock_products_product_id_price_history_get(product_id)

Returns the price history of the given product

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.product_price_history import ProductPriceHistory
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id

    # example passing only required values which don't have defaults set
    try:
        # Returns the price history of the given product
        api_response = api_instance.stock_products_product_id_price_history_get(product_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_price_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |

### Return type

[**[ProductPriceHistory]**](ProductPriceHistory.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of ProductPriceHistory objects |  -  |
**400** | The operation was not successful (possible errors are: Not existing product) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_product_id_printlabel_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} stock_products_product_id_printlabel_get(product_id)

Prints the product label of the given product

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id

    # example passing only required values which don't have defaults set
    try:
        # Prints the product label of the given product
        api_response = api_instance.stock_products_product_id_printlabel_get(product_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_printlabel_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |

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
**200** | The operation was successful |  -  |
**400** | The operation was not successful (possible errors are: Not existing product, error on WebHook execution) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_product_id_to_keep_merge_product_id_to_remove_post**
> stock_products_product_id_to_keep_merge_product_id_to_remove_post(product_id_to_keep, product_id_to_remove)

Merges two products into one

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
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
    api_instance = stock_api.StockApi(api_client)
    product_id_to_keep = 1 # int | A valid product id of the product to keep
    product_id_to_remove = 1 # int | A valid product id of the product to remove

    # example passing only required values which don't have defaults set
    try:
        # Merges two products into one
        api_instance.stock_products_product_id_to_keep_merge_product_id_to_remove_post(product_id_to_keep, product_id_to_remove)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_to_keep_merge_product_id_to_remove_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id_to_keep** | **int**| A valid product id of the product to keep |
 **product_id_to_remove** | **int**| A valid product id of the product to remove |

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
**400** | The operation was not successful (possible errors are: Invalid product id) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_products_product_id_transfer_post**
> [StockLogEntry] stock_products_product_id_transfer_post(product_id, inline_object5)

Transfers the given amount of the given product from one location to another (this is currently not supported for tare weight handling enabled products)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_log_entry import StockLogEntry
from openapi_client.model.inline_object5 import InlineObject5
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
    api_instance = stock_api.StockApi(api_client)
    product_id = 1 # int | A valid product id
    inline_object5 = InlineObject5(
        amount=3.14,
        location_id_from=3.14,
        location_id_to=3.14,
        stock_entry_id="stock_entry_id_example",
    ) # InlineObject5 | 

    # example passing only required values which don't have defaults set
    try:
        # Transfers the given amount of the given product from one location to another (this is currently not supported for tare weight handling enabled products)
        api_response = api_instance.stock_products_product_id_transfer_post(product_id, inline_object5)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_products_product_id_transfer_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| A valid product id |
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  |

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

# **stock_shoppinglist_add_expired_products_post**
> stock_shoppinglist_add_expired_products_post()

Adds expired products to the given shopping list

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.inline_object15 import InlineObject15
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
    api_instance = stock_api.StockApi(api_client)
    inline_object15 = InlineObject15(
        list_id=1,
    ) # InlineObject15 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds expired products to the given shopping list
        api_instance.stock_shoppinglist_add_expired_products_post(inline_object15=inline_object15)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_shoppinglist_add_expired_products_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object15** | [**InlineObject15**](InlineObject15.md)|  | [optional]

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
**400** | The operation was not successful (possible errors are: Not existing shopping list) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_shoppinglist_add_missing_products_post**
> stock_shoppinglist_add_missing_products_post()

Adds currently missing products (below defined min. stock amount) to the given shopping list

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.inline_object13 import InlineObject13
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
    api_instance = stock_api.StockApi(api_client)
    inline_object13 = InlineObject13(
        list_id=1,
    ) # InlineObject13 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds currently missing products (below defined min. stock amount) to the given shopping list
        api_instance.stock_shoppinglist_add_missing_products_post(inline_object13=inline_object13)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_shoppinglist_add_missing_products_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object13** | [**InlineObject13**](InlineObject13.md)|  | [optional]

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
**400** | The operation was not successful (possible errors are: Not existing shopping list) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_shoppinglist_add_overdue_products_post**
> stock_shoppinglist_add_overdue_products_post()

Adds overdue products to the given shopping list

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.inline_object14 import InlineObject14
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
    api_instance = stock_api.StockApi(api_client)
    inline_object14 = InlineObject14(
        list_id=1,
    ) # InlineObject14 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds overdue products to the given shopping list
        api_instance.stock_shoppinglist_add_overdue_products_post(inline_object14=inline_object14)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_shoppinglist_add_overdue_products_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object14** | [**InlineObject14**](InlineObject14.md)|  | [optional]

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
**400** | The operation was not successful (possible errors are: Not existing shopping list) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_shoppinglist_add_product_post**
> stock_shoppinglist_add_product_post(inline_object17)

Adds the given amount of the given product to the given shopping list

If the product is already on the shopping list, the given amount will increase the amount of the already existing item, otherwise a new item will be added

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.inline_object17 import InlineObject17
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
    api_instance = stock_api.StockApi(api_client)
    inline_object17 = InlineObject17(
        product_id=1,
        list_id=1,
        product_amount=1,
        note="note_example",
    ) # InlineObject17 | 

    # example passing only required values which don't have defaults set
    try:
        # Adds the given amount of the given product to the given shopping list
        api_instance.stock_shoppinglist_add_product_post(inline_object17)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_shoppinglist_add_product_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object17** | [**InlineObject17**](InlineObject17.md)|  |

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
**400** | The operation was not successful (possible errors are: Not existing shopping list, Invalid product id supplied) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_shoppinglist_clear_post**
> stock_shoppinglist_clear_post()

Removes all items from the given shopping list

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.inline_object16 import InlineObject16
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
    api_instance = stock_api.StockApi(api_client)
    inline_object16 = InlineObject16(
        list_id=1,
    ) # InlineObject16 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes all items from the given shopping list
        api_instance.stock_shoppinglist_clear_post(inline_object16=inline_object16)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_shoppinglist_clear_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object16** | [**InlineObject16**](InlineObject16.md)|  | [optional]

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
**400** | The operation was not successful (possible errors are: Not existing shopping list) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_shoppinglist_remove_product_post**
> stock_shoppinglist_remove_product_post(inline_object18)

Removes the given amount of the given product from the given shopping list, if it is on it

If the resulting amount is <= 0, the item will be completely removed from the given list, otherwise the given amount will reduce the amount of the existing item

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.inline_object18 import InlineObject18
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
    api_instance = stock_api.StockApi(api_client)
    inline_object18 = InlineObject18(
        product_id=1,
        list_id=1,
        product_amount=1,
    ) # InlineObject18 | 

    # example passing only required values which don't have defaults set
    try:
        # Removes the given amount of the given product from the given shopping list, if it is on it
        api_instance.stock_shoppinglist_remove_product_post(inline_object18)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_shoppinglist_remove_product_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object18** | [**InlineObject18**](InlineObject18.md)|  |

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
**400** | The operation was not successful (possible errors are: Not existing shopping list, Invalid product id supplied) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_transactions_transaction_id_get**
> [StockLogEntry] stock_transactions_transaction_id_get(transaction_id)

Returns all stock bookings of the given transaction id

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.stock_log_entry import StockLogEntry
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
    api_instance = stock_api.StockApi(api_client)
    transaction_id = "transactionId_example" # str | A valid stock transaction id

    # example passing only required values which don't have defaults set
    try:
        # Returns all stock bookings of the given transaction id
        api_response = api_instance.stock_transactions_transaction_id_get(transaction_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_transactions_transaction_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| A valid stock transaction id |

### Return type

[**[StockLogEntry]**](StockLogEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of StockLogEntry objects |  -  |
**400** | The operation was not successful (possible errors are: Not existing transaction) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_transactions_transaction_id_undo_post**
> stock_transactions_transaction_id_undo_post(transaction_id)

Undoes a transaction

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
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
    api_instance = stock_api.StockApi(api_client)
    transaction_id = "transactionId_example" # str | A valid stock transaction id

    # example passing only required values which don't have defaults set
    try:
        # Undoes a transaction
        api_instance.stock_transactions_transaction_id_undo_post(transaction_id)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_transactions_transaction_id_undo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| A valid stock transaction id |

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
**400** | The operation was not successful (possible errors are: Not existing transaction) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stock_volatile_get**
> [CurrentVolatilStockResponse] stock_volatile_get()

Returns all products which are due soon, overdue, expired or currently missing

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import stock_api
from openapi_client.model.current_volatil_stock_response import CurrentVolatilStockResponse
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
    api_instance = stock_api.StockApi(api_client)
    due_soon_days = 5 # int | The number of days in which products are considered to be due soon (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns all products which are due soon, overdue, expired or currently missing
        api_response = api_instance.stock_volatile_get(due_soon_days=due_soon_days)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockApi->stock_volatile_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **due_soon_days** | **int**| The number of days in which products are considered to be due soon | [optional] if omitted the server will use the default value of 5

### Return type

[**[CurrentVolatilStockResponse]**](CurrentVolatilStockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A CurrentVolatilStockResponse object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

