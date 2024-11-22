#Write a program to create a class with name Student and perform the following tasks -
#  Create a class variable grade and name 
# Create a function to print a sentence
#  Create a function to print class variables grade and name 
# Create an object of class Student Call the two functions to execute them

class student:
    #class variables
    grade=10
    name="Tabassum"
    
    def wishes(self):
        print("Hi I am a Student")

    def intro(self):
        print("I am ",self.name)
        print("I study in grade ",self.grade)

st=student()
st.wishes()
st.intro()