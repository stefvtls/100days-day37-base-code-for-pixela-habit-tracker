import requests
import datetime as dt
from dotenv import load_dotenv
import os

today = dt.date.today()
today = str(today).replace("-", "")
yesterday = dt.datetime(year=2022, month=6, day=9).strftime("%Y%m%d")

load_dotenv()
USERNAME = os.getenv("USERNAME_LOG")
TOKEN = os.getenv("TOKEN")
headers = {"X-USER-TOKEN": TOKEN}
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_JSON = {"token": TOKEN, "username": USERNAME, "agreeTermsOfService": "yes", "notMinor": "yes" }
PIXELA_ENDPOINT_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_JSON_GRAPH = {"id": "graph1", "name": "time tracker", "unit": "minute", "type": "int", "color": "ajisai"}
PIXELA_JSON_GRAPH_2 = {"id": "graph2", "name": "km tracker", "unit": "km", "type": "float", "color": "kuro"}
POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT_GRAPH}/{PIXELA_JSON_GRAPH_2['id']}"
POST_PIXEL_JSON = {"date": yesterday, "quantity": "9.0"}
UPDATE_PIXEL_ENDPOINT = f"{POST_PIXEL_ENDPOINT}/{yesterday}"
UPDATE_PIXEL_JSON = {"quantity": "20.0"}

# CREATE A USER
# response_pixela = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_JSON)
# response_pixela.raise_for_status()
# print(response_pixela.status_code)
# print(response_pixela.text)

# CREATE A GRAPH
# response_pixela_graph = requests.post(url=PIXELA_ENDPOINT_GRAPH, json=PIXELA_JSON_GRAPH, headers=headers)
# response_pixela_graph.raise_for_status()
# print(response_pixela_graph.status_code)
# print(response_pixela_graph.text)
# CREATE A GRAPH 2
# response_pixela_graph_2 = requests.post(url=PIXELA_ENDPOINT_GRAPH, headers=headers, json=PIXELA_JSON_GRAPH_2)
# response_pixela_graph_2.raise_for_status()
# print(response_pixela_graph_2.status_code)
# print(response_pixela_graph_2.text)
#
# CREATE A PIXEL
# response_post_pixel = requests.post(url=POST_PIXEL_ENDPOINT, headers=headers, json=POST_PIXEL_JSON)
# response_post_pixel.raise_for_status()
# print(response_post_pixel.status_code)
# print(response_post_pixel.text)

# UPDATE PIXEL
# response_update = requests.put(url=UPDATE_PIXEL_ENDPOINT, headers=headers, json=UPDATE_PIXEL_JSON)
# response_update.raise_for_status()
# print(response_update.status_code)
# print(response_update.text)

# DELETE PIXEL
# response_delete = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
# response_delete.raise_for_status()
# print(response_delete.status_code)
# print(response_delete.text)
