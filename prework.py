
# QUESTIONS:
# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
def sayHello(user_name):
    return f"hello{user_name}!"
sayHello("doodoobrain")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds(): 

 
alist = [1-100] #all numbers 1 to 100

def first_odds(alist):
    for i in alist:
        if i%2 != 0 and i<=100:
            print(i)
first_odds(alist)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 

alist =[1,2,3,8,100]
def max_num_in_list(alist):
    return max(alist)
print(max_num_in_list(alist))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
# ..... 
def leap_year(year):
    if year %4 == 0 and year %100 == 0 and year %400 == 0:
        return True
    if year %4 == 0 and year %100 != 0:
        return True
    else:
        return False



# Question 5

# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
alist =[1,2,3,5,6]
def consList():
    firstnum = alist[0]
    nextnum= 0
    if alist[1] == firstnum+1:
        nextnum.append(alist[1])
    for num in alist:
        if num == (nextnum + 1):
            return True
        else:
            return False
consList(alist)