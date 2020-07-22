from sys import argv

# Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError
try:
    eval("x!!=x")
except SyntaxError:
     print("Fix the syntax of your operation")

# Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode. 

module_name,file_name= argv
print("You are currently in ",module_name)
print("The file you are opening is ",file_name)
while True:
    try:
        f=open(file_name,'r')
        content= f.read()
        print(content)
        f.close()
        break
    except:
        print("No file of such name exists.")
        try_again= input("Do you want to try again? Press Y for yes and N for no: ").upper()
        if try_again=='Y':
            file_name=input("Please enter the correct file name: ")
        else:
            break

# Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits” 
while True:
    try:
        user_input= input("Please enter four numbers: ")
        if len(user_input)>4 or len(user_input)<4:
            raise error
    except:
       print("The length is too short/long.Please provide only four numbers")

# Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
print("Welcome! Please provide your username and password to enter")
username= input("Please enter your username: ")
password = input("Please type your password: ")
password2= input("Please retype the password: ")
count=0
while count<3:
    if password==password2:
        print("{},You are in!".format(username))
        break
    else:
        retype=input("Incorrect password. Please provide the password again: ")
        count+=1

# Read any file using Python File handling concept and return only the even length string from the doc.txt file.
# Consider the content as: 
# 	Hello I am a file 
# 	Where you need to return the data string 
# 	Which is of even length 
# 	Make sure you return the content in 
# 	The same link as it is present.
with open('doc.txt','r') as f:
 	   content=f.read()
  	   for char in content.split():
  if len(char)%2==0:
       		     print(char)
