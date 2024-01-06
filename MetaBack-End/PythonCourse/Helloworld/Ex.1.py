class House:
     
     numRooms = 5
     bathrRooms = 2

     def costEv(self):
          print(self.numRooms)
          pass

house = House()

house.bathrRooms = 7
print(house.bathrRooms)
print(House.bathrRooms)

House.bathrRooms = 5
print(house.bathrRooms)
print(House.bathrRooms)

