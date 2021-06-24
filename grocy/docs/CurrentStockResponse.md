# CurrentStockResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**amount_aggregated** | **float** |  | [optional] 
**amount_opened** | **float** |  | [optional] 
**amount_opened_aggregated** | **float** |  | [optional] 
**best_before_date** | **date** | The next due date for this product | [optional] 
**is_aggregated_amount** | **bool** | Indicates wheter this product has sub-products or not / if the fields &#x60;amount_aggregated&#x60; and &#x60;amount_opened_aggregated&#x60; are filled | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


