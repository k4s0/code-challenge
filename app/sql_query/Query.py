class Query():

  @staticmethod
  def sql_CheckHealth():
    return """
      select 
        'healthy' as status,
        to_char(sysdate, 'YYYY-MM-DD HH24:MI:SS') server_datetime
      from 
        dual
      """
  @staticmethod
  def sql_get_fake_db_data_1():
    return {
              "ecommerce_id": 1,
              "customer_id": 1,
              "cart_date_checkout":"2022-02-14",
              "item_list": [
                {
                  "product_sku": 1,
                  "product_name": "string",
                  "file_type": "application/pdf",
                  "quantity": 100,
                  "delivery_date": "2022-02-14",
                  "price":1.0
                },
                {
                  "product_sku": 3,
                  "product_name": "string",
                  "file_type": "application/pdf",
                  "quantity": 15,
                  "delivery_date": "2022-02-14",
                  "price":1.0
                },
                {
                  "product_sku": 1,
                  "product_name": "string",
                  "file_type": "application/pdf",
                  "quantity": 15,
                  "delivery_date": "2022-02-14",
                  "price":1.0
                },
                {
                  "product_sku": 2,
                  "product_name": "string",
                  "file_type": "application/pdf",
                  "quantity": 10,
                  "delivery_date": "2022-02-14",
                  "price":1.0
                }
              ]
            }
