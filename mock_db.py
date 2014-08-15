#!/usr/bin/python

class Automobile(object):
	def __init__(self, wheels):
		self.wheels = wheels

class Car(Automobile):
	def __init__(self, make, model, year, color):
		Automobile.__init__(self, "4")
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.owner = None
		self.engine = "N/A"

class Bike(object):
	def __init__(self, make, model, year, color):	
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.owner = None
		wheels = 2

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
