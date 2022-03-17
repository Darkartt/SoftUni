import phonenumbers
from phonenumbers import geocoder, timezone, carrier

number = ""
ch_number = phonenumbers.parse(number)

timezone = timezone.time_zones_for_number(ch_number)
print(timezone)

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

ch_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(ch_number, "en"))