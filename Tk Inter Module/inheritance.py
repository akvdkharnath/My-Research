class Animal:
    # properties
	multicellular = True
	# Eukaryotic means Cells with Nucleus
	eukaryotic = True
	
	# functions
	def breath():
            
	def feed():
            
class Mammal(Animal):
	# properties
	haveMammaryGland = True
	def warmBlood = True
	
	# functions
	def produceMilk():
class Amphibian(Animal):
	# properties
	liveInWater = True
	
	# functions
	def metamorphosis():

Amphibian Frog = Amphibian()
Frog.breath()   # calling function defined in Animal class
Frog.metamorphosis()    # calling function defined in Amphibian class
print (Frog.liveInWater)
