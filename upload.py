import requests
import base64
import json

# Your credentials
email = "andreasfischer0201@gmail.com"
api_key = "4K004S8L8CxP43vo867NfZa88L5Q018e"

# Base64 encode the credentials
credentials = f"{email}:{api_key}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# URL for the POST request
url = "http://localhost/cscart/api/products"

# Headers
headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/json"
}

# Create a session object
session = requests.Session()
session.headers.update(headers)

# Data for the new product (example)
product_data = {
    "product_id": "12",
    "product": "100g Pants",
    "product_type": "P",
    "status": "A",
    "price": 100,
    "company_id": "1",
    "list_price": "31.00",
    "amount": "10",
    "weight": "0.000",
    "length": "0",
    "width": "0",
    "height": "0",
    "shipping_freight": "0.00",
    "low_avail_limit": "0",
    # Add other necessary fields as per your CS-Cart configuration
}
while True:
    # Make the POST request
    response = session.post(url, data=json.dumps(product_data))

    # Handle the response
    if response.status_code == 201:
        print("Product successfully created:", response.json())
    else:
        print("Failed to create product:", response.status_code, response.text)

# Close the session
session.close()
