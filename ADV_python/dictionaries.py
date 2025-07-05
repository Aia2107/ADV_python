# Accessing values by key
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

print(my_dict["name"])  # Output: Alice

"""
Accessing Elements in pyhon dictionary video
"""
kitchen = {
    "Sppons": "Top Drawer",
    "Plates": "Middl Shelf",
    "Cups": "Top Shelf",
    "Blender": "Counter"
}

location_of_spoons = kitchen["Plates"]
print(location_of_spoons) 

# The .get() method & avoiding missing keys
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

print(my_dict.get("age"))  # Output: 25
print(my_dict.get("address", "Not Available"))  # Output: Not Available

'''
Handling Missing Keys Video
'''

kitchen = {
    "Sppons": "Top Drawer",
    "Plates": "Middl Shelf",
    "Cups": "Top Shelf",
    "Blender": "Counter",
}

# location_of_toaster = kitchen["Toaster"] #Output will be error

# Adding  and updating elements in py dict

community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM"
}

community_center["Cooking"] = "1 PM"
print(community_center)

# the Art of Updating: Modifiyng Existing Values
community_center = {"Yoga": "8 AM", "Art": "10 AM"}

community_center["Yoga"] = "7:30 AM"
print(community_center)

# Removing Elements: del statement or .pop() method
# del my_dict['city]
book_shelf = {"Fiction": 10, "Non-fiction": 7, "Mystery": 5}
del book_shelf["Non-fiction"]
print(book_shelf) 
# .pop() method
inventory = { "Apples": 30, "Oranges": 20, "Bananas": 15}
removed_item = inventory.pop("Oranges")
print(removed_item)
print(inventory)

# .keys(): Returns a view object that displays a list of all the keys🔑 in the dictionary. It can be converted to a list if needed.

user_profile = {"name": "Alice", "age": 30, "email": "alice@example.com"}
for key in user_profile.keys():
    print(key)
    print(user_profile)

# .items(): Returns a view object that displays a list of dictionary’s key🔑-value tuple pairs.

book_ratings = {"1984": 4.5, "To Kill a Mockingbird": 4.8, "Brave New World": 4.3}
for book, rating in book_ratings.items():
    print(f"{book} has a rating of {rating}")

# Exercise: Create a dictionary
book_list = {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"}

# Add a new key for publisher
book_list["publisher"] = "Secker & Warburg"

# Modify the value for year
book_list["year"] = 1950
for book, list in book_list.items():
    print(f"{book} is {list}")

# Looping through Keys Only: You can loop through only the keys in a dictionary using a for loop. This approach is useful when you only need to access the keys.

for key in my_dict:
    print(key)
# Output: name, age


# Looping through Values Only: Use the .values() method to loop through the values. This is helpful when you are interested only in the values.

for value in my_dict.values():
    print(value)
# Output: Alice, 26


# Looping through Key-Value Pairs: Use the .items() method to loop through both keys and values. This approach is the most common when you need to access both keys and their corresponding values.

for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output: name: Alice, age: 26

# Looping through dict-s keys in particular order

colors_count = {"red": 3, "blue": 4, "green": 1}
for color in sorted(colors_count.keys()):
    print(f"{color}: {colors_count[color]}")

# Creating a dictionary of users, where each user has their own dictionary of details
users = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "address": {"street": "123 Main St", "city": "New York", "zipcode": "10001"},
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "address": {
            "street": "456 Elm St",
            "city": "San Francisco",
            "zipcode": "94107",
        },
    },
}

# In this example, each user has a dictionary containing their 'name', 'age',
# and an 'address' dictionary with more details like street, city, and zipcode.
# Accessing the city of user1 by first accessing 'user1', then 'address', and then 'city'
city_user1 = users["user1"]["address"]["city"]
print(city_user1)  # Output: New York
# Updating the zipcode of user2 from '94107' to '94109'
users["user2"]["address"]["zipcode"] = "94109"
print(users["user2"]["address"]["zipcode"])  # Output: 94109
# Adding a new key 'phone' to user1 with the value '555-1234'
users["user1"]["phone"] = "555-1234"
print(users["user1"]["phone"])  # Output: 555-1234

# Looping through the outer dictionary 'users'
for user, info in users.items():
    print(f"User ID: {user}")

    # Looping through the inner dictionary for each user
    for key, value in info.items():
        print(f"  {key}: {value}")

# Expected Output:
# User ID: user1
#   name: Alice
#   age: 25
#   address: {'street': '123 Main St', 'city': 'New York', 'zipcode': '10001'}
#   phone: 555-1234
# User ID: user2
#   name: Bob
#   age: 30
#   address: {'street': '456 Elm St', 'city': 'San Francisco', 'zipcode': '94109'}

# List of Dictionary
students = [
    {"name": "Alice", "age": 25, "major": "Physics"},
    {"name": "Bob", "age": 22, "major": "Computer Science"},
    {"name": "Charlie", "age": 23, "major": "Mathematics"},
]
first_student_major = students[0]["major"]
print(first_student_major)  # Output: Physics
# Looping through the list of students
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Expected Output:
# Name: Alice, Age: 25, Major: Physics
# Name: Bob, Age: 22, Major: Computer Science
# Name: Charlie, Age: 23, Major: Mathematics


# List within Dictionary
favorite_books = {
    'Alice': ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Bob': ['The Great Gatsby', 'Catch-22', 'Moby Dick'],
    'Charlie': ['The Hobbit', 'Harry Potter', 'War and Peace']
}
# Accessing Alice's favorite books
alice_books = favorite_books["Alice"]
print(alice_books)  # Output: ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice']

# Accessing Bob's second favorite book
second_favorite_bob = favorite_books["Bob"][1]
print(second_favorite_bob)  # Output: Catch-22
# Looping through each person and their list of favorite books
for person, books in favorite_books.items():
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")

# Expected Output:
# Alice's favorite books:
#  - 1984
#  - To Kill a Mockingbird
#  - Pride and Prejudice
# Bob's favorite books:
#  - The Great Gatsby
#  - Catch-22
#  - Moby Dick
# Charlie's favorite books:
#  - The Hobbit
#  - Harry Potter
#  - War and Peace


# Final challenge: Student Grade rogram
students = {"Alice": 85, "Bob": 42, "Charlie": 68, "David": 49}

for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")
