from indoor import Indoor
import random
#volleyball traits
#creation method for each type of item to control the parameters of their traits
#inventory creation using case switch of all those methods
class VolleyBall(Indoor):
    def __init__(self, name, price, type, size, brand, material, stock):
        self.name = name
        self.price = price
        self.type = type
        self.size = size
        self.brand = brand
        self.material = material
        self.stock = stock

    #Creation functions for balls and nets
    def CreateVolleyBall(self):
        randomSize = random.randint(1,3)
        randomMaterial = random.randint(1,2)
        randomBrand = random.randint(1,3)
        self.SetName("Volleyball")
        #Size brand and price
        if((randomSize == 1) and (randomBrand == 1)):
            self.SetSize("Youth")
            self.SetBrand("Wilson")
            self.SetPrice(14.99)
        if((randomSize == 1) and (randomBrand == 2)):
            self.SetSize("Youth")
            self.SetBrand("Molten")
            self.SetPrice(17.99)
        if((randomSize == 1) and (randomBrand == 3)):
            self.SetSize("Youth")
            self.SetBrand("Tachikara")
            self.SetPrice(20.99)
        if((randomSize == 2) and (randomBrand == 1)):
            self.SetSize("Womens")
            self.SetBrand("Wilson")
            self.SetPrice(20.99)
        if((randomSize == 2) and (randomBrand == 2)):
            self.SetSize("Womens")
            self.SetBrand("Molten")
            self.SetPrice(23.99)
        if((randomSize == 2) and (randomBrand == 3)):
            self.SetSize("Womens")
            self.SetBrand("Tachikara")
            self.SetPrice(26.99)
        if((randomSize == 3) and (randomBrand == 1)):
            self.SetSize("Mens")
            self.SetBrand("Wilson")
            self.SetPrice(24.99)
        if((randomSize == 3) and (randomBrand == 2)):
            self.SetSize("Mens")
            self.SetBrand("Molten")
            self.SetPrice(27.99)
        if((randomSize == 3) and (randomBrand == 3)):
            self.SetSize("Mens")
            self.SetBrand("Tachikara")
            self.SetPrice(30.99)
        #Material
        if(randomMaterial == 1):
            self.SetMaterial("Synthetic Leather")
        if(randomMaterial == 2):
            self.SetMaterial("Leather")
        
    #def CreateNet()


    #Display functions for Volleyballs and nets
    def DisplayVolleyBall(self):
        self.GetName()
        self.GetPrice()
        self.GetSize()
        self.GetBrand()
        self.GetMaterial()
        self.GetStock()

    #def Discount()