import random
import string


def generate_random_characters(length):
    return ''.join(random.choices(string.printable, k=length))


while True:
    length = int(
        input("Enter the length of random characters (or 0 to exit): "))
    if length == 0:
        break
    random_characters = generate_random_characters(length)
    print("Random Characters:", random_characters)
