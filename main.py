import json
import datetime
import time
import requests

cookie_price = round(requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]["BOOSTER_COOKIE"]["quick_status"]["sellPrice"])

suppliedMoney = float(input("how much money do u have\n>>> "))

print(f"you can buy {round(suppliedMoney * (675/5.99) / 325)} booster cookies")
print(f"the exchange rate of 1 USD to Hypixel Skyblock coin as of {time.strftime('%d-%m-%Y DD-MM-YYYY %H:%M %Z', time.gmtime(time.time()))} is {round((cookie_price / 325) * (675/5.99)):,}")
