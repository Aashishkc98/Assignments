#Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
x=[1,"Ashish",4.34,3+3j]

#Create a list of size 5 and execute the slicing structure 
x=[1,2,3,4,5]
x[:]
x[:5]
x[1:]
x[1:2:2]

#Write a program to get the sum and multiply of all the items in a given list.
my_list=[1,2,3,4,5]
print(sum(my_list))

multiplier=1
for i in my_list:
    multiplier*=i
print(multiplier)

#Find the largest and smallest number from a given list.
num=[1,2,34,5,6,7,89,10]
max(num)
min(num)

#Create a new list that contains the specified numbers after removing the even numbers from a predefined list. 

old_list=[1,2,3,4,5,6,7]
new_list=[]
for i in old_list:
    if i%2==0:
        new_list.append(i)

print(new_list)

#Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)
lst=[]
for i in range(1,31):
    lst.append(i**2)

print(lst[:5])
print(lst[-5:])

# Write a program to replace the last element in a list with another list.
# Sample data: [1,3,5,7,9,10,[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]
sam=[1,3,5,7,9,10]
a=[2,4,6,8]
sam[-1:]=a
print(sam)

# Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

# Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}
my_dict={}
n=5
for i in range(1,6):
    my_dict[i]=i*i
print(my_dict)

# Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)
# values=input("enter any comma seperated numbers: ")
# lsts=values.split(",")
# tup=tuple(lsts)
# print(lsts)
# print(tup)

# Create a list of given structure and run 
y=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
# Access list [600,  700]
# Access list [100, 300, 500, 600, 800]
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list [10]
# Access list [ ]

print(y[5][:4])
print(y[6:8])
print(y[::2])
print(y[::-1])
print(y[5][5][0])
print(y)

#Create a list of thousand numbers using range and xrange and see the difference between each other.
# Creating a list of 1000 numbers using range will create a list of 1000 integers in memory and all those numbers are generated at once. On the other hand, xrange() generates the numbers on demand, producing one number at a time as the for loop iteration moves to the next number.

#How Tuple is beneficial as compared to the list?
# Tuple is beneficial as compared to list in terms of memory efficiency. Since tuples are immutable, they are fixed sized and thus are allocated a single block of memory as they do not require extra space in the memory. Lists, on the other hand, are mutable and thus require extra space in the memory for any changes and are allocated two blocks of memory. This is also why tuples are faster than lists in terms of operation.

#Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
for i in range(1,100):
    if (i%3==0) and (i%2==0):
        print(i)

#Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.
#Write a program in Python to iterate through the string “hello my name is Abcde” and print the string which has even length of the word.
var="Hello my name is abcde"
for i in var.split():
    if len(i)%2==0:
        print(i)

x=[1,2,3,4,5,6,7]
for i in x:
    print(i*5)
