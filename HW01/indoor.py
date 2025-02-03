#indoor will just have price for inheritance to table tennis and volleyball
#method that generates a bunch of volleyball and table tennis items and stores them in arrays
#getters and setters for volleyball and table tennis in here
class Indoor:
    #Getters
    def GetPrice(self):
        print(self.price)
    def GetName(self):
        print(self.name)
    def GetMaterial(self):
        print(self.material)
    def GetSize(self):
        print(self.size)
    def GetType(self):
        print(self.type)
    def GetStock(self):
        print(self.stock)
    def GetBrand(self):
        print(self.brand)
    

    #Setters
    def SetPrice(self,newPrice):
        self.price = newPrice
    def SetName(self,newName):
        self.name = newName
    def SetMaterial(self, newMaterial):
        self.material = newMaterial
    def SetSize(self, newSize):
        self.size = newSize
    def SetType(self, newType):
        self.type = newType
    def SetStock(self, newStock):
        self.stock = newStock
    def SetBrand(self, newBrand):
        self.brand = newBrand
    