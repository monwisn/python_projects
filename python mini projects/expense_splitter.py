

def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    share_per_person: float = total_amount / number_of_people

    print(f'Total expenses: {total_amount:,.2f} {currency}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {share_per_person:,.2f} {currency} (approximately)')


# live templates
def main() -> None:
    while True:
        try:
            print('Split Expenses Calculator: ')
            total_amount = float(input('Enter total expenses: '))
            if total_amount <= 0:
                raise ValueError('Total amount must be a non-negative number.')

            number_of_people = int(input('Enter number of people: '))
            if number_of_people < 1:
                raise ValueError('Number of people must be greater than one.')

            currency = input('Enter currency (e.g., USD, EUR, PLN): ')
            calculate_split(total_amount, number_of_people, currency)

            end = input('Press "q" to Quit the Calculator')
            if end == 'q':
                break
            else:
                continue

        except ValueError as e:
            print(f'Error: {e}')

        except Exception as err:
            print(f'An unexpected error occurred: {err}')


if __name__ == '__main__':
    main()
