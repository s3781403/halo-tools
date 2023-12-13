import pandas as pd
from modules.file_operations import systemConfigCheck, convertData, export
from modules.user_input import getTargetDataFile, getColumnNameAndSubtractHours

INPUT_FOLDER = './input'
    
def main():
    systemConfigCheck()
    # data = pd.read_csv('./input/data.csv')
    dataFileName=getTargetDataFile(input_folder_path=INPUT_FOLDER)
    
    data = pd.read_csv(f'{INPUT_FOLDER}/{dataFileName}')
    # getTarget()
    columnToConvert, hoursToSubtract = getColumnNameAndSubtractHours(data)
    adjustedDataFrame = convertData(data, columnToConvert, hoursToSubtract)
    
    export(adjustedDataFrame, dataFileName)
    


if __name__ == "__main__":
    main()



