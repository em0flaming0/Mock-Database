#!/usr/bin/python

#demonstrating basic use of classes and inheritance 

class Automobile(object):
	def __init__(self, wheels):
		self.wheels = wheels  #all autmobiles have wheels

class Car(Automobile):
	def __init__(self, make, model, year, color):
		Automobile.__init__(self, "4")  #all Car objects should have 4 wheels
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.owner = None  #an optional attribute for Car objects
		self.engine = "N/A"  #default engine_type for all instances of Car

class Bike(Automobile):
	def __init__(self, make, model, year, color):
		Automobile.__init__(self, "2")  #all Bike objects should have 2 wheels
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.owner = None

def main():
	Car1 = Car("Ford", "Mustang", "2001", "Red")
	Bike1 = Bike("Kawasaki", "Ninja-ZX", "2005", "Green")
	Car2 = Car("Honda", "S2000","2009","Silver")
	
	Bike1.owner = "Mary Thompson"
	Car1.owner = "Mike Smith"
	Car1.engine = "Supercharged"
	Car2.owner = "Robert Johnson"

if __name__ == "__main__":
	main()
