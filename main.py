import requests


print("""Currency Converter
Enter Your Currency, Desired Currency and the amount of money 
""")

cache = []
cache_dict = {}
user_currency = input("Enter Your Currency: ").lower()
r = requests.get(f"http://www.floatrates.com/daily/{user_currency}.json").json()

if "usd" not in cache_dict and user_currency != "usd":
    cache.append("usd")
    cache_dict["usd"] = r["usd"]
if "eur" not in cache_dict and user_currency != "eur":
    cache.append("eur")
    cache_dict["eur"] = r["eur"]

while True:
    desired_currency = input("Enter Desired Currency: ").lower()

    if desired_currency == "":
        break

    else:
        amount = int(input("Enter the amount: "))
        if desired_currency in cache:
            desired_currency_rate = cache_dict[desired_currency]["inverseRate"]
            print("Checking the cache...")
            print("Oh! It is in the cache!")
            print(f"You received {round(amount / desired_currency_rate, 2)} {desired_currency.upper()}.")

        elif desired_currency not in cache:
            cache.append(desired_currency)
            cache_dict[desired_currency] = r[desired_currency]
            desired_currency_rate = cache_dict[desired_currency]["inverseRate"]
            print("Checking the cache...")
            print("Sorry, but it is not in the cache!")
            print(f"You received {round(amount / desired_currency_rate, 2)} {desired_currency.upper()}.")
