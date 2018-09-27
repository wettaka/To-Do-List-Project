#created a class called pet and defined some variables 
#within the class
class pet:
    number_of_dogs = 0
    years_of_tom = 0
    years_of_fletcher = 0
    years_of_larry = 0
    category_of_all = 0

class dog():
	#created a method called eat with an argument self btn the parenthesis.
    def eat(self):
        print("My dogs are not hungry.")  
#Instances and member variables
doug = dog()
#Now that we have an instance of a class, how do we access 
#and manipulate its properties? To reference a property of 
#an object, first we have to tell Python which object 
#(or which instance of a class) we’re talking about, 
#so we’re going to start with ‘doug’. 
#Then, we’re going to write a period to indicate that 
#we’re referencing something that’s contained within our 
#doug instance. After the period, we add the name of our variable. 
#it’s going to look like this:
doug.eat()          
dog = pet()
tom = pet()
fletcher = pet()
larry = pet()
mammals = pet()
category = pet()
dog.number_of_dogs = 3
tom.years_of_tom = 6
fletcher.years_of_fletcher = 7
larry.years_of_larry = 9
category.category_of_all = "mammals"


print ("I have %s dogs." % dog.number_of_dogs)
print ("Tom is %s ." % tom.years_of_tom)
print ("Fletcher is %s ." % fletcher.years_of_fletcher)
print ("Lary is %s ." % larry.years_of_larry)
print ("And they're all %s  ." % category.category_of_all)


