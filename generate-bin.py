import random

def generate_numbers(first_digit, amount):
    generated_numbers = []
    
    for _ in range(amount):
        # Generate a random number with 6 digits
        random_number = random.randint(10000, 99999)
        
        # Combine the first digit with the random number
        generated_number = int(str(first_digit) + str(random_number))
        
        # Add the suffix
        generated_number_with_suffix = str(generated_number) + "xxxxxxxxxx"
        
        generated_numbers.append(generated_number_with_suffix)
    
    return generated_numbers

# User input for the first digit and amount
first_digit = int(input("Enter the desired first digit of the bin: "))
amount = int(input("Enter the number bin(s) to generate: "))

# Generate the numbers
results = generate_numbers(first_digit, amount)

# Save the generated numbers to a text file
file_name = "generated_bin.txt"
with open(file_name, "w") as file:
    for number in results:
        file.write(number + "\n")

print(f"Generated numbers with suffix are saved in {file_name}.\nscript written by t.me/trustsamuel.")