import pandas as pd
from modules.file_operations import systemConfigCheck, convertData, export
from modules.user_input import getTargetDataFile, getColumnNameAndSubtractHours

INPUT_FOLDER = './input'
    
def main():
    systemConfigCheck()
    dataFileName=getTargetDataFile(input_folder_path=INPUT_FOLDER)
    
    #Convert using read_csv if dataFileName is a csv, otherwise use read_excel
    if dataFileName.lower().endswith(".csv"):
        data = pd.read_csv(f'{INPUT_FOLDER}/{dataFileName}')
    elif dataFileName.lower().endswith(".xlsx"):
        data = pd.read_excel(f'{INPUT_FOLDER}/{dataFileName}',engine='openpyxl')
    else:
        print("Error: File must be a csv or xlsx")
        exit()
    
    
    # getTarget()
    columnToConvert, hoursToSubtract = getColumnNameAndSubtractHours(data)
    adjustedDataFrame = convertData(data, columnToConvert, hoursToSubtract)
    
    export(adjustedDataFrame, dataFileName)
    


if __name__ == "__main__":
    main()



