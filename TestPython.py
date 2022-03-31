class Car():
    def __init__(self, make, color):
        self.make = make
        self.color = color

    def display_msg(self):
        print("Car is {color} and is a {make}".format(color = self.color, make = self.make))

car1 = Car("Tesla", "white")
car1.display_msg()

car2 = Car("Honda", "blue")
car2.display_msg()

#Branch one
#Branch two
#Edits