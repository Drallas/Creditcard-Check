""" Card Numbers to check: 
https://developer.paypal.com/docs/payflow/payflow-pro/payflow-pro-testing
"""

# List of Cards to Test
card_numbers = {
"American Express 1": '3782 8224 6310 005',
"American Express 2": '371449635398431',
"American Express 3": '378734493671000',
"Diners Club": '30569309025904',
"Discover 1": '6011111111111117',
"Discover 2": '6011000990139424',
"JCB 1": '3530111333300000',
"JCB 2 ": '3566002020360505',
"Mastercard 1": '2221000000000009',
"Mastercard 2": '2223000048400011',
"Mastercard 3": '2223016768739313',
"Mastercard 4": '5555555555554444',
"Mastercard 5": '51051/05105/1051/00',
"Visa 1": '4111111111111111',
"Visa 2": '4012888888881881',
"Visa 3": '4222-223-222-222',
"Visa 4": '4222-232-222-222'
}


def check_card_type(card):
    """Function takes a Card number and returns Brand name or None"""
    if int(card[0:2]) == 34 or int(card[0:2]) == 37:
        return "American Express"
    elif int(card[0:2])in range(51, 56) or int(card[0:2]) == 22:
        return "MasterCard"
    elif int(card[0:2]) == 35:
        return "JCB"
    elif int(card[0:2]) == 30:
        return "Diners Club"
    elif int(card[0:1]) == 6:
        return "Discover"
    elif int(card[0:1]) == 4:
        return "Visa"

def check_if_card_valid(card):
    """Function takes a Card number and returns True or False if it's valid."""
    result1 = []
    result2 = []
    result3 = []

    for item in range(len(card) -2, -1, -2):
        nr1 = int(card[item])* 2
        result1 += str(nr1)
    
    for number in result1:
        result2.append(int(number))

    for item in range(len(card) -1, -1, -2):
        result3.append(int(card[item]))

    if (sum(result2) + sum(result3)) % 10 == 0:
        return True
    else:
        return False
