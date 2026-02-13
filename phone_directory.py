# store phone numbers with names
phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}

# function to check if the phone number is valid (10 digits and numbers only)
def is_valid_number(number):
    if len(number) != 10:
        return False

    # check each character to make sure it is a digit
    for char in number:
        if char < '0' or char > '9':
            return False
    
    return True

# function to search for a name using the phone number
def find_name_by_number():
    phone_number = input("Enter phone number: ")

    # first check if the number is valid
    if is_valid_number(phone_number):

        # check if number exists in the dictionary
        if phone_number in phone_book:
            print(phone_book[phone_number])
        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")

# search by name
def find_number_by_name():
    name = input("Enter name: ")

    # loop through dictionary to find matching name
    for number, owner in phone_book.items():
        if owner == name:
            print(number)
            return
    
    print("Sorry, the name is not found")

# function to add a new contact to the phone book
def add_new_contact():
    new_name = input("Enter new name: ")
    new_number = input("Enter new number: ")

    # validate the new number before adding
    if is_valid_number(new_number):
        phone_book[new_number] = new_name
        print("Contact added")
    else:
        print("This is invalid number")

# call the functions to run
find_name_by_number()
find_number_by_name()
add_new_contact()
