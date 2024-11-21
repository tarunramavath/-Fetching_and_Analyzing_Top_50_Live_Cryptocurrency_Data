import requests
import pandas as pd
import time

class Fetch_data:
    def Top_50_cryptocurrency():
        url = "https://api.coingecko.com/api/v3/coins/markets"        # using coingeko api key
        parameters = {
            "vs_currency": "usd",           # currancy in usd
            "order": "market_cap_desc",     # in decending order
            "per_page": 50,                 # in a single page 50 details
            "page": 1                       
        }
        response = requests.get(url, params=parameters)
        if response.status_code == 200:         
            data = response.json()
            df = pd.DataFrame(data)
            # extracting the required fields from fetched data
            df = df[[
                "name", 
                "symbol", 
                "current_price", 
                "market_cap", 
                "total_volume", 
                "price_change_percentage_24h"
            ]]
        return df

def rec_excel():
    obj = Fetch_data            # Creating an object
    crypt_data=obj.Top_50_cryptocurrency()
    print(crypt_data)
    print("Wait 5 mins to update......")
    # Saving the updated cryptocurrency for every 5 minutes using python
    crypt_data.to_csv("Python_live_crypto.csv",index=False)        # Saving the updated data for every 5 minutes
    time.sleep(300)             # 300 seconds = 5 minutes
    rec_excel()

if __name__ == "__main__":
    rec_excel()
