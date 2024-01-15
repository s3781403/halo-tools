import json
import os
import pandas as pd
import requests
import logging

from config import API_TOKEN

INPUT_FOLDER = './input'


#Hardcoded system field exclusions for field info
excluded_fields = ['Summary', 'Details', 'Category', 'Impact', 'Urgency', 'Asset']

#Template for the API request to update fields
templ = {"usage": 1,"inputtype": "0","characterlimittype": "0","visibility": "1","tab_id": "0"}
json_template = json.dumps(templ)

logging.basicConfig(filename='api_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

#ingests a hardcoded csv or excel file
#TO DO: Pull the format_date excel selector into a library and use here instead
def importData():
    dataFileName = "./field_update_poc/test2.csv"
    
    if dataFileName.lower().endswith(".csv"):
        data = pd.read_csv(f'{dataFileName}')
    elif dataFileName.lower().endswith(".xlsx"):
        data = pd.read_excel(f'{dataFileName}',engine='openpyxl')
    else:
        print("Error: File must be a csv or xlsx")
        exit()
        
        
    return data

#prepare a dataframe to JSON format
def structureData(df):
    
    # Loop through the dataframe and change the value for Single Select where it exists to 2
    for df_index, df_row in df.iterrows():
        if df_row['type'] == 'Single Select':
            df.at[df_index, 'type'] = '2'
        elif df_row['type'] == 'Multi Select':
            df.at[df_index, 'type'] = '3'
        else:
            df.at[df_index, 'type'] = '1'
          
    # Add a column called name and set it to label, with whitespace stripped
    df['name'] = df['label'].str.replace(' ', '')
    
    df_row_list = []
    
    # Separate each row of the dataframe into a separate JSON object and put it into an array
    for _, row in df.iterrows():
        json_obj = row.to_json()
        json_obj = json.loads(json_obj)
        json_obj.update(templ)
        
        df_row_list.append(json_obj)
        
    return df_row_list
    # print(df_row_list[1])
    #Michael helped write this part

#Sends data to the api via a hardcoded url
#TODO: make dynamic, and allow the user to enter their bearer info
def sendToAPI(data):
    url = 'https://oliverhale.internal.halopsa.com/api/fieldinfo'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code in range(200, 299):
        print("Data sent successfully!")
        print(f"Response: {response.status_code}")
    else:
        print(f"Error sending data. Status code: {response.status_code}, Response: {response.text}")
        
    logging.info(f"Status code: {response.status_code}\n Result: {response.text}")
    
          

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
    return ''


def main():
    df = importData()
    fields = df[~df['label'].isin(excluded_fields)].drop(columns=['Ticket Type', 'Mandatory (Y/N)', 'Agent Only'])    
    fieldJson = structureData(fields)
    
    for row in fieldJson:
        print('-------------------')
        print(row)
        print('-------------------')
        
    sendToAPI(fieldJson)


if __name__ == "__main__":
    main()
