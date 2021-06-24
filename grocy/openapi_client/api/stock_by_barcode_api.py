"""
    grocy REST API

    Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.error400 import Error400
from openapi_client.model.inline_object10 import InlineObject10
from openapi_client.model.inline_object11 import InlineObject11
from openapi_client.model.inline_object12 import InlineObject12
from openapi_client.model.inline_object8 import InlineObject8
from openapi_client.model.inline_object9 import InlineObject9
from openapi_client.model.product_details_response import ProductDetailsResponse
from openapi_client.model.stock_log_entry import StockLogEntry


class StockByBarcodeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __stock_products_by_barcode_barcode_add_post(
            self,
            barcode,
            inline_object8,
            **kwargs
        ):
            """Adds the given amount of the by its barcode given product to stock  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.stock_products_by_barcode_barcode_add_post(barcode, inline_object8, async_req=True)
            >>> result = thread.get()

            Args:
                barcode (str): Barcode
                inline_object8 (InlineObject8):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [StockLogEntry]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['barcode'] = \
                barcode
            kwargs['inline_object8'] = \
                inline_object8
            return self.call_with_http_info(**kwargs)

        self.stock_products_by_barcode_barcode_add_post = _Endpoint(
            settings={
                'response_type': ([StockLogEntry],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/stock/products/by-barcode/{barcode}/add',
                'operation_id': 'stock_products_by_barcode_barcode_add_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'barcode',
                    'inline_object8',
                ],
                'required': [
                    'barcode',
                    'inline_object8',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'barcode':
                        (str,),
                    'inline_object8':
                        (InlineObject8,),
                },
                'attribute_map': {
                    'barcode': 'barcode',
                },
                'location_map': {
                    'barcode': 'path',
                    'inline_object8': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__stock_products_by_barcode_barcode_add_post
        )

        def __stock_products_by_barcode_barcode_consume_post(
            self,
            barcode,
            inline_object9,
            **kwargs
        ):
            """Removes the given amount of the by its barcode given product from stock  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.stock_products_by_barcode_barcode_consume_post(barcode, inline_object9, async_req=True)
            >>> result = thread.get()

            Args:
                barcode (str): Barcode
                inline_object9 (InlineObject9):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [StockLogEntry]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['barcode'] = \
                barcode
            kwargs['inline_object9'] = \
                inline_object9
            return self.call_with_http_info(**kwargs)

        self.stock_products_by_barcode_barcode_consume_post = _Endpoint(
            settings={
                'response_type': ([StockLogEntry],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/stock/products/by-barcode/{barcode}/consume',
                'operation_id': 'stock_products_by_barcode_barcode_consume_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'barcode',
                    'inline_object9',
                ],
                'required': [
                    'barcode',
                    'inline_object9',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'barcode':
                        (str,),
                    'inline_object9':
                        (InlineObject9,),
                },
                'attribute_map': {
                    'barcode': 'barcode',
                },
                'location_map': {
                    'barcode': 'path',
                    'inline_object9': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__stock_products_by_barcode_barcode_consume_post
        )

        def __stock_products_by_barcode_barcode_get(
            self,
            barcode,
            **kwargs
        ):
            """Returns details of the given product by its barcode  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.stock_products_by_barcode_barcode_get(barcode, async_req=True)
            >>> result = thread.get()

            Args:
                barcode (str): Barcode

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ProductDetailsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['barcode'] = \
                barcode
            return self.call_with_http_info(**kwargs)

        self.stock_products_by_barcode_barcode_get = _Endpoint(
            settings={
                'response_type': (ProductDetailsResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/stock/products/by-barcode/{barcode}',
                'operation_id': 'stock_products_by_barcode_barcode_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'barcode',
                ],
                'required': [
                    'barcode',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'barcode':
                        (str,),
                },
                'attribute_map': {
                    'barcode': 'barcode',
                },
                'location_map': {
                    'barcode': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__stock_products_by_barcode_barcode_get
        )

        def __stock_products_by_barcode_barcode_inventory_post(
            self,
            barcode,
            inline_object11,
            **kwargs
        ):
            """Inventories the by its barcode given product (adds/removes based on the given new amount)  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.stock_products_by_barcode_barcode_inventory_post(barcode, inline_object11, async_req=True)
            >>> result = thread.get()

            Args:
                barcode (str): Barcode
                inline_object11 (InlineObject11):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [StockLogEntry]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['barcode'] = \
                barcode
            kwargs['inline_object11'] = \
                inline_object11
            return self.call_with_http_info(**kwargs)

        self.stock_products_by_barcode_barcode_inventory_post = _Endpoint(
            settings={
                'response_type': ([StockLogEntry],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/stock/products/by-barcode/{barcode}/inventory',
                'operation_id': 'stock_products_by_barcode_barcode_inventory_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'barcode',
                    'inline_object11',
                ],
                'required': [
                    'barcode',
                    'inline_object11',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'barcode':
                        (str,),
                    'inline_object11':
                        (InlineObject11,),
                },
                'attribute_map': {
                    'barcode': 'barcode',
                },
                'location_map': {
                    'barcode': 'path',
                    'inline_object11': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__stock_products_by_barcode_barcode_inventory_post
        )

        def __stock_products_by_barcode_barcode_open_post(
            self,
            barcode,
            inline_object12,
            **kwargs
        ):
            """Marks the given amount of the by its barcode given product as opened  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.stock_products_by_barcode_barcode_open_post(barcode, inline_object12, async_req=True)
            >>> result = thread.get()

            Args:
                barcode (str): Barcode
                inline_object12 (InlineObject12):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [StockLogEntry]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['barcode'] = \
                barcode
            kwargs['inline_object12'] = \
                inline_object12
            return self.call_with_http_info(**kwargs)

        self.stock_products_by_barcode_barcode_open_post = _Endpoint(
            settings={
                'response_type': ([StockLogEntry],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/stock/products/by-barcode/{barcode}/open',
                'operation_id': 'stock_products_by_barcode_barcode_open_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'barcode',
                    'inline_object12',
                ],
                'required': [
                    'barcode',
                    'inline_object12',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'barcode':
                        (str,),
                    'inline_object12':
                        (InlineObject12,),
                },
                'attribute_map': {
                    'barcode': 'barcode',
                },
                'location_map': {
                    'barcode': 'path',
                    'inline_object12': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__stock_products_by_barcode_barcode_open_post
        )

        def __stock_products_by_barcode_barcode_transfer_post(
            self,
            barcode,
            inline_object10,
            **kwargs
        ):
            """Transfers the given amount of the by its barcode given product from one location to another (this is currently not supported for tare weight handling enabled products)  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.stock_products_by_barcode_barcode_transfer_post(barcode, inline_object10, async_req=True)
            >>> result = thread.get()

            Args:
                barcode (str): Barcode
                inline_object10 (InlineObject10):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [StockLogEntry]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['barcode'] = \
                barcode
            kwargs['inline_object10'] = \
                inline_object10
            return self.call_with_http_info(**kwargs)

        self.stock_products_by_barcode_barcode_transfer_post = _Endpoint(
            settings={
                'response_type': ([StockLogEntry],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/stock/products/by-barcode/{barcode}/transfer',
                'operation_id': 'stock_products_by_barcode_barcode_transfer_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'barcode',
                    'inline_object10',
                ],
                'required': [
                    'barcode',
                    'inline_object10',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'barcode':
                        (str,),
                    'inline_object10':
                        (InlineObject10,),
                },
                'attribute_map': {
                    'barcode': 'barcode',
                },
                'location_map': {
                    'barcode': 'path',
                    'inline_object10': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__stock_products_by_barcode_barcode_transfer_post
        )
