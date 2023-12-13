import pandas as pd
import os
import time

#TODO: pull out loading animation into its own separate function to be called whenever a loading screen is needed
# Can have a variable for the word to use when displaying animation (.e.g loading, scanning, etc)

input_folder = './input'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
loading_chars = ['|', '/', '-', '\\']


def displayFiles(files):
    print('Select from these options:')
    for i,fileName in enumerate(files):
        print(f"[{i}]: {fileName}")


#check for input, ouptut and archive folders
def systemConfigCheck():
    if not os.path.exists('./input'):
        os.makedirs('./input')
    if not os.path.exists('./out'):
        os.makedirs('./out')
    if not os.path.exists('./archive'):
        os.makedirs('./archive')



#Add a check here that asks the user for the name of the data file
def getTarget():
    #scan input folder for csv files
    inputFiles = [file for file in os.listdir(input_folder) if file.lower().endswith(".csv")]
    
    if len(inputFiles) == 0:
        print(f"{bcolors.FAIL}Error: No csv input file found{bcolors.ENDC}")
        print('Please add a csv file to the input folder and try again')
        time.sleep(5)
        exit()
        
    elif len(inputFiles) > 1:
        for _ in range(2):  # Adjust the number of iterations as needed
            for char in loading_chars:
                print(f"\rScanning... {char}", end='')
                time.sleep(0.1)  # Adjust the sleep duration as needed
        print(f"{bcolors.OKBLUE}\rMultiple files found!{bcolors.ENDC}")
        
        displayFiles(inputFiles)
        
        while True:
            try:
                inputFileName = input('Enter the file you would like to process: ')
                
                if inputFileName in inputFiles:
                    # Do something with the file
                    print(f"{bcolors.OKGREEN}File selected: {inputFileName}!{bcolors.ENDC}")
                    return inputFileName
                    
                else:
                    try:
                        selection = inputFiles[int(inputFileName)]
                        print(f"{bcolors.OKGREEN}File selected: {inputFiles[int(inputFileName)]}!{bcolors.ENDC}")
                        return selection
                    except Exception as e:
                        print(f"{bcolors.FAIL}Error: File not found{bcolors.ENDC}")
                        # print(e)
                        continue
            except ValueError:
                print(f"{bcolors.WARNING}Warning: Please enter a valid file name{bcolors.ENDC}")
                continue



#Get user input for column name and hours to subtract
def getUserInput(data):
    while True:
        try:
            columnToConvert = input('Enter the column name to convert (exact spelling): ')
            
            #add a dummy loading bar here to make it look like it's doing something for a second or two
            for _ in range(2):  # Adjust the number of iterations as needed
                for char in loading_chars:
                    print(f"\rLoading... {char}", end='')
                    time.sleep(0.1)  # Adjust the sleep duration as needed

            data[columnToConvert]
            print(f"\r{bcolors.OKGREEN}Found column!{bcolors.ENDC}")
            break
        except KeyError:
            print(f"\r{bcolors.FAIL}Failed. Enter a valid column name{bcolors.ENDC}")
            continue
    
    #prompt the user to enter the number of hours to subtract
    while True:
        try:
            hoursToSubtract = int(input('Enter the number of hours to subtract: '))
            
            break
        except ValueError:
            print(f"{bcolors.WARNING}Warning: Please enter a number{bcolors.ENDC}")
            continue
             
    return columnToConvert, hoursToSubtract





def convert(df, columnToConvert, hoursToSubtract):
    print(f"{bcolors.OKCYAN}Converting...{bcolors.ENDC}")
    
    #Convert specified column to datetime format
    df[columnToConvert] = pd.to_datetime(df[columnToConvert])
    
    #Subtract specified number of hours from the column
    df[columnToConvert] = df[columnToConvert] - pd.Timedelta(hours=hoursToSubtract)

    #Format the dates into the desired form
    df[columnToConvert] = pd.to_datetime(df[columnToConvert], format='%Y/%m/%dT%H:%M:%S')

    return df
    
    
    
    
    
def export(df, inputFileName):
    #Export the data to a new csv file with the date/time it was created in the name
    current_datetime = pd.to_datetime('now', utc=True).strftime('%y%m%d_%H%M%S')
    
    output_name = f'./out/data_{current_datetime}.csv'
    archive_name = f'./archive/{inputFileName.rstrip(".csv")}_{current_datetime}.csv'
    
    try:
        #Convert dataFrame to CSV and export it, Move the input file to the archive folder
        df.to_csv(output_name, index=False)
        # os.rename('./input/data.csv', archive_name)
        
        print(f"{bcolors.OKGREEN}\n-----Success!-----{bcolors.ENDC}")
        print('Data has been formatted and exported to a new file in ./out/ - marked by date/time processed.')
        print('Check the output folder for your new file! ')
    except Exception as e:
        print(f"{bcolors.FAIL}Error: Something went wrong{bcolors.ENDC}")
        print(e)
        
    os.rename(f"./input/{inputFileName}", archive_name)
    
    
def main():
    systemConfigCheck()
    # data = pd.read_csv('./input/data.csv')
    dataFileName=getTarget()
    data = pd.read_csv(f'{input_folder}/{dataFileName}')
    # getTarget()
    columnToConvert, hoursToSubtract = getUserInput(data)
    adjustedDataFrame = convert(data, columnToConvert, hoursToSubtract)
    
    export(adjustedDataFrame, dataFileName)
    


if __name__ == "__main__":
    main()



