import requests
from datetime import datetime

TOKEN = "tokenForPixelaAPI"
USERNAME = "mochis"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Training Graph",
    "unit": "h", 
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

while True:
    try:
        value = float(input("Type how long you worked out today. \nValidation rule: int, float[1-10]: "))
        if isinstance(value, float) and value <= 10:
            print("test")   
            pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"


            create_pixel_config = {
                "date": today.strftime("%Y%m%d"),
                "quantity": value,
            }

            # response = requests.post(url=pixel_creation_endpoint, headers=headers, json=create_pixel_config)
            # print(response.text)
        
        elif value == "quit".lower() or value == "exit".lower() or value == "q".lower():
            break
        
        elif value > 10:
            print("Value too high, try again and be better 💩.")

    except ValueError:
        print("WRONG, not a number. Try again and be better 💩.")
        


# update_pixel = {
#     "quantity": "0.32",
# }

# pixel_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# response = requests.put(url=pixel_update_endpoint, json=update_pixel, headers=headers)
# print(response.text)

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)
