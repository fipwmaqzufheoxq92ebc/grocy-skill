# StockLogEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**best_before_date** | **date** |  | [optional] 
**purchased_date** | **datetime** |  | [optional] 
**used_date** | **datetime** |  | [optional] 
**spoiled** | **bool** |  | [optional]  if omitted the server will use the default value of False
**stock_id** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**transaction_type** | [**StockTransactionType**](StockTransactionType.md) |  | [optional] 
**row_created_timestamp** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


