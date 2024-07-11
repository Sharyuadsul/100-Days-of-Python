#all code done with the help of Pixela API Doc

import requests
import datetime as dt

pixela_url = "https://pixe.la/v1/users"

USER ="sharyuadsul19"
TOKEN = "sjbyfywhsbajnvKSNIU3Y437"  #randomly chosen unique

#creating user account
user_params = {
    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#
# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)

#Creating a Graph
graph_endpoint= f"{pixela_url}/{USER}/graphs"
graph_id= "graph1"

graph_config={
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"sora",
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#creating a pixel on the graph
add_pixel_endpoint = f"{graph_endpoint}/{graph_id}"
today = dt.datetime(year=2024, month=7, day=8)
# print(today)

pixel_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"15",
}


# response = requests.post(url = add_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# response = requests.post(url = add_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

#FOR UPDATION

update_pixel_endpoint = f"{add_pixel_endpoint}/{today.strftime("%Y%m%d")}"
update_data = {
    "quantity":"20",   #updated the value from 12 to 20 km
}

# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# print(response.text)

#DELETING a pixel

# pixel_delete_endpoint = f"{add_pixel_endpoint}/{today.strftime("%Y%m%d")}"
#
# response= requests.delete(url=pixel_delete_endpoint, headers=headers)


#------------------------------------------------------------------

#creating a pixel on the graph
add_pixel_endpoint = f"{graph_endpoint}/{graph_id}"
today = dt.datetime.now()

pixel_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many Kilometers did you run today?"),
}


response = requests.post(url = add_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

#check the graph on  https://pixe.la/v1/users/sharyuadsul19/graphs/graph1.html