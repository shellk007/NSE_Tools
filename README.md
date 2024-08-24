# NSE_Tools
Starting this repo as a simple PE scrapper for the list of all listed companies on NSE. This may evolve into something else in time that may be useful in analyzing stocks.
**Overview**
This repository contains a Python script for calculating the Price-to-Earnings (PE) ratios of stocks listed on the NSE (National Stock Exchange of India). The script retrieves stock information from Yahoo Finance and saves the results to an Excel file. The output includes company names, market capitalizations, sectors, industries, and PE ratios.

**Features**
**Fetch PE Ratios**: Retrieves the PE ratio of stocks using Yahoo Finance.
**Company Details**: Includes company names and market capitalizations.
**Sector and Industry Information**: Adds sector and industry details for each stock.
**Configurable Processing**: Allows you to specify the number of stocks to process.
**File Handling**: Deletes existing output files and saves the updated data.
**Requirements**
Python 3.x
yfinance library
pandas library
openpyxl library (for Excel file handling)
You can install the required Python libraries using pip:

pip install yfinance pandas openpyxl

**Usage**
Prepare Your Input File:

Create an Excel file named NSE_list.xlsx with a column named Symbol containing the stock symbols.
**Run the Script:**

Download or clone this repository.
Navigate to the directory containing the script.
Execute the script using Python:

python pe_calculator.py
**Check the Output:**

The script will generate a file named NSE_list_with_PE_ratios.xlsx containing the updated stock information.
Configuration
num_stocks_to_process: Configure the number of stocks to process by changing this variable in the script. For example, set num_stocks_to_process = 100 to process only the top 100 stocks.
**Example**
Here's an example of how to modify the script to process only the top 50 stocks:

# Configuration variable for the number of stocks to process
num_stocks_to_process = 50
**Troubleshooting**
If you encounter issues with missing libraries, ensure that you have all required packages installed.
If the script fails to fetch data for some stocks, it may be due to connectivity issues or changes in the Yahoo Finance API.
**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Acknowledgements**
Yahoo Finance API for stock data.
pandas for data manipulation.
yfinance for accessing financial data.
