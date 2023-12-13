from modules.colors import bcolors
import os
import time
from modules.file_operations import displayFiles
from modules.animations import doLoadingAnimation


#Asks the user for the name of the file, from a list of files in the input folder
def getTargetDataFile(input_folder_path):
    #scan input folder for csv files
    inputFiles = [file for file in os.listdir(input_folder_path) if file.lower().endswith(".csv")]
    
    if len(inputFiles) == 0:
        print(f"{bcolors.FAIL}Error: No csv input file found{bcolors.ENDC}")
        print('Please add a csv file to the input folder and try again')
        time.sleep(5)
        exit()
        
    elif len(inputFiles) > 1:
        doLoadingAnimation(phrase='Scanning...')
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
    elif len(inputFiles) == 1:
        print(f"{bcolors.OKGREEN}File selected: {inputFiles[0]}!{bcolors.ENDC}")
        return inputFiles[0]

#Get user input for column name and hours to subtract
def getColumnNameAndSubtractHours(data):
    while True:
        try:
            columnToConvert = input('Enter the column name to convert (exact spelling): ')
            
            #Loading animation to make you think things are happening quickly
            doLoadingAnimation(phrase='Loading',num_iter=1)
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
            if hoursToSubtract > 48 or hoursToSubtract < -48:
                print(f"{bcolors.FAIL}Error: Number must be between 48 and -48")
                hoursToSubtract=0
                continue
            else: 
                break
        except ValueError:
            print(f"{bcolors.WARNING}Warning: Please enter a number{bcolors.ENDC}")
            continue
             
    return columnToConvert, hoursToSubtract


