from indoor import Indoor
#volleyball traits
#creation method for each type of item to control the parameters of their traits
#inventory creation using case switch of all those methods
class VolleyBall(Indoor):
    def __init__(self,name,price,size, material):
        self.name = name
        self.price = price
        self.size = size
        self.material = material

#example creator
def CreateVolleyBall(self):
    #self.setPrice
    #self.setSize
    #self.setName
    #self.setMaterial