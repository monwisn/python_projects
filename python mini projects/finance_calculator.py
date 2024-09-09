
# function returns None, that just means we're only meant to execute the function, we're not returning anything
# type annotations are not required in our code, use it if you enjoy the benefits of type annotations
# The type annotations are a good practice as they help make code more readable and catch type-related issues earlier
def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax

    yearly_income: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_income - yearly_tax  # this is the result we subtract the tax from our salary

    # Calculate finances
    print('---------------------------------')
    print(f'Monthly income: {monthly_income:,.2f} {currency}')  # comma ',' = thousands separator, '.2' = decimal places
    print(f'Tax rate: {tax_rate:,.0f} %')  # this will round it to zero decimal places
    print(f'Monthly tax: {monthly_tax:,.2f} {currency}')
    print(f'Monthly net income: {monthly_net_income:,.2f} {currency}')
    print('---------------------------------')
    print(f'Yearly salary: {yearly_income:,.2f} {currency}')
    print(f'Yearly tax paid: {yearly_tax:,.2f} {currency}')
    print(f'Yearly net income: {yearly_net_income:,.2f} {currency}')


calculate_finances(4580, 18, 'PLN')
calculate_finances(12300, 12, 'PLN')
calculate_finances(3620, 22, 'PLN')


def main():
    while True:
        try:
            monthly_income: float = float(input('Enter your monthly salary: '))
            tax_rate: float = float(input('Enter your tax rate (%): '))

            # Check for non-negative values
            if monthly_income < 0 or tax_rate < 0:
                print("Income and tax rate must be positive numbers. Please try again.")
                continue

            calculate_finances(monthly_income, tax_rate, currency='PLN')
            break
        except ValueError as e:
            print(f"You've entered an incorrect type. {e}. Please try again.")


# will only run if we run this script directly
if __name__ == '__main__':
    main()
