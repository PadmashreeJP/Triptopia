class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
place = Node("Pondicherry,India")
print(place.data)
p1= Node("Paradise Beach\n\ttimings")
p2= Node("Auroville\n\ttimings")
p3= Node("Rock Beach\n\ttimings")
p4= Node("Old Lighthouse\n\ttimings")
p5= Node("French War Memorial\n\ttimings")
p6= Node("Botanical Garden\n\ttimings")
p7= Node("The Promenade\n\ttimings")
p8= Node("Park Monument\n\ttimings")
p9= Node("Ousteri Lake\n\ttimings")
p10= Node("Chunnambar Boathouse\n\ttimings")
p11= Node("Statue Of Dupleix\n\ttimings")
p12= Node("ISKCON Pondicherry\n\ttimings")
p13= Node("Immaculate Conception Cathedral\n\ttimings")
p14= Node("Serenity Beach\n\ttimings")
p15= Node("Eglise de Notre Dame des Anges\n\ttimings")
place.add_child(p1)
place.add_child(p2)
place.add_child(p3)
place.add_child(p4)
place.add_child(p5)
place.add_child(p6)
place.add_child(p7)
place.add_child(p8)
place.add_child(p9)
place.add_child(p10)
place.add_child(p11)
place.add_child(p12)
place.add_child(p13)
place.add_child(p14)
place.add_child(p15)
for i in place.children:
    print (i.data)
