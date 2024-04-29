import requests
import os
from functools import lru_cache
from dotenv import load_dotenv
load_dotenv()

currencies = {
    "USD": 1.0,
    "EUR": 0.83,
    "GBP": 0.76,
    "JPY": 109.38
}

def convert_currency(amount, from_currency, to_currency):
    rate = to_currency / from_currency
    converted_amount = amount * rate
    return converted_amount

@lru_cache(maxsize=None)
def currency_converter():
    amount = float(input("Enter the amount: "))
    from_currency_url = f"https://v6.exchangerate-api.com/v6/{os.getenv('Currency_ENV')}/latest/USD"
    to_currency_url = f"https://v6.exchangerate-api.com/v6/{os.getenv('Currency_ENV')}/latest/USD"
    inp_from_currency = input("Enter the source currency (USD, EUR, GBP, JPY): ").upper()
    inp_to_currency = input("Enter the target currency (USD, EUR, GBP, JPY): ").upper()

    while 1:
        try:
            from_currency = requests.get(from_currency_url).json()["conversion_rates"][inp_from_currency]
            to_currency = requests.get(to_currency_url).json()["conversion_rates"][inp_to_currency]
            break
        except Exception:
            print("There was some problem getting the data you are trying to get. Try again")
    
    converted_amount = convert_currency(amount, from_currency, to_currency)

    print(f"{amount:.02f} {inp_from_currency} = {converted_amount:.02f} {inp_to_currency}")

if __name__ == "__main__":
    currency_converter()