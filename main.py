""" 
version : 1.1
date : 25-12-2021
"""

from cards import card_numbers, check_card_type, check_if_card_valid
from random import choice

# Global Variables
clean_card_nr = ""

# A random Credit Card number is retrieved from the card_numbers list and assigned to the variable card_to_to_verify.
card_to_to_verify = choice(list(card_numbers.items()))

# Unpack the tuple and map the values to the variables card_type and card_num values.
card_type = card_to_to_verify[0]
card_num = card_to_to_verify[1]

print(f"Card Brand : {card_type} & Card Number : {card_num}")

# Filter out unwanted chars (space, -, /, etc ) keepping only (0-9)
for char in card_num:
    if char.isdigit():
        clean_card_nr += char

# Call the function to Check if Card is valid.
valid = check_if_card_valid(clean_card_nr)

# Call the function to Check what is the Card Type.
card_type = check_card_type(clean_card_nr)

# Display the results of the check.
if valid:
    print(f"This a valid {card_type}")
else:
    print(f"This an invalid {card_type}")
