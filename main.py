""" 
version : 1.0
date : 04-01-2021 
"""

from cards import card_numbers, card_type_check, check_if_card_valid
from random import choice

# Get a random card to verify.
cc = key, ccnumber = choice(list(card_numbers.items())) 

print(f"Entered Cardnumber : {ccnumber}")

nummer = ["0","1","2","3","4","5","6","7","8","9"]
clean_card_nr = ""
user_card = ccnumber

# Remove unwanted chars and symbols.
for item in user_card:
    if item in nummer:
        clean_card_nr += item

print(f"Clean cardnumber : {clean_card_nr} ")
user_card = clean_card_nr

# Call Function to Check if Card is valid.
valid = check_if_card_valid(user_card)

# Call Function to Check what is the Card Type.
card_type = card_type_check(clean_card_nr)

# Display the results.
if valid:
    print(f"This a valid {card_type}")
else:
    print(f"This a none valid {card_type}")
