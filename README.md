# Fetching_and_Analyzing_Top_50_Live_Cryptocurrency_Data
## Top 50 Cryptocurrency Live Data Fetching

## Project Overview

This project fetches live data for the top 50 cryptocurrencies by market capitalization using the **CoinGecko API**. It provides key metrics like current price, market capitalization, 24-hour trading volume, and percentage price change over the last 24 hours.

The project is implemented in **Python** and continuously updates the data, which can be used for analysis, visualizations, or as part of a larger cryptocurrency tracking system.

## Key Features
- Fetches live data of top 50 cryptocurrencies.
- Includes the following data points for each cryptocurrency:
  - **Name**: The name of the cryptocurrency.
  - **Symbol**: The symbol of the cryptocurrency.
  - **Current Price (USD)**: The current market price of the cryptocurrency.
  - **Market Capitalization**: The total market value of the cryptocurrency.
  - **24h Trading Volume**: The volume of the cryptocurrency traded in the last 24 hours.
  - **Price Change (24h)**: The percentage change in price over the last 24 hours.
- Data is refreshed every 5 minutes to ensure real-time accuracy.

## Technologies Used
- **Python** (for scripting and data handling)
- **Requests** (for API calls)
- **Pandas** (for data manipulation and analysis)
- **CoinGecko API** (for cryptocurrency data)

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `pandas`
  - `time`
## How to Set Up Live Updating Excel Sheet

### Step 1: Fetch Cryptocurrency Data using Python

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/crypto-live-update-excel.git
    cd crypto-live-update-excel
    ```

2. **Run the Python Script**:
    The Python script fetches live data and saves it to a CSV file (`live_crypto_data.csv`).
    ```bash
    python fetch_crypto_data.py
    ```

    This script fetches data for the top 50 cryptocurrencies and stores it in the CSV file. The script will run continuously, updating the CSV file every 5 minutes.

---

### Step 2: Set Up Power Query in Excel for Live Updates

1. **Open Excel** and create a new workbook.
2. **Go to the "Data" tab**, click on **"Get Data"**, and select **"From File" > "From Text/CSV"**.
3. **Select the `live_crypto_data.csv` file** that was created by the Python script.
4. In the **"Navigator" window**, select the file and click on **"Load"**.

---

### Step 3: Set Auto Refresh

1. **Right-click the data table** and choose **"Table"** > **"External Data Properties"**.
2. In the **"Connection Properties"** window, set the **refresh interval** to **5 minutes** under the **"Refresh every"** option.

---

Now, Excel will automatically refresh the data every 5 minutes, pulling the updated data from the CSV file, which is being updated by the Python script.

