import json


# We can extract the information from the JSON file and use it to convert some currencies.
def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


def convert(amount: float, base_currency: str, to_currency: str, rates: dict[str, dict]) -> float:
    base_currency: str = base_currency.lower()
    to_currency: str = to_currency.lower()

    # None because the currency we're trying to retrieve the value for might not exist if we're mistyping
    from_rates: dict | None = rates.get(base_currency)
    to_rates: dict | None = rates.get(to_currency)

    # JSON data is by default converting everything from euros.
    # Conversion from EUR
    if base_currency == 'eur':
        # Use the target currency's rate against EUR
        return amount * to_rates['rate']

    # Conversion to EUR
    elif to_currency == 'eur':
        # Use the base currency's inverseRate to convert to EUR
        return amount * from_rates['inverseRate']

    # Conversion between two non-EUR currencies
    else:
        return amount * to_rates['rate'] / from_rates['rate']


def main() -> None:
    # Load the rates from a JSON file
    try:
        rates_file: dict[str, dict] = load_rates('python mini projects/rates.json')
    except FileNotFoundError:
        print("Error: The rates file could not be found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while loading rates: {e}")
        return

    try:
        result: float = convert(amount=15, base_currency='eur', to_currency='dkk', rates=rates_file)
        print(f"15 EUR is equal to {round(result, 2)} DKK")
    except KeyError as e:
        print(f"Currency error: {e}")
    except Exception as e:
        print(f"An error occurred during the initial conversion: {e}")

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            base_currency = input("Enter the base currency (PLN, USD, DKK, etc.): ").lower()
            to_currency = input("Enter the target currency (PLN, USD, DKK, etc.): ").lower()

            result = convert(amount, base_currency, to_currency, rates_file)
            print(f"{amount:.2f} {base_currency.upper()} is equal to {result:.2f} {to_currency.upper()}")

            again = input("Do you want to convert another amount? (yes/no): ").lower()
            if again != 'yes':
                break
        except ValueError:
            print("Error: Please enter a valid number for the amount.")
        except KeyError as e:
            print(f"Error: Currency not recognized. {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Run the main function if this script is executed directly.
if __name__ == '__main__':
    main()
