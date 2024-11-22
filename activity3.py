#Write a program to create a class Parrot and perform the following tasks -
#  Create a class variable species 
# Create a __init__ method that has instance variables - name and age 
# Create instances of class Parrot, passing arguments as well 
# Print Class variable by accessing it
#  Print Instance variables as well

class Parrot:
    species="Bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Parrot("Blu",10)
p2=Parrot("Rio",12)

#Access the class variable
print("Blu is {}".format(p1.species))
print("Rio is {}".format(p2.species))

#Access the instance variables
print("{0} is {1} years old".format(p1.name,p1.age))
print("{0} is {1} years old".format(p2.name,p2.age))
        