import json
import os
import pandas as pd
import requests

INPUT_FOLDER = './input'

excluded_fields = ['Summary', 'Details', 'Category', 'Impact', 'Urgency', 'Asset']

templ = {"usage": 1,"inputtype": "0","characterlimittype": "0","visibility": "1","tab_id": "0"}
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
        json_obj.update(templ)
        
        df_row_list.append(json_obj)
        
    return df_row_list
    # print(df_row_list[1])
    #Michael helped write this part
    
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
    
def getAccessToken():
    # Implement logic to obtain and return the access token using your client ID and secret
    # This might involve making a request to the service's token endpoint

    # Example (you would replace this with your actual implementation):
    # token_url = 'https://example.com/token'
    # token_data = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
    # response = requests.post(token_url, data=token_data)
    # return response.json().get('access_token')

    # For testing purposes, you can replace this with a hardcoded token (not recommended for production):
    return 'CfDJ8C8c7b5bmLJBrnc7HjACq1uQ2k171TotAm3X81GCDVPb0eA8GH_fg9y-bDDQqrv8CiQo2VcKxl7p5kvvFXXCQIp-iVZ1GLKtwe6qLG-tDfFWsUZ_x1sapJRc2qlbV2lk1ekCPKArXr04RIAd0H7dAnHf86z4b88ZjQJn--fAUkFINkqTxPkfd0zqVJghO2iXS3pZ6-TGKtRC5DnWaQrqtA2mFLfjspmHTUTox5IwVh81b-6Q4FWzcwjYUzCQs96B98RK7BH4FdBHcQGaEicVgAbm4ODZrWu42OOFiinyt477K3TKZPmctsE5HvTt5Ld7IaXa4PHeaIz8w1va_9kX4tlHuo0tyOY2eXtSXiU_H0xUpi4NrvF6tXv4k9JjEoJuWH9seRskXst2yF0sgeGNcSM0p80kG-aS8T1WAnjoXhb9y_V3gYkMq3UCQaTKbLoJG2odn-aBbUcjB8wb4fokVBY1wuX9CkTHbS9Vrco4cZ_KtVL_64H0hQEclNnefBtG_IddcCkEV_7YchxDuJFuma7uS4GYGp4OtJV4qtX8pN0YzjCQnNpGqKD6y0_jDF4JiiF0MM_1wZF_EdnP3PeEpNHIR1C2m9KXYP3szxe3jRqbKvQSOwTALucF2fPpl4RqTW_XzLjARl8rBiWwGGXy_1mOOK_oMOqk83b44ePbikY_zmAMw-i9zum6xMoRPOzrM63KR0-Gr8d6KWkWbgaFQWLr91J9GL97hGHhJDS9yHe69NNVuvYCBIw3EEhaYjqD0yJnPP5mBbB9XwPc5jNlW0-krNTnbUhW6-yGU-UjEZOBeat3h8gdApekZtpSimkR0ay3q36ykumm40hUa3Gio_B2EG4fCbM6lKoPkX9rf3IuHpM_8ANqTPua7X5pKT5IRybIvPd-_wbaWPTV6vLGQnmEN6LHaEwhBZIQW-2v8bpxf_cSmG3dbHA__ykK4GvUR6wNxFZW_v4T6R0_zQnpMLb4ntWLtKMYSsci_CAB2LgKjZlO16dOXgKHMn73XJY5hGD8pWowwt-uOHH8axNc3_av1czapJ34aNhau8y5L-9hJOs3p3d8C3jFvM2TaCim7UkHlTsTyns0lL3aoCgug9A7BlkzfaRcnWaSBq1wA1Gb0575qKkYEWnTJJ8E5xYhocHoj2Mx9xepe59ixmngXGCgTo_VuxesDCO-j9RovCDI7p1zXu6sZ_KV8G88dWd8m7pbKj1l2KqLhYnVUqVtU6m_LCsHygCHDDzuLhbHkkRgfhX-JHgOZlEBTDhsrrhC8-Rsh8v__0RCS431im1J56xc9LOckhjZrJsJYOfZyLL-4tSCLmVHc4yeI2S7Ik2SzEH2IV6rhpZDCb7FjOlrqSsGBe7L1M59h-suOZ_0ajHad0gdjqHLN4fBeNNyNWif-P4NKpH2bracdQxMx92enGy5OJibwS3z2QMlIkuqYuSRTbmui8dbdZHu9gCGEvgaMK09jhxzMT3WOjHNEVPxO_Jn7iQNrjWlMCqFqs8MIftJDpGeMalsn1nkj9BA7EsA8DngMF9UQOe2KAWsb1USX3HoY7s63V4HcCxS4VR1dr1-F_9kVaIIqQ-ZHdv5FfjJwsUTo2b4FbnoDEDbjCCX1GCGllJCOJgvIgonHCU26nVxt6j1eyd5d7PPu_xmEh2181z7exIN0mMliWMpbfmsrpiPh5CjYfAV-8Moi76Cuc6s77p-kPAuGFbFVGxM8ZrMjN8V-b07ERNiO4uVZMAGjLUxzb7nx9EmdWcEMCnHsm94fiPE2PsQYWsoxUAgq7XYtG4HdbpBtaVReFVms5_wuKKIPKQ-AOoHEXdN2tJz9LoazdXqhU9jst7iJphRhW0XirOOW0LQrhpJQUk_yO6TxSBzVDrel54EDKyBsCxkNsMtrgHBSvq3UgrzoQGSr9Qub-NpOksZpoKk5KRhamSUYXRJVHfpBQNS1YHdGATWfSCNk_5ql3PICS4EhHacsLngijFA5sK8JoJysHPAqb0WGXQi1uUtWmaW4x2_Qxf46USv4AWQGgcWQKGFHeqMVjQTlCfa2VKI30sP4yQT_s_7XmaN9NNP24IoUihtn2GIlH4rUL0aF0UTISR4K3YESpEuBbf6cmFnldzONc-L2gVImbi9q80wypGqqTw6A_qt0DbSA6K_7URdVRlJPlE8c4QYtUEwcTT_W_jymxuDkrRrKFA_Npy50P7VNCdRzzkv0tGzx8KQu_0SA3lV9nShKze-rkPo76qD8SSh4u2kTUEdOQ6487SpdOv7lmMicMfTETF-diBK2rRbkXTp8mydPM_LLJNxeiMWKHpbpLlYI55Bq9JsfxsYRGCtD_gihshLS6ZF1E5pfCltsUNiYivAC3_JLOd3AUH5Ohct8Ed8avWb_9yYF2Kndhi9UuWYv7nTMSK1wtujSLhYIi3rVucV5v5D4dbQJPHXUPj-uma-O00VPoT_EYmE2-8rDkT58h0KBY21jeQQlCXuUKJxnFvf-yYbnj0IRyJmV87ekPs3feotbIzGI-K5A2Qd79EmsA2KuOsZGMCbIZmjNQ2AZU5k2y8EUs_lpvfoSKJb8lkNKDqWBMUpJdDdp14KPiwf89Sd8mwDZeSgOvCTWuYN9b-TxbjR-dOLTWpW2lJ8W7NvKFtacCeupQeS10N36-UcMJMS5lSJltsqvTpv0Anbi6XfJvSAgkTyJfj2ZP704apDg1FWH2sPmiG-WuNOU8n9qJ7-myiFdNqbw2qlWJqkMYnneQVN1Q'


def main():
    df = importData()
    fields = df[~df['label'].isin(excluded_fields)].drop(columns=['Ticket Type', 'Mandatory (Y/N)', 'Agent Only'])    
    fieldJson = structureData(fields)
    
    for row in fieldJson:
        print('-------------------')
        print(row)
        print('-------------------')
    sendToAPI(fieldJson)
        
    
    
    
    # grouped_data = df.groupby('Ticket Type', 'label')
    # grouped_data = df.groupby(['Ticket Type', 'label'])
    # print(grouped_data.head(500))
    
    # for name, group in grouped_data:
        
    #     print(group)
    #     print('-------------------')
    # print(df)

if __name__ == "__main__":
    main()
