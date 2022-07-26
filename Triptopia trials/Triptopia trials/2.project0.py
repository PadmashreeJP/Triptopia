import destinations

def main():
    # Print a welcome message
    print("Welcome to the Trip Planner")

    # Show destinations
    destinations.print_options()

    # Pick destination
    choice = destinations.get_choice()

    # Get destination info
    destination = destinations.get_info(choice)

    # Determine length of stay
    while True:
        try:
            print("And how many days will you be staying in",destination,"?")
            length_of_stay = int(input())
            
            # Check for non-positive input
            if (length_of_stay < 0):
                print("Please enter a positive number of days.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    # Save itinerary
    #try:
    itt(destination, length_of_stay)
    # Catch file errors
    #except:
        
        #print("Error: the itinerary could not be saved.")

    # Print confirmation
    #else:
        #print("Your trip to", destination,"has been booked!")




def itt(destination, length_of_stay):
    f=open("itn.txt","w+")
    f=open("itn.txt","a+")
    f.write("Trip Itinerary")
    f.write("\n--------------\n")
    f.write("\nDestination: " +str(destination))
    f.write("\nLength of stay:" +str(length_of_stay))
    f.write("Plans",get_plans())
    f.close()
    f=open("itn.txt", "r")
    if f.mode == 'r':
         contents =f.read()
         print (contents)
    fl =f.readlines()
    for x in fl:
        print (x)
def get_plans():
        while destination=="London":
            print("lon")
        while destination=="Paris":
            pass
        while destination=="New York":
            pass
        while destination=="Chennai":
            pass
        while destination=="Port Blair":
            pass
        while destination=="Pondycherry":
            pass
# Call main
main()
