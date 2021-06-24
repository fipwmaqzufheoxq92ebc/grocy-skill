# InlineObject3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to add - please note that when tare weight handling for the product is enabled, this needs to be the amount including the container weight (gross), the amount to be posted will be automatically calculated based on what is in stock and the defined tare weight | [optional] 
**best_before_date** | **date** | The due date of the product to add, when omitted, the current date is used | [optional] 
**transaction_type** | [**StockTransactionType**](StockTransactionType.md) |  | [optional] 
**price** | **float** | The price per stock quantity unit in configured currency | [optional] 
**location_id** | **float** | If omitted, the default location of the product is used | [optional] 
**shopping_location_id** | **float** | If omitted, no store will be affected | [optional] 
**print_stock_label** | **bool** | True when the stock entry label should be printed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


