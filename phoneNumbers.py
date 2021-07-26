import phonenumbers
from phonenumbers import carrier, geocoder

phoneNo = input("Enter PhoneNo: ")

phNo = phonenumbers.parse(phoneNo)
print(geocoder.description_for_number(phNo, 'en'))
print(carrier.name_for_number(phNo, 'en'))