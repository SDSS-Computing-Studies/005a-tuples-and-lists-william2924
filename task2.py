#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']

"""

print("\n======")
myList = []

a = str(input(" Enter a word: "))
b = str(input(" Enter a word: "))
c = str(input(" Enter a word: "))
d = str(input(" Enter a word: "))
e = str(input(" Enter a word: "))

myList.append(str(a))
myList.append(str(b))
myList.append(str(c))
myList.append(str(d))
myList.append(str(e))

print(myList)
print("======")









