# Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.

a=list(filter(lambda x:x%3!=0 and x%7==0, range(1,10)))
print(a)

# Write a program in Python to  multiple the element of list by itself using a traditional function and pass the function to map to complete the operation.

def multiply(lst):
    return lst*lst
b=[1,2,3,4,5]
c=list(map(multiply,b))
print(c)

# Write a program to Python find out the character in a string which is uppercase using list comprehension.
x=input("Enter a word: ")
upper_letters=[i for i in x if i.isupper()]
print(upper_letters)

# Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
my_dict={k:v for(k,v) in zip(Student,capital)}
print(my_dict)

# Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
def rev_string(string):
    for i in range(len(string) -1,-1,-1):
        yield string[i]
a=rev_string("Consultadd Trainig")
print(next(a))

# Write any example on decorators.
def my_decorator(func):
    def inner():
        before=func()
        after=before.capitalize()
        return after
        return inner
@my_decorator
def string():
    return input("enter a string: ")
    a=string()
print(a)

#  	Learn about What is FRONT END and its Technologies and Tools
# Make sure to mention at least 5 top notch technologies of Frontend.
# Also mentioned the name of companies using those 5 technologies individually

#### Answer:::Front end technologies are those technologies used in the development of the user 
# interface of web applications and web pages. Using these front-end tools and technologies,
#  developers create the design, structure, behavior and everything the user sees on the screen 
#  while opening a web page or a web application. Below are five of the top notch frontend technologies
#   and the name of the companies that are using them;
# •	Angular  JS – Netflix,JetBlue
# •	React JS – Facebook,Instagram, Ubereats
# •	Vue.js – Nintendo
# •	Bootstrap – Spotify,Twitter,Lyft
# •	Saas – Pandora,Hubspot

