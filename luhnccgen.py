import random

def generate_credit_card_number(prefix):
    # Convert prefix to string
    prefix = str(prefix)

    # Generate remaining 9 digits randomly
    remaining_digits = ''.join(random.choices('0123456789', k=9))

    # Concatenate prefix and remaining digits
    credit_card_number = prefix + remaining_digits

    # Calculate the check digit using Luhn algorithm
    check_digit = generate_check_digit(credit_card_number)

    # Append the check digit to the credit card number
    credit_card_number += str(check_digit)

    return credit_card_number

def generate_check_digit(number):
    # Convert the credit card number to a list of integers
    digits = [int(x) for x in str(number)]

    # Double every second digit, starting from the right
    doubled_digits = [(2 * digit) if index % 2 == 0 else digit for index, digit in enumerate(digits[::-1])]

    # Subtract 9 from any digits that are greater than 9
    subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]

    # Calculate the sum of all digits
    total = sum(subtracted_digits)

    # Find the check digit that makes the total a multiple of 10
    check_digit = (10 - (total % 10)) % 10

    return check_digit

def generate_expiration_date():
    # Generate a random expiration month (between 1 and 12)
    month = random.randint(1, 12)

    # Generate a random expiration year (between 2024 and 2030)
    year = random.randint(2024, 2030)

    # Format the expiration date as MM/YY
    expiration_date = f"{month:02d}/{str(year)[-2:]}"

    return expiration_date

def generate_cvv():
    # Generate a random 3-digit CVV number
    cvv = random.randint(100, 999)

    return cvv

# Get the prefix from the user
prefix = input("Enter the 5-digit prefix: ")

# Generate the credit card number
credit_card_number = generate_credit_card_number(prefix)

# Generate the expiration date
expiration_date = generate_expiration_date()

# Generate the CVV number
cvv = generate_cvv()

# Print the generated credit card details
print("Generated Credit Card Number:", credit_card_number)
print("Expiration Date:", expiration_date)
print("CVV:", cvv)