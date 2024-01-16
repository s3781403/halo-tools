import requests
import logging
from modules.utilities.config import API_TOKEN



#Sends data to the api via a hardcoded url
#TODO: make dynamic, and allow the user to enter their bearer info
def postToAPI(data, endpoint):
    url = f'https://oliverhale.internal.halopsa.com/api/{endpoint}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }
    response = requests.post(url, headers=headers, json=data)
    showResponseStatus(response)
        
    logging.info(f"====================\POST PERFORMED\n===================\nStatus code: {response.status_code}\n Result: {response.text}\n")


#Makes a GET request to an endpoint
def getFromAPI(endpoint):
    url = f'https://oliverhale.internal.halopsa.com/api/{endpoint}'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {getAccessToken()}'
        }
    response = requests.get(url, headers=headers)
    showResponseStatus(response)

    logging.info(f"====================\nGET REQUEST PERFORMED\n===================\nStatus code: {response.status_code}\n")
    
    return response

def showResponseStatus(response):
    if response.status_code in range(200,299):
        print("Request successful")
        print(f"Response: {response.status_code}")
    else:
        print(f"Error sending data. Status code: {response.status_code}, Response: {response.text}")
    

#Unimplemented
#TODO: Implement
def getAccessToken():
    # Implement logic to obtain and return the access token using your client ID and secret
    # This would involve making a request to the auth server

    # token_url = 'https://example.halo.com/auth'
    # token_data = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
    # response = requests.post(token_url, data=token_data)
    # return response.json().get('access_token')

    # For testing purposes, you can replace this with a hardcoded token (not recommended for production):
    return API_TOKEN

def retrieveFieldIDs(fields):
    response = getFromAPI('fieldinfo')
        
    if response.status_code in (200,299):
        json_data=response.json()
        field_ids = [entry['id'] for entry in json_data if entry.get("label") in fields]
    else:
        print("No values to parse")
        return
    
    return field_ids
        
        