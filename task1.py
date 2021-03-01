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
animal = ('Cat', 'Fish', "Dog", "Bear", "Turtle")
print('Cat', 'Fish', "Dog", "Bear", "Turtle")

number = input("Enter a number")
print("\n======")

print(" string animal[0] is " + str(animal[0]))
print(" string animal[1] is " + str(animal[1]))
print(" string animal[2] is " + str(animal[2]))
print(" string animal[-1] is " + str(animal[-1]))
print(" string animal[-2] is " + str(animal[-2]))
print("\n======")