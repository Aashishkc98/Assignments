# Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”
from functools import reduce
def rev_str(str):
    return str[::-1]
print(rev_str("1234abcd"))

# Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def my_func(str):
    upper_count=0
    lower_count=0
    for char in str:
        if char.isupper():
            upper_count+=1
        else:
            lower_count+=1
    print("No of Upper case characters: ",upper_count)
    print("No of lower case characters: ",lower_count)

my_func("MamangPAitAy")


# Create a function that takes a list and returns a new list with unique elements of the first list.

def func(lst):
    a=set(lst)
    return list(a)


print(func([1,2,2,2,3,4,5,6]))

#  Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically

def myfunc():
    a=input("Enter a hyphen-seperated sentence: ").split("-")
    a=sorted(a)
    print("-".join(a))

myfunc()

#  Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def capitalized_word():
    a=input("Enter a sentence to be capitalized: ").upper()
    print(a)
capitalized_word()

# Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def sum_number():
    b=int(input("Enter a int number: "))
    c=int(input("Enter another int number: "))
    sum=b+c
    print(sum)
sum_number()

#  Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

def two_string():
    a=input("enter a word: ")
    b=input("enter another word: ")
    if len(a)==len(b):
        print(a)
        print(b)
    elif len(a)>len(b):
        print(a)
    else:
        print(b)
two_string()

#  Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def num():
    lst=[]
    for i in range(1,20):
        lst.append(i*i)
    print(tuple(lst))
num()

# Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
showNumbers(5)

# Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

def even_number():
    lst=[]
    for i in range(1,21):
        if i%2==0:
            lst.append(i)
    print(lst)
even_number()

# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions
a=list(map(lambda x:x**2, range(1,11)))
print(a)
b=list(filter(lambda x:x%2==0,a))
print(b)

# Write a function to compute 5/0 and use try/except to catch the exceptions

def compute():
    try:
        5/0
    except:
        print("Error")
compute()

# Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 
a=[1,2,3,4,5,6,7]
b=reduce(lambda x,y:10*x+y,a)
print(b)

# What would be the output for these codes:
# (i) def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

####### Answer: The output will be 2.

# ii) def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()
####### Answer: Will get Error saying F is nit defined.


