# Tale of  Tuplea and Lists Entwined Video

enchanted_library = ("Magic Towe", ["Anchient Scrolls", ("Spell", "Curse")], "Wizard'scguide")

print(enchanted_library[1] [1] [1]) #output Curse

# Tuple Manipulation
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: "apple"
print(my_tuple[1])  # Output: "banana"

# Delving into Deeper Layers Video
mythical_collection = ("Greek Myths", [("Zeus", "Hero"), ["Mount Olympus", ("Lightning", "Thunder")]], "Norse Myths")
print(mythical_collection[1][1][1][1]) #Output  Thunder

# Slicing Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4]) 

# Looping Over Tuples
my_tuple = (1, 2, 3, 4, 5)
for num in my_tuple:
    print(num)

# Workarounds for Modifiyng Tuples Video
my_tuple = ("Introduction", "Conclusion")
temp_list = list(my_tuple)
print(temp_list)
temp_list.append("Epilogue")
print(temp_list)
my_tuple = tuple(temp_list)
print(my_tuple) #Output all tree

# Engage & Apply: Tuple Exploration
my_tuple = (42, "hello", 3.14, True)
# access and print
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
# Attempt to Modify the Tuple
# my_tuple[1] = "world"  # This should raise an error

# tuple packing
person_info = "Alice", 30, "Developer"
print(person_info)  # Output: ("Alice", 30, "Developer")

# tuple unpacking
# Unpacking tuple into individual variables
name, age, profession = person_info

print(name)  # Output: Alice
print(age)  # Output: 30
print(profession)  # Output: Developer

# Basic Unpacking Video
my_tuple = ("Magic", "Mystery", "Myth")
genre1, genre2, genre3 = my_tuple
print(genre1)
print(genre2)
print(genre3)

# extend unpacking
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)  # Output: 1
print(rest)  # Output: [2, 3, 4, 5]

*start, last = numbers
print(start)  # Output: [1, 2, 3, 4]
print(last)  # Output: 5

# Extend Unpacking Code
my_tuple = ("Prologue", "Adventure", "Climax", "Epilogue")
beginning, *middle, end = my_tuple
print(beginning)
print(middle)
print(end)

# Ignoring Values with Underscore(_)
person_info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = person_info  # Ignore age and location

print(name)  # Output: Eve
print(profession)  # Output: Artist


# Tuple packing & Unpacking with Function
# returning multiple values
def get_user_info():
    return "Bob", 29, "Engineer"


# Unpacking the returned tuple
name, age, profession = get_user_info()
print(name)  # Output: Bob


# passing multiple values with unpacking
def display_info(name, age, profession):
    print(f"{name} is {age} years old and works as a {profession}.")


info_tuple = ("Charlie", 28, "Designer")

# Unpacking the tuple when calling the function
display_info(*info_tuple)
# Output: Charlie is 28 years old and works as a Designer.

# tuple methods
# .count()
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3
# .index()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2

#Final Challenge: Tuple Mastery
#Create a Tuple: Create a tuple with at least 6 elements. Feel free to mix different data types like integers, strings, and floats.
my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")

#Access and Print Elements: Access and print the third and fifth elements using indexing.
print("Third element:", my_tuple[2])
print("Fifth element:", my_tuple[4])

#Slice the Tuple: Slice the tuple to extract elements from the second to the fifth position.
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)

#Count Occurrences: Use the count() method to find how many times a specific value appears in your tuple.
count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code)

#Unpack the Tuple: Unpack the tuple into individual variables and print them.
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)

#Concatenate Tuples: Concatenate your tuple with another tuple and print the new tuple.
new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)