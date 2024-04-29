currencies = {
    "USD": 1.0,
    "EUR": 0.83,
    "GBP": 0.76,
    "JPY": 109.38
}

def convert_currency(amount, from_currency, to_currency):
    rate = currencies[to_currency] / currencies[from_currency]
    converted_amount = amount * rate
    return converted_amount

def currency_converter():
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency (USD, EUR, GBP, JPY): ").upper()
    to_currency = input("Enter the target currency (USD, EUR, GBP, JPY): ").upper()

    if from_currency not in currencies or to_currency not in currencies:
        print("Invalid currency")
        return
    
    converted_amount = convert_currency(amount, from_currency, to_currency)

    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

if __name__ == "__main__":
    currency_converter()