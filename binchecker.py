import requests

def identify_bin_info(bin_number):
    # Send a GET request to the binlist.io API
    response = requests.get(f"https://api.binlist.io/v1/{bin_number}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the country and issuer information
        country = data.get('country', {}).get('name')
        issuer = data.get('bank', {}).get('name')

        return country, issuer

    # Return None if the request was unsuccessful
    return None, None

# Get the BIN from the user
bin_number = input("Enter the BIN: ")

# Identify the origin country and issuer
origin_country, issuer = identify_bin_info(bin_number)

# Print the origin country and issuer
if origin_country and issuer:
    print("Origin Country:", origin_country)
    print("Issuer:", issuer)
else:
    print("Could not identify the origin country and issuer for the given BIN.")
