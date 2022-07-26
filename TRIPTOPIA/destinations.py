def print_options():
    print("List of Destinations")
    print("--------------")
    print("1. London")
    print("2. Paris")
    print("3. New York")
def get_choice():
    while True:
        try:
            choice = int(input("Where would you like to go?[Enter a Number] "))
            if (choice < 1) or (choice > 3):
                print("Please select a choice between 1 and 3.")
                continue
        except ValueError:
            print("Only numerical values are valid.")
        else:
            return choice
def get_info(choice):
    if (choice == 1):
        return "London"
    elif (choice == 2):
        return "Paris"
    elif (choice == 3):
        return "New York"

