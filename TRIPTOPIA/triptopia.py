import destinations
import paris
import newyork
import london
import cost
import packinglist
def main():
    print("Welcome to the Triptopia-Your Official Trip Planner\n")
    destinations.print_options()
    choice = destinations.get_choice()
    destination = destinations.get_info(choice)
    while True:
        try:
            print("How many days will you be staying in",destination,"?")
            global length_of_stay
            length_of_stay = int(input())
            if (length_of_stay < 0):
                print("Please enter a positive number of days.")
                continue
        except ValueError:
            print("Only numerical values are valid.")
        else:
            break
    itnry(destination, length_of_stay)
def itnry(destination, length_of_stay):
    print("Triptopia\n-----------------------------")
    print("\nHere's your itinerary for", length_of_stay,"days")
    get_plans(destination)
    print("Have a pleasant stay at", destination)
def get_plans(destination):
    while (destination=="London" and length_of_stay<=30):
        packinglist.pl.printnode()
        if length_of_stay==1:
            london.day1()
            print("cost = ",cost.n.item[0],"£")
            break
        elif length_of_stay==2:
            london.day2()
            print("cost = ",cost.n.item[1],"£")
            break
        elif length_of_stay==3:
            london.day3()
            print("cost = ",cost.n.item[2],"£")
            break
        elif length_of_stay==4:
            london.day4()
            print("cost = ",cost.n.item[3],"£")
            break
        elif length_of_stay==5:
            london.day5()
            print("cost = ",cost.n.item[4],"£")
            break
        elif length_of_stay==6:
            london.day6()
            print("cost = ",cost.n.item[5],"£")
            break
        elif length_of_stay==7:
            print(london.day7())
            print("cost = ",cost.n.item[6],"£")
            break
        elif length_of_stay==8:
            print(london.day8())
            print("cost = ",cost.n.item[7],"£")
            break
        elif length_of_stay==9:
            print(london.day9())
            print("cost = ",cost.n.item[8],"£")
            break
        elif length_of_stay==10:
            print(london.day10())
            print("cost = ",cost.n.item[9],"£")
            break
        elif length_of_stay==11:
            print(london.day11())
            print("cost = ",cost.n.item[10],"£")
            break
        elif length_of_stay==12:
            print(london.day12())
            print("cost = ",cost.n.item[11],"£")
            break
        elif length_of_stay==13:
            print(london.day13())
            print("cost = ",cost.n.item[12],"£")
            break
        elif length_of_stay==14:
            print(london.day14())
            print("cost = ",cost.n.item[13],"£")
            break
        elif length_of_stay==15:
            print(london.day15())
            print("cost = ",cost.n.item[14],"£")
            break
        elif length_of_stay==16:
            print(london.day16())
            print("cost = ",cost.n.item[15],"£")
            break
        elif length_of_stay==17:
            print(london.day17())
            print("cost = ",cost.n.item[16],"£")
            break
        elif length_of_stay==18:
            print(london.day18())
            print("cost = ",cost.n.item[17],"£")
            break
        elif length_of_stay==19:
            print(london.day19())
            print("cost = ",cost.n.item[18],"£")
            break
        elif length_of_stay==20:
            print(london.day20())
            print("cost = ",cost.n.item[19],"£")
            break
        elif length_of_stay==21:
            print(london.day21())
            print("cost = ",cost.n.item[20],"£")
            break
        elif length_of_stay==22:
            print(london.day22())
            print("cost = ",cost.n.item[21],"£")
            break
        elif length_of_stay==23:
            print(london.day23())
            print("cost = ",cost.n.item[22],"£")
            break
        elif length_of_stay==24:
            print(london.day24())
            print("cost = ",cost.n.item[23],"£")
            break
        elif length_of_stay==25:
            print(london.day25())
            print("cost = ",cost.n.item[24],"£")
            break
        elif length_of_stay==26:
            print(london.day26())
            print("cost = ",cost.n.item[25],"£")
            break
        elif length_of_stay==27:
            print(london.day27())
            print("cost = ",cost.n.item[26],"£")
            break
        elif length_of_stay==28:
            print(london.day28())
            print("cost = ",cost.n.item[27],"£")
            break
        elif length_of_stay==29:
            print(london.day29())
            print("cost = ",cost.n.item[28],"£")
            break
        elif length_of_stay==30:
            print(london.day30())
            print("cost = ",cost.n.item[29],"£")
            break
    while (destination=="Paris" and length_of_stay<=30):
        packinglist.pl.printnode()
        if length_of_stay==1:
            paris.day1()
            print("cost = ",cost.n.item[0],"$")
            break
        elif length_of_stay==2:
            paris.day2()
            print("cost = ",cost.n.item[1],"$")
            break
        elif length_of_stay==3:
            paris.day3()
            print("cost = ",cost.n.item[2],"$")
            break
        elif length_of_stay==4:
            paris.day4()
            print("cost = ",cost.n.item[3],"$")
            break
        elif length_of_stay==5:
            paris.day5()
            print("cost = ",cost.n.item[4],"$")
            break
        elif length_of_stay==6:
            paris.day6()
            print("cost = ",cost.n.item[5],"$")
            break
        elif length_of_stay==7:
            print(paris.day7())
            print("cost = ",cost.n.item[6],"$")
            break
        elif length_of_stay==8:
            print(paris.day8())
            print("cost = ",cost.n.item[7],"$")
            break
        elif length_of_stay==9:
            print(paris.day9())
            print("cost = ",cost.n.item[8],"$")
            break
        elif length_of_stay==10:
            print(paris.day10())
            print("cost = ",cost.n.item[9],"$")
            break
        elif length_of_stay==11:
            print(paris.day11())
            print("cost = ",cost.n.item[10],"$")
            break
        elif length_of_stay==12:
            print(paris.day12())
            print("cost = ",cost.n.item[11],"$")
            break
        elif length_of_stay==13:
            print(paris.day13())
            print("cost = ",cost.n.item[12],"$")
            break
        elif length_of_stay==14:
            print(paris.day14())
            print("cost = ",cost.n.item[13],"$")
            break
        elif length_of_stay==15:
            print(paris.day15())
            print("cost = ",cost.n.item[14],"$")
            break
        elif length_of_stay==16:
            print(paris.day16())
            print("cost = ",cost.n.item[15],"$")
            break
        elif length_of_stay==17:
            print(paris.day17())
            print("cost = ",cost.n.item[16],"$")
            break
        elif length_of_stay==18:
            print(paris.day18())
            print("cost = ",cost.n.item[17],"$")
            break
        elif length_of_stay==19:
            print(paris.day19())
            print("cost = ",cost.n.item[18],"$")
            break
        elif length_of_stay==20:
            print(paris.day20())
            print("cost = ",cost.n.item[19],"$")
            break
        elif length_of_stay==21:
            print(paris.day21())
            print("cost = ",cost.n.item[20],"$")
            break
        elif length_of_stay==22:
            print(paris.day22())
            print("cost = ",cost.n.item[21],"$")
            break
        elif length_of_stay==23:
            print(paris.day23())
            print("cost = ",cost.n.item[22],"$")
            break
        elif length_of_stay==24:
            print(paris.day24())
            print("cost = ",cost.n.item[23],"$")
            break
        elif length_of_stay==25:
            print(paris.day25())
            print("cost = ",cost.n.item[24],"$")
            break
        elif length_of_stay==26:
            print(paris.day26())
            print("cost = ",cost.n.item[25],"$")
            break
        elif length_of_stay==27:
            print(paris.day27())
            print("cost = ",cost.n.item[26],"$")
            break
        elif length_of_stay==28:
            print(paris.day28())
            print("cost = ",cost.n.item[27],"$")
            break
        elif length_of_stay==29:
            print(paris.day29())
            print("cost = ",cost.n.item[28],"$")
            break
        elif length_of_stay==30:
            print(paris.day30())
            print("cost = ",cost.n.item[29],"$")
            break
    while (destination=="New York" and length_of_stay<=30):
        packinglist.pl.printnode()
        if length_of_stay==1:
            newyork.day1()
            print("cost = ",cost.n.item[0],"$")
            break
        elif length_of_stay==2:
            newyork.day2()
            print("cost = ",cost.n.item[1],"$")
            break
        elif length_of_stay==3:
            newyork.day3()
            print("cost = ",cost.n.item[2],"$")
            break
        elif length_of_stay==4:
            newyork.day4()
            print("cost = ",cost.n.item[3],"$")
            break
        elif length_of_stay==5:
            newyork.day5()
            print("cost = ",cost.n.item[4],"$")
            break
        elif length_of_stay==6:
            newyork.day6()
            print("cost = ",cost.n.item[5],"$")
            break
        elif length_of_stay==7:
            print(newyork.day7())
            print("cost = ",cost.n.item[6],"$")
            break
        elif length_of_stay==8:
            print(newyork.day8())
            print("cost = ",cost.n.item[7],"$")
            break
        elif length_of_stay==9:
            print(newyork.day9())
            print("cost = ",cost.n.item[8],"$")
            break
        elif length_of_stay==10:
            print(newyork.day10())
            print("cost = ",cost.n.item[9],"$")
            break
        elif length_of_stay==11:
            print(newyork.day11())
            print("cost = ",cost.n.item[10],"$")
            break
        elif length_of_stay==12:
            print(newyork.day12())
            print("cost = ",cost.n.item[11],"$")
            break
        elif length_of_stay==13:
            print(newyork.day13())
            print("cost = ",cost.n.item[12],"$")
            break
        elif length_of_stay==14:
            print(newyork.day14())
            print("cost = ",cost.n.item[13],"$")
            break
        elif length_of_stay==15:
            print(newyork.day15())
            print("cost = ",cost.n.item[14],"$")
            break
        elif length_of_stay==16:
            print(newyork.day16())
            print("cost = ",cost.n.item[15],"$")
            break
        elif length_of_stay==17:
            print(newyork.day17())
            print("cost = ",cost.n.item[16],"$")
            break
        elif length_of_stay==18:
            print(newyork.day18())
            print("cost = ",cost.n.item[17],"$")
            break
        elif length_of_stay==19:
            print(newyork.day19())
            print("cost = ",cost.n.item[18],"$")
            break
        elif length_of_stay==20:
            print(newyork.day20())
            print("cost = ",cost.n.item[19],"$")
            break
        elif length_of_stay==21:
            print(newyork.day21())
            print("cost = ",cost.n.item[20],"$")
            break
        elif length_of_stay==22:
            print(newyork.day22())
            print("cost = ",cost.n.item[21],"$")
            break
        elif length_of_stay==23:
            print(newyork.day23())
            print("cost = ",cost.n.item[22],"$")
            break
        elif length_of_stay==24:
            print(newyork.day24())
            print("cost = ",cost.n.item[23],"$")
            break
        elif length_of_stay==25:
            print(newyork.day25())
            print("cost = ",cost.n.item[24],"$")
            break
        elif length_of_stay==26:
            print(newyork.day26())
            print("cost = ",cost.n.item[25],"$")
            break
        elif length_of_stay==27:
            print(newyork.day27())
            print("cost = ",cost.n.item[26],"$")
            break
        elif length_of_stay==28:
            print(newyork.day28())
            print("cost = ",cost.n.item[27],"$")
            break
        elif length_of_stay==29:
            print(newyork.day29())
            print("cost = ",cost.n.item[28],"$")
            break
        elif length_of_stay==30:
            print(newyork.day30())
            print("cost = ",cost.n.item[29],"$")
            break    
# Call main
main()
