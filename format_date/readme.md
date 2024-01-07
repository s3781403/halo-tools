# Halo Tools

## Table of Contents

- [Halo Tools](#halo-tools)
  - [Table of Contents](#table-of-contents)
  - [Installation \& How to Use](#installation--how-to-use)
    - [Method One](#method-one)
    - [Optional Steps](#optional-steps)
  - [Description](#description)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)


## Installation & How to Use

### Method One

[1] Clone the repository to your local machine.

[2] Ensure you have python3 installed on your system (if you don't, you can download it [here](https://www.python.org/downloads/)).

[3] Install the required packages by running `pip install -r requirements.txt` in the project directory in your terminal

[4] Run the project by running `python3 main.py` in the project directory.
  
[5] The program will create the required folder structure in the same directory as the executable file.

[6] Place the csv/xlsx file(s) you want to edit in the input folder.

[7] Run the program again (`python3 main.py`).

[8] Select the file you want to edit.

[9] Enter the column you want to edit (make sure its a date/time friendly column - no processing occurs to filter out your ugly values yet).

[10] Enter the number of hours you want to adjust the column by.

[11] The program will output the edited file to the output folder.


### Optional Steps
[1] (Optional) Install pyinstaller (run `pip install pyinstaller` in your terminal)

[2] (Optional) Create an executable file by running `pyinstaller main.py` in the halo-tools folder.

[3] (Optional) Run the executable file in the dist/main folder that is created.

## Description
Currently an obsessively complex way to format a date column in a csv file and then output it into a new file.

Was previously ~6 lines of code, but the intention is to make it useable / relatively foolproof for other people (by providing some minimal CLI functionality) and to make it more flexible (by allowing the user to specify the input files, the column to change and the number of hours to adjust).

Additional tools will be incorporated later! (I hope)

Let me know if you have any suggestions or requests.

## Usage

Use me to adjust the date/time values in a csv/xlsx file by a specified number of hours, then output the data into a Halo friendly format for import.

## Contributing

To contribute to the project, feel free to fork the repository and submit a pull request (or talk to me)

## License

This project is licensed under the GNU GPLv3 license. See [LICENSE](license.md) for more information.