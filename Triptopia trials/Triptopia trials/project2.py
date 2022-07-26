import destinations
import paris1
import London1
def main():
    print("Welcome to the Trip Planner\n")
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
    f=open("itinerary.txt","w+")
    f=open("itinerary.txt","a+")
    f.write("Trip Itinerary")
    f.write("\n--------------\n")
    f.write("\nDestination: " +str(destination))
    f.write("\nLength of stay:" +str(length_of_stay))
    f.write("\nPlans:\n"+str(get_plans(destination)))
    f.close()
    f=open("itinerary.txt","r")
    if f.mode=='r':
        contents=f.read()
        print(contents)
    f1=f.readlines()
    for x in f1:
        print(x)
    

def get_plans(destination):
  while destination=="London":
        if length_of_stay==1:
            print(London1.day1())
            break

        elif length_of_stay==2:
            print(London1.day2())
            break
        elif length_of_stay==3:
            print(London1.day3())
            break
        elif length_of_stay==4:
            print(London1.day4())
            break
        elif length_of_stay==5:
            print(London1.day5())
            break
            
        elif length_of_stay==6:
            print(London1.day6())
            break
        elif length_of_stay==7:
            print(London1.day7())
            break
        elif length_of_stay==8:
            print(London1.day8())
            break
        elif length_of_stay==9:
            print(London1.day9())
            break
        elif length_of_stay==10:
            print(London1.day10())
            break
        elif length_of_stay==11:
            print(London1.day11())
            break
        elif length_of_stay==12:
            print(London1.day12())
            break
        elif length_of_stay==13:
            print(London1.day13())
            break
        elif length_of_stay==14:
            print(London1.day14())
            break
        elif length_of_stay==15:
            print(London1.day15())
            break
        elif length_of_stay==16:
            print(London1.day16())
            break
        elif length_of_stay==17:
            print(London1.day17())
            break
        elif length_of_stay==18:
            print(London1.day18())
            break
        elif length_of_stay==19:
            print(London1.day19())
            break
        elif length_of_stay==20:
            print(London1.day20())
            break
        elif length_of_stay==21:
            print(London1.day21())
            break
        elif length_of_stay==22:
            print(London1.day22())
            break
        elif length_of_stay==23:
            print(London1.day23())
            break
        elif length_of_stay==24:
            print(London1.day24())
            break
        elif length_of_stay==25:
            print(London1.day25())
            break
        elif length_of_stay==26:
            print(London1.day26())
            break
        elif length_of_stay==27:
            print(London1.day27())
            break
        elif length_of_stay==28:
            print(London1.day28())
            break
        elif length_of_stay==29:
            print(London1.day29())
            break
        elif length_of_stay==30:
            print(London1.day30())
            break

      
    

  while destination=="Paris":
        if length_of_stay==1:
            return "10:00am-10:30am : Place de la Bastille\n11:00am-12:30pm : Coulee Verte Rene-Dumont\n01:00pm-03:30pm : Lac des Minimes\n04:00pm-06:00pm : La Tour Eiffel"
        elif length_of_stay==2:
            return "Day 1:\n10:00am-10:30am : Place de la Bastille\n11:00am-12:30pm : Coulee Verte Rene-Dumont\n01:00pm-03:30pm : Lac des Minimes\n04:00pm-06:00pm : La Tour Eiffel\n\nDay 2:\n10:00am-01:30pm : Musee d'Orsay\n02:00pm-06:00pm : Louvre Musee"
        elif length_of_stay==3:
            return "Day 1:\n10:00am-10:30am : Place de la Bastille\n11:00am-12:30pm : Coulee Verte Rene-Dumont\n01:00pm-03:30pm : Lac des Minimes\n04:00pm-06:00pm : La Tour Eiffel\n\nDay 2:\n10:00am-01:30pm : Musee d'Orsay\n02:00pm-06:00pm : Louvre Musee\nDay 3:\n10:00am-12:30pm : Le Marais\n01:00pm-03:00pm : Canal Saint Martin\n03:30pm-05:00pm : 2nd Arrondissement\n05:30pm-06:00pm : Les Drapeaux de France"
        elif length_of_stay==4:
            return "Day 1:\n10:00am-10:30am : Place de la Bastille\n11:00am-12:30pm : Coulee Verte Rene-Dumont\n01:00pm-03:30pm : Lac des Minimes\n04:00pm-06:00pm : La Tour Eiffel\n\nDay 2:\n10:00am-01:30pm : Musee d'Orsay\n02:00pm-06:00pm : Louvre Musee\nDay 3:\n10:00am-12:30pm : Le Marais\n01:00pm-03:00pm : Canal Saint Martin\n03:30pm-05:00pm : 2nd Arrondissement\n05:30pm-06:00pm : Les Drapeaux de France\nDay 4:\n10:00am-12:00pm : Chateau de Chamrande\n01:00pm-02:30pm : La Maison Picassiette\n03:00pm-04:30pm : Eglise St-Aignan"
        elif length_of_stay==5:
            return "Day 1:\n10:00am-10:30am : Place de la Bastille\n11:00am-12:30pm : Coulee Verte Rene-Dumont\n01:00pm-03:30pm : Lac des Minimes\n04:00pm-06:00pm : La Tour Eiffel\n\nDay 2:\n10:00am-01:30pm : Musee d'Orsay\n02:00pm-06:00pm : Louvre Musee\nDay 3:\n10:00am-12:30pm : Le Marais\n01:00pm-03:00pm : Canal Saint Martin\n03:30pm-05:00pm : 2nd Arrondissement\n05:30pm-06:00pm : Les Drapeaux de France\nDay 4:\n10:00am-12:00pm : Chateau de Chamrande\n01:00pm-02:30pm : La Maison Picassiette\n03:00pm-04:30pm : Eglise St-Aignan\nDay 5:\n10:30am-05:30pm : Palais de Versailles"
        
        elif length_of_stay==6:
            print(paris1.day6())
            break
        elif length_of_stay==7:
            print(paris1.day7())
            break
        elif length_of_stay==8:
            print(paris1.day8())
            break
        elif length_of_stay==9:
            print(paris1.day9())
            break
        elif length_of_stay==10:
            print(paris1.day10())
            break
        elif length_of_stay==11:
            print(paris1.day11())
            break
        elif length_of_stay==12:
            print(paris1.day12())
            break
        elif length_of_stay==13:
            print(paris1.day13())
            break
        elif length_of_stay==14:
            print(paris1.day14())
            break
        elif length_of_stay==15:
            print(paris1.day15())
            break
        elif length_of_stay==16:
            print(paris1.day16())
            break
        elif length_of_stay==17:
            print(paris1.day17())
            break
        elif length_of_stay==18:
            print(paris1.day18())
            break
        elif length_of_stay==19:
            print(paris1.day19())
            break
        elif length_of_stay==20:
            print(paris1.day20())
            break
        elif length_of_stay==21:
            print(paris1.day21())
            break
        elif length_of_stay==22:
            print(paris1.day22())
            break
        elif length_of_stay==23:
            print(paris1.day23())
            break
        elif length_of_stay==24:
            print(paris1.day24())
            break
        elif length_of_stay==25:
            print(paris1.day25())
            break
        elif length_of_stay==26:
            print(paris1.day26())
            break
        elif length_of_stay==27:
            print(paris1.day27())
            break
        elif length_of_stay==28:
            print(paris1.day28())
            break
        elif length_of_stay==29:
            print(paris1.day29())
            break
        elif length_of_stay==30:
            print(paris1.day30())
            break
            
                  
  while destination=="New York":
    if length_of_stay==1:
        return "Statue of Liberty\nCentral park\nEmpire state building\nTimes square\nTrade center\n9/11 Memorial\n"
    elif length_of_stay==2:
        return "Statue of Liberty\nCentral park\nEmpire state building\nTimes square\nTrade center\n9/11 Memorial\nCentral park\nRockefeller center\nThe metropolitan museum of art\nBrooklyn bridge\n"
    break
  while destination=="Chennai":
    return "4"
    break
  while destination=="Port Blair":
    return "cellular jail "
    break
  while destination=="Pondycherry":
    return "Paradise Beach"
    break

    
# Call main
main()

