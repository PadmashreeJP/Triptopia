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



