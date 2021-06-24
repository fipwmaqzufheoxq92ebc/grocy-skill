# openapi_client.FilesApi

All URIs are relative to *http://localhost:8111/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_group_file_name_delete**](FilesApi.md#files_group_file_name_delete) | **DELETE** /files/{group}/{fileName} | Deletes the given file
[**files_group_file_name_get**](FilesApi.md#files_group_file_name_get) | **GET** /files/{group}/{fileName} | Serves the given file
[**files_group_file_name_put**](FilesApi.md#files_group_file_name_put) | **PUT** /files/{group}/{fileName} | Uploads a single file


# **files_group_file_name_delete**
> files_group_file_name_delete(group, file_name)

Deletes the given file

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import files_api
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
    api_instance = files_api.FilesApi(api_client)
    group = "group_example" # str | The file group
    file_name = "fileName_example" # str | The file name (including extension)<br>**BASE64 encoded**

    # example passing only required values which don't have defaults set
    try:
        # Deletes the given file
        api_instance.files_group_file_name_delete(group, file_name)
    except openapi_client.ApiException as e:
        print("Exception when calling FilesApi->files_group_file_name_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The file group |
 **file_name** | **str**| The file name (including extension)&lt;br&gt;**BASE64 encoded** |

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

# **files_group_file_name_get**
> file_type files_group_file_name_get(group, file_name)

Serves the given file

With proper Content-Type header

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import files_api
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
    api_instance = files_api.FilesApi(api_client)
    group = "group_example" # str | The file group
    file_name = "fileName_example" # str | The file name (including extension)<br>**BASE64 encoded**
    force_serve_as = "picture" # str | Force the file to be served as the given type (optional) if omitted the server will use the default value of "picture"
    best_fit_height = 1 # int | Only when using `force_serve_as` = `picture`: Downscale the picture to the given height while maintaining the aspect ratio (optional)
    best_fit_width = 1 # int | Only when using `force_serve_as` = `picture`: Downscale the picture to the given width while maintaining the aspect ratio (optional)

    # example passing only required values which don't have defaults set
    try:
        # Serves the given file
        api_response = api_instance.files_group_file_name_get(group, file_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FilesApi->files_group_file_name_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Serves the given file
        api_response = api_instance.files_group_file_name_get(group, file_name, force_serve_as=force_serve_as, best_fit_height=best_fit_height, best_fit_width=best_fit_width)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FilesApi->files_group_file_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The file group |
 **file_name** | **str**| The file name (including extension)&lt;br&gt;**BASE64 encoded** |
 **force_serve_as** | **str**| Force the file to be served as the given type | [optional] if omitted the server will use the default value of "picture"
 **best_fit_height** | **int**| Only when using &#x60;force_serve_as&#x60; &#x3D; &#x60;picture&#x60;: Downscale the picture to the given height while maintaining the aspect ratio | [optional]
 **best_fit_width** | **int**| Only when using &#x60;force_serve_as&#x60; &#x3D; &#x60;picture&#x60;: Downscale the picture to the given width while maintaining the aspect ratio | [optional]

### Return type

**file_type**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The binary file contents (Content-Type header is automatically set based on the file type) |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_group_file_name_put**
> files_group_file_name_put(group, file_name)

Uploads a single file

The file will be stored at /data/storage/{group}/{file_name} (you need to remember the group and file name to get or delete it again)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import openapi_client
from openapi_client.api import files_api
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
    api_instance = files_api.FilesApi(api_client)
    group = "group_example" # str | The file group
    file_name = "fileName_example" # str | The file name (including extension)<br>**BASE64 encoded**
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Uploads a single file
        api_instance.files_group_file_name_put(group, file_name)
    except openapi_client.ApiException as e:
        print("Exception when calling FilesApi->files_group_file_name_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Uploads a single file
        api_instance.files_group_file_name_put(group, file_name, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling FilesApi->files_group_file_name_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The file group |
 **file_name** | **str**| The file name (including extension)&lt;br&gt;**BASE64 encoded** |
 **body** | **file_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The operation was successful |  -  |
**400** | The operation was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

