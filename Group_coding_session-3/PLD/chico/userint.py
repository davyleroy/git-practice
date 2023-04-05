collection = []


class House:
    
    def __init__ (self, rooms, owner, contact, location, rent, sale, price):
        self.rooms = rooms
        self.owner = owner
        self.contact = contact
        self.location = location
        self.rent = rent
        self.sale = sale
        self.price = price
        collection.append(f'{rooms} rooms house at {location} price is {price}')
        
    def __str__(self):
        return (f"the house at {self.location} has {self.rooms} rooms, the price is {self.price} the owner contact is {self.contact}")
    

def owners(rooms, owner, contact, location, rent, sale, price):
    global house5
    house5 = House(rooms, owner, contact, location, rent, sale, price)
    return house5
    
    
owners(2, 'pro', 4546634, 'kicukiro', False, True, 50000)
owners(2, 'pro', 4546634, 'kicukiro', True, False, 50000)
owners(2, 'pro', 4546634, 'gasabo', False, True, 50000)
owners(2, 'pro', 4546634, 'gasabo', True, False, 50000)
owners(2, 'pro', 4546634, 'nyarugenge', False, True, 50000)
owners(2, 'pro', 4546634, 'nyarugenge', True, False, 50000)

print(house5.location)

yish = True

name = input("name: ")
password = input("password: ")

print(f"Welcome {name}")



while yish:

    print("choose your category")
    
    print("(1). Owner")
    print("(2). client")
    
    
    choice = int(input("choose between 1 (owner) or 2(client): "))
    
    if choice == 1:
        print("Welcome owner\n")
        
        print("do you want to Add house or see your houses? ")
        print("(1). Add")
        print("(2). see your houses")
        print("(3). Log out")
        
        chico = True
        
        while chico:
            choice1 = int(input("choose 1 (Add) or 2 (See houses), 3 (Loguot): "))
            
            if choice1 == 1:
                print("you are going to add")
                
                rooms = input("number of rooms: ")
                owner = input("name: ")
                contact = input("contact: ")
                location = input("location: ")
                rent = input("is it for rent: ")
                sale = input("is it for savle: ")
                price = input("number of rooms: ")
                
                owners(rooms, owner, contact, location, rent, sale, price)
                
                print("house added")
                print(house5)
                
                chico = True
                            
            elif choice1 == 2:
                
                for element in collection:
                    print(element)
            
                chico = True
            
            else:
                print("\nlogged out|n")
                
                chico = False
                
                
        
            
            
    elif choice == 2:
        print("welcome!")
        print("\nAre you buying or renting?")
        
        print("(1). buying")
        print("(2). renting")
        
        chico1 = True
        
        while chico1:
            choice2 = input("choose 1 (buying) or 2(renting): ")
         
        
            
            if choice2 == 1:
                    
                print("Choose location")
                
                print("(1). kicukiro")
                print("(2). gasabo")
                print("(3). nyarugenge")
                print("(4). log out")
                
                choice3 = input("choose: ")
                
                if choice3 == 1:
                    print(collection[1])
                    
                    
                    chico1 = True
                        
                        
                            
                elif choice3 == 2:
                    pass
                    
                elif choice3 == 3:
                    pass
                    
                else:
                    print("Logged out")
                        
                    chico1 = False
                
            if choice2 == 2:
                print("Choose location")
                    
                print("(1). kicukiro")
                print("(2). gasabo")
                print("(3). nyarugenge")
                pass
                    