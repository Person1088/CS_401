class Interface:
    def OutdoorMenu(self):
        print("welcome to outdoor")

    def IndoorMenu(self):
        print("Welcome to the indoor sports section! Please select a category to browse available products.")
        print("For Volleyball, enter 1.")
        print("For Table Tennis, enter 2.")
        #for table tennis implement a stock decrementation
        userInput = int(input("Enter your selection: "))
        if(userInput == 1):
            print("something")
            #generate Volleyball Objects and store them in an array
            #use rng and case switch of creation methods to decide which items
            #rng for whether or not its discounted Discount() defined in VolleyBall

    def Start(self):
        print("Welcome to Paradigm Sporting Goods! Please select a category to begin.")
        print("For outdoor sports, enter 1.")
        print("For indoor sports, enter 2.")
        userInput = int(input("Enter your selection: "))
        if(userInput == 1):
            self.OutdoorMenu()
        elif(userInput == 2):
            self.IndoorMenu()
        else:
            print("----------------")
            print("Invalid input, please try again")
            self.Start()
           
            
interface = Interface()
interface.Start()
        
   