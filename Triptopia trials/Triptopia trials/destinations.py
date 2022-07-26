def print_options():
    # Print travel options
    print("Travel Options")
    print("--------------")
    print("1. London")
    print("2. Paris")
    print("3. New York")
    print("4. Chennai")
    print("5. Port Blair")
    print("6. Pondycherry")
    print("")


def get_choice():
    # Get destination choice
    while True:
        try:
            choice = int(input("Where would you like to go?[Enter a Number] "))
            if (choice < 1) or (choice > 3):
                print("Please select a choice between 1 and 3.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            return choice


def get_info(choice):
    
    if (choice == 1):
        return "London"

    elif (choice == 2):
        return "Paris"

    elif (choice == 3):
        return "New York"
    elif(choice==4):
        return "Chennai"
    elif (choice==5):
        return "Port Blair"
    elif (choice==6):
        return "Pondycherry"
