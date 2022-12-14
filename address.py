#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: December 6, 2022
# This program asks the user for their mailing information
# and displays their mailing address formatted


# Formats the user's information into a mailing address
def format_address(
    name, street_num, street_name, city, province, postal_code, apartment_num=None
):

    # Initializes address variable
    address = ""

    # Concatenates user's name to address variable (with carriage returns)
    address += "\n" + name + "\n"

    # Checks if user lives inside of an apartment
    if apartment_num != None:
        address += apartment_num + "-"

    # Concatenates street address, city, province and postal code to address variable
    address += (
        street_num
        + " "
        + street_name
        + "\n"
        + city
        + " "
        + province
        + " "
        + postal_code
    )

    # Returns address variable to main()
    return address


def main():
    # Initialize Variable
    user_apartment_num = None

    # Asks user for their full name
    user_name = input("Enter your full name: ").upper()

    # Checks if the user lives in an apartment
    user_apartment = input("Do you live in an apartment? (y/n) ").upper()

    # If user does live inside of an apartment
    if user_apartment == "Y":
        user_apartment_num = input("Enter your apartment number (ex. 1A, 2B): ").upper()

    # Asks user for their street number
    user_street_num = input("Enter your street number : ").upper()

    # Asks user for their street name
    user_street_name = input(
        "Enter your street name AND type (ex. Main St., Flower Cres., etc.): "
    ).upper()

    # Asks user for their city
    user_city = input("Enter your city: ").upper()

    # Asks user for their province
    user_province = input(
        "Enter your province (As an abbreviation, i.e. ON, AB, etc.): "
    ).upper()

    # Asks user for their postal code
    user_postal_code = input("Enter your postal code (A1B 2C3): ").upper()

    # Calls function to format their mailing address
    user_mailing_address = format_address(
        user_name,
        user_street_num,
        user_street_name,
        user_city,
        user_province,
        user_postal_code,
        user_apartment_num,
    )

    # Displays to user their formatted mailing address
    print(f"\nYour canadian mailing address: {user_mailing_address}")


if __name__ == "__main__":
    main()
