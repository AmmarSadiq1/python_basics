# defining a string
food = "biryani"

# finding string length
print(len(food))

#Capitalizae first element
print(food.capitalize())

#Converts all into into upper-case letters
print(food.upper())

#Converts all into into lower-case letters
print(food.lower())

#Replace
print(food.replace('b', "Sh"))

#Counting a specific alphabet in a string
sent = "I am learning python with Dr. Ammar"
print(sent.count("a"))

# Finding an index number in string
sent = "I am learning python with Dr. Ammar"
print(sent.find("I"))

# Splitting a string?
food = 'I wanna eat apple, banana, dates, and cherry'
print(food.split(","))

# Indexing in string
a="Chilli milli"
print(a)

print(a[0])        # output : C
print(a[5])        # output : i
print(a[6])        # output : ' ' 

#Last index is exclusive
print(a[0:5])      # output : Chill
print(a[0:6])      # output : Chilli

# -1 is the last index, -2 is seconf last, -3 is third last and so on... 
print(a[-1])       # output : i
print(a[-5:-1])    # output : mill
a[-5:13]           # output : milli