# Lorenzo's implementetion of Pixartprinting Code challenge: Cart API

## How to run the API

First step we need to install python3/pip and FastAPI framework.
Take a look to official framework page [FastAPI](https://fastapi.tiangolo.com/tutorial/)

- First step install requirements.txt with:
    ```pip install -r requirements.txt```  
- Now launch the application with: 
    ```python3 -m uvicorn app.main:app --reload```
- To see the OpenAPI documentation page is running at:
    ```http://127.0.0.1:8000/docs```

### - To Know -
My main purpose for this challenge was to show my ordinary project organization from an architectural point of view. 
For this reason I haven't entered the information in a test database so i haven't wanted to implement it, but the methods that should perform that function are structured to give an equivalent answer.

### Cart creation
```[POST] http://127.0.0.1:8000/cart/create```

Example request body :
{
  "ecommerce_id": 1,
  "customer_id": 1,
  "status": "created",
  "created_at": "2022-02-16T19:04:40.220Z",
  "updated_at": "2022-02-16T19:04:40.220Z"
}

### Add Items to Cart
```[POST] http://127.0.0.1:8000/cart/add/```
Example request body :
{
  "ecommerce_id": 1,
  "customer_id": 1,
  "item_list": [
    {
      "product_sku": 0,
      "product_name": "string",
      "file_type": "psd",
      "quantity": 0,
      "delivery_date": "2022-02-16T19:20:24.671000+00:00",
      "price": 2.45
    },
    {
      "product_sku": 0,
      "product_name": "string",
      "file_type": "ai",
      "quantity": 0,
      "delivery_date": "2022-02-16T19:20:24.671000+00:00",
      "price": 2.35
    },
    {
      "product_sku": 0,
      "product_name": "string",
      "file_type": "pdf",
      "quantity": 0,
      "delivery_date": "2022-02-16T19:20:24.671000+00:00",
      "price": 2.25
    }
  ]
}
**What have I done?**
As you can see inside the `CartService` class, when I insert the `Items` I have decided to apply the price policies that increase its price, i.e. the `mime_type` and the `delivery_date`, considering the fixed price of 1.0
**A doubt**
>The `file_type` as a string value indicating the file's MIME type

If you head over to IANA, which holds all the official MIME types, you’ll notice that Adobe Illustrator is not even mentioned. So i decided into the ItemDTO class to insert the file extension control instead the mime_type, to be consistent with pricing policies 
```__allowed_mime = ["application/pdf","image/vnd.adobe.photoshop"]```
```__allowed_ext = ["pdf","psd","ai"]```
### View a Cart

```[GET] http://127.0.0.1:8000/cart/1```

when the customer requests to display the cart, the price policies that discount the total are applied, considering the possibility of having more `Item` with the same `product_sku` the total quantity of all is considered and compared with the policies.

### Cart checkout

```[POST] http://127.0.0.1:8000/cart/checkout/100```

## Final Consideration

The test was very stimulating, and I really enjoyed doing it. I take this opportunity to thank you for the time you have dedicated to me. 
Best regards Lorenzo.