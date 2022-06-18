# Basic Data structures in python

# 1-Tuple
# 2-List
# 3-Dictionaries
# 4-Sets

## 1- Tuple
# - Ordered collections of elements
# - Enclosed in round braces() or paranthesis
# - Different types of elements can be stored
# - Immutatable (Stored elements cannot be changed later)

tup1 = (1, "Mango", 2.5, True)
print(tup1)

# Type of a tuple
print(type(tup1))

### - Indexing in tuple
print(tup1[1])
print(tup1[2])

# Last element is exclusive
print(tup1[0:3])
print(tup1[1:3])

#counting elements in tuple
print(len(tup1))

# Declaring another tuple
tup2 = ("Baba", 2 , True, 1.1)

# Concatenation : Adding 2 or more tuples
print(tup1 + tup2)
print(tup1*2 + tup2)

# Declaring another tuple
tup3 = (23, 20, 90, 98, 17, 71)

#minimum in a tuple
print(min(tup3))

#maximum in a tuple
print(max(tup3))

print(tup3*2) #doubles the number of element
#only multiplication operator can be applied at tuple

#tup3+2 #Error due to TypeError: can only concatenate tuple (not "int") to tuple

## 2- Lists
# - Ordered collections of elements
# - Enclosed in squre bracket/braces
# - Mutable, You can change the values

list1 = ["BabaG", 1, True, 1.1]

print(type(list1))    # returns type
print(len(list1))     # returns length
print(list1[2])       # returns third element (stating from 0th element)
print(list1[3])       # returns fourth element (stating from 0th element)

# Declaring another list
list2 = [2,1, "BabaG", "light", 5.5, True]

# Adding teo lists
print(list1 + list2)

# Duplication number of elements in a list
print(list1*2)

list1.reverse() #The reverse() method reverses the elements of the list.
print(list1)

list1.append("Codanics") #The append() method adds an item to the end of the list.
print(list1)

print(list1.count(1)) #The count() method returns the number of times the specified element appears in the list.

# Declaring another list

list3 = [2,3,2,77,76,7,8,9,3,6,5,4,7]
print(list3)
print(len(list3))

list3.sort() #The sort() method sorts the elements of a given list in a specific ascending or descending order.
print(list3)

print(list3*2) #doubles the number of element

print(list1 + list2) #addes two lists 
print(lists = list1 + list2 + list3)


## 3- Dictionaries
# - Any unordered collection of elements
# - Key and Values
# - Enclosed in curly braces or brackets {}
# - Mutatable; We can change the valued of it's elements anytime

#Food and their prices
menu1 = {"Samosa": 30, "Pakorda": 10, "Salad": 20, "Chicken Roles": 60}
print(menu1)
print(type(menu1))
#extracting data
keys1 = menu1.keys()
print(keys1)

#extracting data
values1 = menu1.keys()
print(values1)

#Adding new element
menu1["Chatni"] = 10
print(menu1)

#Update the values
menu1["Chatni"] = 20
print(menu1)

food2 = {"dates":50, "Chocolates":100, "Sphaghettis":50}
print(food2)

#Concatination
menu1.update(food2)
print(menu1)


## 4- Sets
# - Unordered and unindexed
# - curly braces are used
# - No duplicates are allowed

# Declaring a set
s1 = {2, 5, True, "FaislaAbad", "Ammar" "BabaG", "Codanics" }
print(s1)
print(type(s1))

#Adding new element in sets
s1.add("Ammar1")
print(s1)

#Removing some elements from the sets
s1.remove("Ammar1")
print(s1)