import yfinance as yf
import pandas as pd
import time
import os

# Configuration variable for the number of stocks to process
num_stocks_to_process = 1000  # Change this to the desired number (e.g., 100, 200, 500)

# Load the Excel file
file_path = 'NSE_list.xlsx'  # Assuming the file is in the same directory as the script
df = pd.read_excel(file_path)

# Add a new column for PE Ratios
df['PE Ratio'] = None

# Limit the DataFrame to the specified number of stocks
df_to_process = df.head(num_stocks_to_process)

# Loop through each symbol and fetch the PE ratio
for index, row in df_to_process.iterrows():
    symbol = row['Symbol'] + '.NS'
    print(f"Working on stock: {symbol}")  # Print which stock is being processed
    try:
        stock = yf.Ticker(symbol)
        pe_ratio = stock.info.get('trailingPE', None)  # Get the PE ratio
        df.at[index, 'PE Ratio'] = pe_ratio
        print(f"PE Ratio for {symbol}: {pe_ratio}")  # Print the fetched PE ratio
    except Exception as e:
        print(f"Failed to get data for {symbol}: {e}")
    
    # Sleep for 2 seconds to avoid hitting API rate limits
    time.sleep(1)

# Output file path
output_file_path = 'NSE_list_with_PE_ratios.xlsx'  # Save in the same directory

# Delete the output file if it already exists
if os.path.exists(output_file_path):
    os.remove(output_file_path)
    print(f"Existing file {output_file_path} deleted.")

# Save the updated DataFrame back to the Excel file
df.to_excel(output_file_path, index=False)

print(f"Updated Excel file saved to: {output_file_path}")
