# InlineObject10


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to transfer - please note that when tare weight handling for the product is enabled, this needs to be the amount including the container weight (gross), the amount to be posted will be automatically calculated based on what is in stock and the defined tare weight | [optional] 
**location_id_from** | **float** | A valid location id, the location from where the product should be transfered | [optional] 
**location_id_to** | **float** | A valid location id, the location to where the product should be transfered | [optional] 
**stock_entry_id** | **str** | A specific stock entry id to transfer, if used, the amount has to be 1 | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


