import json
import os
import pandas as pd

INPUT_FOLDER = './input'

excluded_fields = ['Summary', 'Details', 'Category', 'Impact', 'Urgency', 'Asset']

templ = {",usage": 1,"inputtype": "0","characterlimittype": "0","visibility": "1","tab_id": "0"}
json_template = json.dumps(templ)


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
        df_row_list.append(json_obj)
    
    print(df_row_list[1])
    

    
    
    
    


def main():
    df = importData()
    fields = df[~df['label'].isin(excluded_fields)].drop(columns=['Ticket Type', 'Mandatory (Y/N)', 'Agent Only'])    
    fieldJson = structureData(fields)

    
    
    # grouped_data = df.groupby('Ticket Type', 'label')
    # grouped_data = df.groupby(['Ticket Type', 'label'])
    # print(grouped_data.head(500))
    
    # for name, group in grouped_data:
        
    #     print(group)
    #     print('-------------------')
    # print(df)

if __name__ == "__main__":
    main()
