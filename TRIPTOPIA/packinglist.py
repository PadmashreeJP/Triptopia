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
    def printnode(self):
        c=self.head
        while c:
            print(c.data)
            c=c.getnextnode()
pl=packing_list()
pl.addnodel("Essentials and Clothing:")
pl.addnodel("\tShirts")
pl.addnodel("\tPants")
pl.addnodel("\tUnderwear")
pl.addnodel("\tShoes")
pl.addnodel("\tTowel")
pl.addnodel("\tPyjama")
pl.addnodel("\tT-shirts ")
pl.addnodel("\tSandals")
pl.addnodel("\tSunglasses")
pl.addnodel("\tLuggage label")
pl.addnodel("\tEarplugs")
pl.addnodel("\tLaundry bag")
pl.addnodel("\tEye mask")
pl.addnodel("\tTravel pillow")
pl.addnodel("Electronics:")
pl.addnodel("\tMobile phone")
pl.addnodel("\tCamera")
pl.addnodel("\tLaptop / tablet")
pl.addnodel("\tChargers")
pl.addnodel("\tExtension cords")
pl.addnodel("\tExtra memory cards")
pl.addnodel("\tSpare batteries")
pl.addnodel("\tTravel adaptor")
pl.addnodel("Hygiene:")
pl.addnodel("\tDeodorant")
pl.addnodel("\tToothbrush")
pl.addnodel("\tToothpaste")
pl.addnodel("\tMouthwash")
pl.addnodel("\tShower gel / Shampoo")
pl.addnodel("\tSunscreen")
pl.addnodel("\tHair gel / spray")
pl.addnodel("\tHairBrush")
pl.addnodel("\tHair-dryer")
pl.addnodel("\tGlasses")
pl.addnodel("\tContacts")
pl.addnodel("\tBandages")
pl.addnodel("\tRazor")
pl.addnodel("Documents:")
pl.addnodel("\tPassport")
pl.addnodel("\tVisa")
pl.addnodel("\tDriver's license")
pl.addnodel("\tPlane tickets")
pl.addnodel("\tTravel insurance documents")
pl.addnodel("\tMoney")
pl.addnodel("\tCredit card")


