#Write a program to create a class Parrot and perform the following tasks - 
# Create a class variable species 
# Create a constructor that has instance variables - name and age 
# Create instance methods for this class named sing and dance, making them print a message.
#  Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

class Parrot:
   
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return "{0} sings {1}".format(self.name,song)
    
    def dance(self):
        return "{} likes to dance ".format(self.name)
    
p1=Parrot("Blu",10)
p2=Parrot("Rio",12)

print(p1.sing("'Happy'"))
print(p1.dance())

print(p2.sing("'Party'"))
print(p2.dance())

 
        