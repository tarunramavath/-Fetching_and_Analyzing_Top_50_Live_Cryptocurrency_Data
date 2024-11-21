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
- **Streamlit** (optional, for visualizing data in real-time)
- **CoinGecko API** (for cryptocurrency data)

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `pandas`
  - `time`

You can install the required libraries using `pip`:
```bash
pip install requests pandas

