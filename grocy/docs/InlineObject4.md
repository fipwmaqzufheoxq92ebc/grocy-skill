# InlineObject4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to remove - please note that when tare weight handling for the product is enabled, this needs to be the amount including the container weight (gross), the amount to be posted will be automatically calculated based on what is in stock and the defined tare weight | [optional] 
**transaction_type** | [**StockTransactionType**](StockTransactionType.md) |  | [optional] 
**spoiled** | **bool** | True when the given product was spoiled, defaults to false | [optional] 
**stock_entry_id** | **str** | A specific stock entry id to consume, if used, the amount has to be 1 | [optional] 
**recipe_id** | **float** | A valid recipe id for which this product was used (for statistical purposes only) | [optional] 
**location_id** | **float** | A valid location id (if supplied, only stock at the given location is considered, if ommitted, stock of any location is considered) | [optional] 
**exact_amount** | **bool** | For tare weight handling enabled products, &#x60;true&#x60; when the given is the absolute amount to be consumed, not the amount including the container weight | [optional] 
**allow_subproduct_substitution** | **bool** | &#x60;True&#x60; when any in-stock sub product should be used when the given product is a parent product and currently not in-stock | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


