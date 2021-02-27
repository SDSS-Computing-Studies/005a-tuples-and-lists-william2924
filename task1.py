#!python3

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""
tuple = int(input("Enter a number"))
myTuple = ('Alpha', 'Baker', "Charlie", "Delta", "Echo","Foxtrot","Golf")
print("\n======")
print(myTuple)
print(" tuple[0] is " + myTuple[0])
print(" tuple[1] is " + myTuple[1])
print(" tuple[2] is " + myTuple[2])
print(" tuple[3] is " + myTuple[3])
print(" tuple[-1] is " + myTuple[-1])
print(" tuple[-2] is " + myTuple[-2])
print(" tuple[-3] is " + myTuple[-3])
