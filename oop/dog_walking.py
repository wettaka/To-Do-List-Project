#To define a class, in typical simple Python fashion, 
#we use the word ‘class,’ followed by the name of your new class. 
#I’m going to make a new class here, called ‘pet’. 
#We use a colon after the name, and then anything contained 
#within the class definition is indented. However, 
#with a class, there are no parentheses:
class pet:
    def walk(self):
        print("Tom is walking!")

class dog(pet):
    def walk(self):
        print("Tom is walking!") 
        print("Fletcher is walking!")  
        print("Larry is walking!")     
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
#If we’re accessing the number_of_legs variable, it’s going to look like this:
doug.walk()  