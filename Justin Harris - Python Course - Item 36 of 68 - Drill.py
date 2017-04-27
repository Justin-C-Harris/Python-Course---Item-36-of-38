# Python:   2.7.13
#
# Author:   Justin C. Harris
#
# Purpose:  To complete the drill in Item 36 of 68 in the Python course at The Tech Academy

#1, 2, and 3 Assign an integer, string, and float variable
#4 Use the print function and .format() notation to print out the variables you assigned
def func1():
    vInt = 5 # assign an integer to a variable
    vStr = "String" # assign a string to a variable
    vFloat = 4.25 # assign a float to a variable
    print("My integer is: {}\nMy string is: {}\nMy float is: {}".format(vInt,vStr,vFloat)) # print out my variables and use the .format() notation

#5 Use each of these operators +,-,*,/,+=,=,%
def func2():
    vInt1 = 10
    vInt2 = 5
    vInt3 = 10
    vInt3 += vInt2
    print("\n{} + {} = {}".format(vInt1,vInt2,vInt1+vInt2))
    print("{} - {} = {}".format(vInt1,vInt2,vInt1-vInt2))
    print("{} * {} = {}".format(vInt1,vInt2,vInt1*vInt2))
    print("{} / {} = {}".format(vInt1,vInt2,vInt1/vInt2))
    print("vInt1 = {}, therfore the value of vInt1 is: {}".format(vInt1,vInt1))
    print("{} % {} = {}".format(vInt1,vInt2,vInt1%vInt2))

#6 Use of logical operators: and, or, not
#7 Use of conditional statements: if,elif,else
def func3():
    x = 1
    y = 2
    print("\nI assigned 1 to x and 2 to y for this function.")
    if (x == 1 and y == 2):
        print("If this line printed it was because both x was equal to 1 and y was equal to 2")
    if (x == 1 or y == 3):
        print("If this line printed it was because either x was equal to 1 or y was equal to 3")
    if not(x == 3):
        print("If this line printed it was because x was not equal to 3")
    if y == 3:
        print("If this line printed it was because y was equal to 3")
    else:
        print("If this line printed it means that y was equal to any other number other than 3")

#8 Use of a while loop
def func4():
    print("\nThis function will demonstrate a while loop")
    stop = True
    while stop:
        choose = raw_input("\nDo you want the while loop to continue? (y/n)").lower()
        if choose == 'y':
            stop = True
            print("The loop is going to continue")
        if choose == 'n':
            stop = False
            print("The loop is going to quit")

#9 Use of a for loop
def func5():
    print("\nThis function will demonstrate a for loop that uses range(0,5)")
    for x in range(0,5):
        print x # prints out x in each iteration

#10 Create a list and iterate through that list using a for loop to print each item out on a new line
def func6():
    created_list = ["one", "two", "three", "four", "five", "six"]
    print("\nHere is my created list {} that I will loop through and print out each item on a separate line".format(created_list))
    for item in created_list:
        print(item)

#11 Create a tuple and iterate through it using a for loop to print each item out on a new line
def func7():
    created_tuple = (1,2,3,4)
    print("\nThis function will create a tuple, here is my created tuple: {}, and iterate through it using a for loop to print each item on a new line.".format(created_tuple))
    for x in created_tuple:
        print(x)

#12 Define a function that returns a string variable
def func8():
    string_variable = "returned string"
    return string_variable

#13 Call the function you defined above and print the result to the shell
def func9():
    print("\nThis function calls func8(), which returns a string, and prints out the returned string")
    string = func8()
    print("This is the string that was returned: '{}'".format(string))

if __name__ == "__main__":
    func1()
    func2()
    func3()
    func4()
    func5()
    func6()
    func7()
    func9()
