import phonenumbers
from test import n
from phonenumbers import geocoder
ch_number= phonenumbers.parse(n ,"CH")
print(geocoder.description_for_number(ch_number, "en"))
from phonenumbers import carrier
service_number= phonenumbers.parse(n,"RO")
print(carrier.name_for_number(service_number, "en"))