from Fetch_Live_Data import Fetch_data
import pandas as pd

data=Fetch_data.Top_50_cryptocurrency()

class data_analysis:
    def top_5_crypto():
        # Top 5 crypto currancy based on market_cap
        top_5_crypto_cap=data.nlargest(5,"market_cap")
        return top_5_crypto_cap
    def avg_top_50_cryto():
        # Average of all top 50 crypto currancy current_price
        average_top_50=data["current_price"].mean()
        return average_top_50
    def highest_24hr_price_change():
        # Highest price change
        highest_change = data.loc[data["price_change_percentage_24h"].idxmax()]
        return highest_change
    def lowest_24hr_price_change():
        # Lowest price change
        lowest_change = data.loc[data["price_change_percentage_24h"].idxmin()]
        return lowest_change

if __name__=="__main__":
    obj=data_analysis
    top_5=obj.top_5_crypto()
    avg=obj.avg_top_50_cryto()
    high_price=obj.highest_24hr_price_change()
    low_price=obj.lowest_24hr_price_change()
    print(f"Top 5 crypto currancy are : \n {top_5} \n ")
    print(f"Average of top 50 crypto currancy is {avg} \n ")
    print(f"Highest 24 hours pice change is \n {high_price} \n ")
    print(f"Lowest 24 hours price change is \n {low_price}")