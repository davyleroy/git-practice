class House:
    
    def __init__ (self, rooms, owner, contact, location, rent, sale, price):
        self.rooms = rooms
        self.owner = owner
        self.contact = contact
        self.location = location
        self.rent = rent
        self.sale = sale
        self.price = price
        
    def __str__(self):
        return (f"the house at {self.location} has {self.rooms} rooms, the price is {self.price} the owner contact is {self.contact}")
    

def owners(rooms, owner, contact, location, rent, sale, price):
    global house5
    house5 = House(rooms, owner, contact, location, rent, sale, price)
    return house5
    
    
owners(2, 'pro', 4546634, 'kicukiro', False, True, 50000)

print(house5.location)