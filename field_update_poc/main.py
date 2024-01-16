import json
import os
import pandas as pd
import requests
import logging
from modules.utilities.api import postToAPI, getFromAPI

from field_update_poc.modules.utilities.config import API_TOKEN

INPUT_FOLDER = './input'


#Hardcoded system field exclusions for field info
excluded_fields = ['Summary', 'Details', 'Category', 'Impact', 'Urgency', 'Asset']
exc_list = {"Summary":2, "Details":3, "Category": 5, "Impact":165,"Urgency":166,"Asset":4}


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



    
def main():
    df = importData()
    fields = df[~df['label'].isin(excluded_fields)].drop(columns=['Ticket Type', 'Mandatory (Y/N)', 'Agent Only'])    
    fieldJson = structureData(fields)
    
    # for row in fieldJson:
    #     print('-------------------')
    #     print(row)
    #     print('-------------------')
    
    #Post the new fields to the API
    # postToAPI(fieldJson, 'fieldinfo')
    
    #Add the new fields to the ticket types
    
    
    
    



if __name__ == "__main__":
    main()

