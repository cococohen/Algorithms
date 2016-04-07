class Animal():
	def __init__(self, name):
		self.name = name
		
	def say_something(self):
		print "I am - - -  " + self.name

class Dog(Animal):
	def say_something(self):
		print "I am " + self.name + ", and I can bark"
	
dog = Dog("chiwana")
dog.say_something()