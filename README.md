# -Fetching_and_Analyzing_Top_50_Live_Cryptocurrency_Data
Top 50 Cryptocurrency Live Data Fetching
Project Overview
This project fetches live data for the top 50 cryptocurrencies by market capitalization using the CoinGecko API. It provides key metrics like current price, market capitalization, 24-hour trading volume, and percentage price change over the last 24 hours.

The project is implemented in Python and continuously updates the data, which can be used for analysis, visualizations, or as part of a larger cryptocurrency tracking system.

Key Features
Fetches live data of top 50 cryptocurrencies.
Includes the following data points for each cryptocurrency:
Name: The name of the cryptocurrency.
Symbol: The symbol of the cryptocurrency.
Current Price (USD): The current market price of the cryptocurrency.
Market Capitalization: The total market value of the cryptocurrency.
24h Trading Volume: The volume of the cryptocurrency traded in the last 24 hours.
Price Change (24h): The percentage change in price over the last 24 hours.
Data is refreshed every 5 minutes to ensure real-time accuracy.
Technologies Used
Python (for scripting and data handling)
Requests (for API calls)
Pandas (for data manipulation and analysis)
Streamlit (optional, for visualizing data in real-time)
CoinGecko API (for cryptocurrency data)
Prerequisites
Python 3.x
Required Python libraries:
requests
pandas
time
You can install the required libraries using pip:

bash
Copy code
pip install requests pandas
How to Run the Project
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/top-50-cryptocurrency.git
cd top-50-cryptocurrency
Run the Script: To fetch and display the data:

bash
Copy code
python fetch_crypto_data.py
This will fetch the live data from CoinGecko, display the top 50 cryptocurrencies, and save the data to a CSV file (Python_live_crypto.csv).

Set Up Auto-Refresh (Optional):

The script updates the data every 5 minutes to ensure the most recent information is available.
You can also integrate this script with Streamlit for a real-time interactive dashboard.
Code Walkthrough
fetch_crypto_data.py
This Python script fetches the top 50 cryptocurrencies' data using the CoinGecko API.
It processes the data using Pandas and saves it as a CSV file (Python_live_crypto.csv).
The script runs in a loop and updates the data every 5 minutes.
python
Copy code
import requests
import pandas as pd
import time

class FetchData:
    def get_top_50_cryptos(self):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",              
            "order": "market_cap_desc",      
            "per_page": 50,                  
            "page": 1
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df = df[[
                "name", 
                "symbol", 
                "current_price", 
                "market_cap", 
                "total_volume", 
                "price_change_percentage_24h"
            ]]
        return df

def update_crypto_data():
    obj = FetchData()
    crypto_data = obj.get_top_50_cryptos()
    print(crypto_data)
    crypto_data.to_csv("Python_live_crypto.csv", index=False)
    time.sleep(300)  # Update every 5 minutes
    update_crypto_data()

if __name__ == "__main__":
    update_crypto_data()
How it Works
API Request: The get_top_50_cryptos() method sends a request to the CoinGecko API and retrieves data for the top 50 cryptocurrencies.
Data Processing: The JSON response is converted to a pandas DataFrame, with the relevant columns extracted.
Auto-Refresh: The time.sleep(300) pauses the program for 5 minutes, after which the data is refreshed.
Streamlit Integration (Optional)
You can integrate this script with Streamlit for a live dashboard:

python
Copy code
import streamlit as st
import pandas as pd

# Load data and display it in a table
df = pd.read_csv("Python_live_crypto.csv")
st.write(df)
How to Use Streamlit:
Install Streamlit:

bash
Copy code
pip install streamlit
Run the Streamlit app:

bash
Copy code
streamlit run streamlit_app.py
This will display the data in a user-friendly dashboard.

Contributing
Feel free to fork this repository and make improvements. If you find any issues or would like to suggest enhancements, please open an issue or submit a pull request.

