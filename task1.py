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
animal = ('Alpha', 'Baker', "Charlie", "Delta", "Echo","Foxtrot","Golf")
number = int(input("Enter a number"))
print("\n======")

print(animal)
print("string animal[0] is " + animal[0])
print("string animal[1] is " + animal[1])
print("string animal[2] is " + animal[2])
print("string animal[3] is " + animal[3])
print("string animal[-1] is " + animal[-1])
print("string animal[-2] is " + animal[-2])
print("string animal[-3] is " + animal[-3])
