# Check week number of your birth date (then translate your week day to Spanish)
import datetime
import calendar


# match case only if you have python 3.10 or upper
def translate_to_spanish(day_name):
    match day_name:
        case 'Monday':
            return 'Lunes'
        case 'Tuesday':
            return 'Martes'
        case 'Wednesday':
            return 'Miércoles'
        case 'Thursday':
            return 'Jueves'
        case 'Friday':
            return 'Viernes'
        case 'Saturday':
            return 'Sábado'
        case 'Sunday':
            return 'Domingo'


date_of_birth = input("Enter your date of birth in the format day-month-year (e.g. 1-1-2000): ")

# unpacking the  data
day, month, year = date_of_birth.split("-")  # (1, 1, 2000)

# variable override
# convert str to int
date_of_birth = datetime.datetime(int(year), int(month), int(day))

# show the day of week (int)
print(date_of_birth.weekday())

# show the day of week (name)
day_name = calendar.day_name[date_of_birth.weekday()]
print(day_name)

# translate day name
print(translate_to_spanish(day_name))
