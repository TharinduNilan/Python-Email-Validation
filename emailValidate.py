#import reguler expression library
from ast import pattern
import re
pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
user_id=input("Enter the Email Address : ")

#Checking if the entered value is valid
if re.search(pattern, user_id):
    print("Valid email address ")
else:
    print("Invalid email address ")