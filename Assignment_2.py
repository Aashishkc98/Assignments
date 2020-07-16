# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
if num%3==0:
    print("Consultadd")

# If a number is divisible by 5 it should print “c” as a string
if number%5==0:
     print("C")

# If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.
if numbers%3==0 and numbers%5==0:
    print("Consultadd Python Training")

# Ask the user to choose the following option first:
# If User Enter 1 - Addition  # If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average
x=int(input("Enter Number: "))
y=int(input("Enter Number: "))
print("Which Operater to use?")
z=input("Enter 1 for addition, 2 for subtraction, 3 for division, 4 for Multiplication, 5 for Average:  ")
result=0
if z=='1':
    result=x+y
    print("The sum of {} and {} is:{}".format(x,y,result))
elif z=='2':
    result=x-y
    print("The differnece between {} and {} is:{}".format(x,y,result))
elif z=='3':
    result=x*y
    print("Multiplication between {} and {} is:{}".format(x,y,result))
elif z=="4":
    result=x/y
    print("Division between {} and {} is:{}".format(x,y,result))
elif z=='5':
    result=x+y/2
    print("The Average of {} and {} is:{}".format(x,y,result))
else:
    print("Not Recognized")
if result<0:
    print("Zsa")


age=38
if age>=11:
    print("You are eligible to see football match")
else:
    print("You're not eligible to buy a ticket")
if age<=20 or age>=60:
    print("Ticket price $12.")
else:
    print("Ticket price is $20")

# If a user enters a negative number just break the loop and print “It’s Over”
# If a user enters a positive number just continue in the loop and print “Good Going”

while True:
    var1=int(input("Enter Number: "))
    if var1<0:
        print("It's Over") 
        break
    else:
        print("Good Going")
        continue


# Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
for num in range(2000,3200):
    if num%7==0 and num%5!=0:
        print(num)

# Write a program that prints all the numbers from 0 to 6 except 3 and 6.
    
# Expected output: 0 1 2 4 5
# Note: Use the ‘continue’ statement
for num in range(7):
    if num==3:
        continue
    elif num==6:
        continue
    print(num)

# Write a program that accepts a string as an input from the user and calculates the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2
word=input("Enter a string: ")
d=l=0
for c in word:
    if c.isalpha():
        l+=1
    elif c.isdigit():
        d+=1
print("letter", l)
print("digit", d)

