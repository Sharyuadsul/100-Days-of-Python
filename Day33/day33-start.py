import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)

# if response.status_code == 404:
#     raise Exception("does not exist")

response.raise_for_status()

data = response.json()
# print(data)

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude,longitude)
print(iss_position)