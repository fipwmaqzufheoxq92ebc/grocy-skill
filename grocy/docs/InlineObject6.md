# InlineObject6


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_amount** | **int** | The new current amount for the given product - please note that when tare weight handling for the product is enabled, this needs to be the amount including the container weight (gross), the amount to be posted will be automatically calculated based on what is in stock and the defined tare weight | [optional] 
**best_before_date** | **date** | The due date which applies to added products | [optional] 
**shopping_location_id** | **float** | If omitted, no store will be affected | [optional] 
**location_id** | **float** | If omitted, the default location of the product is used (only applies to added products) | [optional] 
**price** | **float** | If omitted, the last price of the product is used (only applies to added products) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


