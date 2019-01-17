#Indexing

my_string = "abcdefg"
print (my_string[6])

#you can also index -1 to capture last character in a string and so on
# -7 is the same as index 0
print (my_string[-7])

#slicing
print (my_string[3:])  #from index 3 to the end

print (my_string[:3]) #from beginning up to but not including index 3

print (my_string[1:5]) #from index 1 up to but NOT including index 5

print (my_string[:]) #to print the whole string

print (my_string[::1])
#from beginning to end, STEP SIZE is one which prints every character
print (my_string[::2])
#it skips every other one

#STRINGS ARE IMMUTABLE , YOU CANNOT REASSIGN A VALUE FOR AN INDEX

#STRING FUNCTIONS

x=  my_string.upper()
print (x)
x = my_string.lower()
print(x)
x = my_string.capitalize()   #caps for first letter only
print (x)

#split
myString = "Hello World"
x = myString.split()  #it splits in the blank space by default
print (x)
x = myString.split("e")  #['H', 'llo World']
print (x)
x = myString.split("o") #['Hell', ' W', 'rld']
print (x)

#Print Formatting  , string interpolation
x = "Insert another string here {}".format("INSERT ME")
print (x)
x = "Item One: {}, Item Two:{}".format("Piper", "Penny")
print(x)
x = "Item One: {y}, Item Two:{x}".format(x = "Piper", y = "Penny")
print(x)
