import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "ovie"
PASSWORD = "abcd123456"

pixela_parameter = {
    "token": PASSWORD,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# user_creation_response = requests.post(url=pixela_endpoint, json=pixela_parameter)
# print(user_creation_response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "readgraph1",
    "name": "Reading graph",
    "unit": "Hour",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PASSWORD
}

# graph_creation_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_creation_response.text)

today = dt.datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
pixel_config = {
    "date": today.strftime("%Y%m%%d"),
    "quantity": "10"
}

# pixel_creation_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_creation_response.text)