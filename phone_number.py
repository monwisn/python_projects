import phonenumbers

from phonenumbers import geocoder

phone_number = phonenumbers.parse("Number with country code")
# for example: Area code for Poland: +48 XXXXXXXXX
# phone_number = phonenumbers.parse("+48123456789")

# this will print the country name
print(geocoder.description_for_number(phone_number, 'en'))


