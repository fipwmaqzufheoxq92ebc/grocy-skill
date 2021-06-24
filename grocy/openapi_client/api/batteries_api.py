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
from openapi_client.model.battery_charge_cycle_entry import BatteryChargeCycleEntry
from openapi_client.model.battery_details_response import BatteryDetailsResponse
from openapi_client.model.current_battery_response import CurrentBatteryResponse
from openapi_client.model.error400 import Error400
from openapi_client.model.error500 import Error500
from openapi_client.model.inline_object22 import InlineObject22


class BatteriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __batteries_battery_id_charge_post(
            self,
            battery_id,
            inline_object22,
            **kwargs
        ):
            """Tracks a charge cycle of the given battery  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.batteries_battery_id_charge_post(battery_id, inline_object22, async_req=True)
            >>> result = thread.get()

            Args:
                battery_id (int): A valid battery id
                inline_object22 (InlineObject22):

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
                BatteryChargeCycleEntry
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
            kwargs['battery_id'] = \
                battery_id
            kwargs['inline_object22'] = \
                inline_object22
            return self.call_with_http_info(**kwargs)

        self.batteries_battery_id_charge_post = _Endpoint(
            settings={
                'response_type': (BatteryChargeCycleEntry,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/batteries/{batteryId}/charge',
                'operation_id': 'batteries_battery_id_charge_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'battery_id',
                    'inline_object22',
                ],
                'required': [
                    'battery_id',
                    'inline_object22',
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
                    'battery_id':
                        (int,),
                    'inline_object22':
                        (InlineObject22,),
                },
                'attribute_map': {
                    'battery_id': 'batteryId',
                },
                'location_map': {
                    'battery_id': 'path',
                    'inline_object22': 'body',
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
            callable=__batteries_battery_id_charge_post
        )

        def __batteries_battery_id_get(
            self,
            battery_id,
            **kwargs
        ):
            """Returns details of the given battery  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.batteries_battery_id_get(battery_id, async_req=True)
            >>> result = thread.get()

            Args:
                battery_id (int): A valid battery id

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
                BatteryDetailsResponse
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
            kwargs['battery_id'] = \
                battery_id
            return self.call_with_http_info(**kwargs)

        self.batteries_battery_id_get = _Endpoint(
            settings={
                'response_type': (BatteryDetailsResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/batteries/{batteryId}',
                'operation_id': 'batteries_battery_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'battery_id',
                ],
                'required': [
                    'battery_id',
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
                    'battery_id':
                        (int,),
                },
                'attribute_map': {
                    'battery_id': 'batteryId',
                },
                'location_map': {
                    'battery_id': 'path',
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
            callable=__batteries_battery_id_get
        )

        def __batteries_charge_cycles_charge_cycle_id_undo_post(
            self,
            charge_cycle_id,
            **kwargs
        ):
            """Undoes a battery charge cycle  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.batteries_charge_cycles_charge_cycle_id_undo_post(charge_cycle_id, async_req=True)
            >>> result = thread.get()

            Args:
                charge_cycle_id (int): A valid charge cycle id

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
                None
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
            kwargs['charge_cycle_id'] = \
                charge_cycle_id
            return self.call_with_http_info(**kwargs)

        self.batteries_charge_cycles_charge_cycle_id_undo_post = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/batteries/charge-cycles/{chargeCycleId}/undo',
                'operation_id': 'batteries_charge_cycles_charge_cycle_id_undo_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'charge_cycle_id',
                ],
                'required': [
                    'charge_cycle_id',
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
                    'charge_cycle_id':
                        (int,),
                },
                'attribute_map': {
                    'charge_cycle_id': 'chargeCycleId',
                },
                'location_map': {
                    'charge_cycle_id': 'path',
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
            callable=__batteries_charge_cycles_charge_cycle_id_undo_post
        )

        def __batteries_get(
            self,
            **kwargs
        ):
            """Returns all batteries incl. the next estimated charge time per battery  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.batteries_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                query ([str]): An array of filter conditions, each of them is a string in the form of `<field><condition><value>` where<br>`<field>` is a valid field name<br>`<condition>` is a comparison operator, one of<br>&nbsp;&nbsp;`=` equal<br>&nbsp;&nbsp;`!=` not equal<br>&nbsp;&nbsp;`~` LIKE<br>&nbsp;&nbsp;`!~` not LIKE<br>&nbsp;&nbsp;`<` less<br>&nbsp;&nbsp;`>` greater<br>&nbsp;&nbsp;`<=` less or equal<br>&nbsp;&nbsp;`>=` greater or equal<br>&nbsp;&nbsp;`§` regular expression<br>`<value>` is the value to search for. [optional]
                order (str): A valid field name by which the response should be ordered, use the separator `:` to specify the sort order (`asc` or `desc`, defaults to `asc` when omitted). [optional]
                limit (int): The maximum number of objects to return. [optional]
                offset (int): The number of objects to skip. [optional]
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
                [CurrentBatteryResponse]
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
            return self.call_with_http_info(**kwargs)

        self.batteries_get = _Endpoint(
            settings={
                'response_type': ([CurrentBatteryResponse],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/batteries',
                'operation_id': 'batteries_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'query',
                    'order',
                    'limit',
                    'offset',
                ],
                'required': [],
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
                    'query':
                        ([str],),
                    'order':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'query': 'query[]',
                    'order': 'order',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'query': 'query',
                    'order': 'query',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                    'query': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__batteries_get
        )
