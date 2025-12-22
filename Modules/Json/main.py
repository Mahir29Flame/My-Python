import json 

mr_json = ('''
{
  "category": "Electronics",
  "items": [
    {
      "id": 101,
      "name": "Laptop",
      "brand": "Dell",
      "price": 750.00,
      "specs": {
        "processor": "Intel i5",
        "ram": "8GB",
        "storage": "512GB SSD"
      }
    },
    {
      "id": 102,
      "name": "Smartphone",
      "brand": "Samsung",
      "price": 500.00,
      "specs": {
        "screen": "6.5 inch",
        "processor": "Exynos 2200",
        "ram": "8GB",
        "storage": "256GB",
        "battery": "4500mAh",
        "camera": "48MP"
      }
    }
  ]
}


''')

mr_dict = json.loads(mr_json)
print(mr_dict,type(mr_dict))
mr_json_str = json.dumps(mr_dict, indent=4)
print(mr_json_str,type(mr_json_str))

with open('Modules/Json/mr_json.json','w') as f:
    json.dump(mr_dict,f,indent=4)

with open('Modules/Json/mr_json.json','r') as f:
    mr_dict2 = json.load(f)
    print(mr_dict2,type(mr_dict2))

laptop_processor = mr_dict2["items"][0]["specs"]["processor"]
print("the laptop's Proccessor is: ", laptop_processor)