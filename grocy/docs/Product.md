# Product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**qu_id_purchase** | **int** |  | [optional] 
**qu_id_stock** | **int** |  | [optional] 
**enable_tare_weight_handling** | **int** |  | [optional] 
**not_check_stock_fulfillment_for_recipes** | **int** |  | [optional] 
**product_group_id** | **int** |  | [optional] 
**qu_factor_purchase_to_stock** | **float** |  | [optional] 
**tare_weight** | **float** |  | [optional] 
**barcode** | **str** | Can contain multiple barcodes separated by comma | [optional] 
**min_stock_amount** | **int** |  | [optional]  if omitted the server will use the default value of 0
**default_best_before_days** | **int** |  | [optional]  if omitted the server will use the default value of 0
**default_best_before_days_after_open** | **int** |  | [optional]  if omitted the server will use the default value of 0
**picture_file_name** | **str** |  | [optional] 
**row_created_timestamp** | **datetime** |  | [optional] 
**shopping_location_id** | **int** |  | [optional] 
**userfields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Key/value pairs of userfields | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


