import destinations
import paris1


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
    f.write("\nPacking list:\n"+str(packing_list))
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
      
    return "1"
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

class Node:
    def __init__(self,data,nextnode=None):
        self.data=data
        self.nextnode=nextnode
    def getdata(self):
        return self.data
    def setdata(self,data):
        self.data=data
    def getnextnode(self):
        return self.nextnode
    def setnextnode(self,val):
        self.nextnode=val
class packing_list:
    def __init__(self,head=None):
        self.head=head
        self.tail=None
        self.size=0
    def addnodeF(self,data):
        newnode=Node(data,self.head)
        self.head=newnode
        self.size+=1
        return True
    def addnodel(self,data):
        if self.head==None:
            newnode=Node(data,self.head)
            self.head=newnode
            self.size+=1
        else:
            c=self.head
            newnode=Node(data,self.tail)
            while(self.size>1 and c.getnextnode()!=None):
                c=c.getnextnode()
            c.setnextnode(newnode)
            self.size+=1
            return True
    def delnodeF(self):
        if self.head==None:
            print("empty list")
        else:
            pos=self.head
            print(" The deleted element is", pos.data)
            pos=pos.getnextnode()
    def delnodeL(self):
        if self.head==None:
            print("empty list")
        else:
            pos=self.head
            while pos.getnextnode().getnextnode()!=None:
                pos=pos.getnextnode()
            print(" The deleted element is",pos.nextnode.data)
            pos.nextnode=None
    def printnode(self):
        c=self.head
        while c:
            print(c.data)
            c=c.getnextnode()
            return(c.data)

    
# Call main
main()
pl=packing_list()
pl.addnodel("Essentials and Clothing:")
pl.addnodel("1.Underwear")
pl.addnodel("2.Socks")
pl.addnodel("3.Shirts")
pl.addnodel("4.Pants")
pl.addnodel("5.Caps")
pl.addnodel("6.Shoes")
pl.addnodel("7.Towel")
pl.addnodel("8.Pyjama")
pl.addnodel("9.Jacket")
pl.addnodel("10.T-shirts ")
pl.addnodel("11.Sandals")
pl.addnodel("12.Sunglasses")
pl.addnodel("13.Pocketknife")
pl.addnodel("14.Luggage label")
pl.addnodel("15.Luggage locks")
pl.addnodel("16.Earplugs")
pl.addnodel("17.Wallet")
pl.addnodel("18.Laundry bag")
pl.addnodel("19.Umbrella")
pl.addnodel("20.Eye mask")
pl.addnodel("21.Travel pillow")
pl.addnodel("Electronics:")
pl.addnodel("22.Mobile phone")
pl.addnodel("23.Camera")
pl.addnodel("24.Laptop / tablet")
pl.addnodel("25.USB-stick")
pl.addnodel("26.Chargers")
pl.addnodel("27.Extension cords")
pl.addnodel("28.Extra memory cards")
pl.addnodel("29.Spare batteries")
pl.addnodel("30.Travel adaptor")
pl.addnodel("Hygiene:")
pl.addnodel("31.Deodorant")
pl.addnodel("32.Toothbrush")
pl.addnodel("33.Toothpaste")
pl.addnodel("34.Mouthwash")
pl.addnodel("35.Floss")
pl.addnodel("36.Shower gel / Shampoo")
pl.addnodel("37.Sunscreen")
pl.addnodel("38.Hair gel / spray")
pl.addnodel("39.HairBrush")
pl.addnodel("40.Pain killers")
pl.addnodel("41.Pocket mirror")
pl.addnodel("42.Hair-dryer")
pl.addnodel("43.Glasses")
pl.addnodel("44.Contacts")
pl.addnodel("45.Bandages")
pl.addnodel("46.Razor")
pl.addnodel("47.Jewelry")
pl.addnodel("Documents:")
pl.addnodel("48.Passport")
pl.addnodel("49.Visa")
pl.addnodel("50.Driver's license")
pl.addnodel("51.Plane tickets")
pl.addnodel("52.Travel insurance documents")
pl.addnodel("53.Money")
pl.addnodel("54.Credit card")
pl.addnodel("55.Cheque Book")
pl.printnode()
