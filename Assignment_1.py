#TASK ONE: NUMBERS AND VARIABLES
#Create three variables in a single line and assign different values to them and make sure their data types are different. Like one is int, another one is float and the last one is a string.
x,y,z = 2,24.3,"Ashish"
print(x,y,z)

#Create a variable of value type complex and swap it with another variable whose value is an integer.
a= 5+3j
b=2
a,b=b,a
print(a,b)

#Swap two numbers using the third variable as the result name and do the same task without using any third variable.
var1=5
var2=2
temp=var1
var1=var2
var2=temp
print(x,y)

#Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
print("Hello world") #for python3
#print"hello world" #for python2

#Write a program to complete the task given below:
#Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
#Use z for adding 30 into it and print the final result by using variable results.
user_input=int(input("enter a number between 1-10: "))
user_input_again=int(input("enter a number between 1-10: "))
z=user_input+user_input_again
results=z+30
print(results)

#Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc
output=eval(input("enter anything: "))
print("The input value dataType is: ",type(output))

#If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?
#Answer: Yes, the value will change because python has dynamic memory allocation.

