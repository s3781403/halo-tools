# Project Name
Halo Tools

## Description
Currently an obsessively complex way to format a date in a csv file and then output it into a new file.

Was previously ~6 lines of code, but the intention is to make it useable / relatively foolproof for other people (by providing some minimal CLI functionality) and to make it more flexible (by allowing the user to specify the input files, the column to change and the number of hours to adjust).

Currently sits as a single file, but will be split into multiple files.

Ideally, additional tools will then be incorporated into the project.

## Table of Contents

- [Project Name](#project-name)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Method One](#method-one)
    - [Method Two](#method-two)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

### Method One
Use the executable file in the dist folder. 

[1] Download the dist folder.

[2] Run the executable file.

### Method Two
Run the project from source. 

[1] Clone the repository to your local machine.

[2] Ensure you have python3 installed on your system (if you don't, you can download it [here](https://www.python.org/downloads/)).

[3] Install the required packages by running `pip install -r requirements.txt` in the project directory.

[4] Run the project by running `python3 formatDate.py` in the project directory.


## Usage

On first run the program will scan the current directory for the necessary folder structure. If it doesn't find it, it will create it.
It then looks in the input folder for any csv files. If it finds any, it will ask you to select one. It will then ask you to select the column you want to change and the number of hours you want to change it by. It will then output the file to the output folder.

## Contributing

To contribute to the project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the GNU GPLv3 license. See [LICENSE](license.md) for more information.