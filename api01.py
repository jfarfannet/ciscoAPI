import requests
import urllib.parse

url = "https://nextmedicall.tk/admin/values/"
json_data = requests.get(url).json()
print(json_data["code"])
# print(json_data["message"])
resp = json_data["message"]

for item in resp:
    print(item["especialidad"], ' ', item["precio"])