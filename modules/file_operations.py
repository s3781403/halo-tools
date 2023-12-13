import os
import pandas as pd
from modules.colors import bcolors
from time import sleep

def displayFiles(files):
    print('Select from these options:')
    for i,fileName in enumerate(files):
        print(f"[{i}]: {fileName}")


#check for input, ouptut and archive folders
def systemConfigCheck():
    print(f"{bcolors.OKCYAN}Doing initial setup...{bcolors.ENDC}")
    if not os.path.exists('./input'):
        os.makedirs('./input')
    if not os.path.exists('./out'):
        os.makedirs('./out')
    if not os.path.exists('./archive'):
        os.makedirs('./archive')
        

def convertData(df, columnToConvert, hoursToSubtract):
    print(f"\r{bcolors.OKCYAN}Converting...{bcolors.ENDC}")
    
    try:
        #Convert specified column to datetime format    
        df[columnToConvert] = pd.to_datetime(df[columnToConvert])
        #Subtract specified number of hours from the column
        df[columnToConvert] = df[columnToConvert] - pd.Timedelta(hours=hoursToSubtract)
        #Format the dates into the desired form
        df[columnToConvert] = pd.to_datetime(df[columnToConvert], format='%Y/%m/%dT%H:%M:%S')
        
    except Exception as e :
        print(f"{bcolors.FAIL}Error: Failed to convert column to datetime. Double-check there aren't any strange values.{bcolors.ENDC}")
        print(f'\n{bcolors.FAIL}System Error Message:{bcolors.ENDC}\n{e}')
        sleep(3)
        exit()
        
    print(f"\r{bcolors.OKGREEN}Converted!{bcolors.ENDC}")
    return df


def export(df, inputFileName):
    #Export the data to a new csv file with the date/time it was created in the name
    current_datetime = pd.to_datetime('now', utc=True).strftime('%y%m%d_%H%M%S')
    
    output_name = f'./out/data_{current_datetime}.csv'
    
    archive_name = f'./archive/{inputFileName.rstrip(".csv.xlsx")}_{current_datetime}.csv'
    
    try:
        #Convert dataFrame to CSV and export it, Move the input file to the archive folder
        df.to_csv(output_name, index=False)
        os.rename(f"./input/{inputFileName}", archive_name)
        
        print(f"{bcolors.OKGREEN}\n-----Success!-----{bcolors.ENDC}")
        print('Data has been formatted and exported to a new file in ./out/ - marked by date/time processed.')
        print('Check the "out" folder for your new file!')
    except Exception as e:
        print(f"{bcolors.FAIL}Error: Something went wrong{bcolors.ENDC}")
        print(e)
        
    