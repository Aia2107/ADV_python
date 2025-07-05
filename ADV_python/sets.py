#Create an empty set

def empty_set():
    print(type(empty_set))

#Create a set with some value
def set_with_values():
    my_set = {1, 2, 3, 4, 5}
    print(my_set)

#Create working with lists, tuples, and dictionaries
alist = [1, 2, 3, 4, 5]
set_list = set(alist)
print(set_list)

#Exercise: Creating Sets for hobbies
hobbies = ['reading', 'gaming', 'hiking', 'gaming', 'swimming', 'hiking']
hobbies_set = set(hobbies)
print("Original List:", hobbies)
print("Set with Duplicates Removed:", hobbies_set)

#Looping Over Sets: for loop
#looping over sets
aset = ('apple', 'orange', 'banana')
for fruit in aset:
    print(fruit)

#loop through a set
favorite_movies = {'Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Gladiator'}
for movie in favorite_movies:
    print(movie)

#set Methods
#using in keyword
my_set = {'superman', 'batmn', 'wonder womam', 'the flash'}
print('superman' in my_set)  # True
print('spiderman' in my_set)  # False

#example
guests = {'Alice', 'Bob', 'Charlie'}
if 'Alice' in guests:
    print('Alice is invited to the party.')
else:
    print('Alice is not invited to the party.')

#adding items to a set: add()
my_choose = {'superman', 'batman', 'wonder woman', 'the flash',}
my_choose.add('green lantern')
print(my_choose)  # Output: {'superman', 'batman', 'wonder woman', 'the flash', 'green lantern'}

#set modification practice
foods = {'pizza', 'sushi', 'pasta', 'ice cream'}
foods.add('burger')  # Adding a new item
print('pasta' in foods)  # Checking for an item
print(foods)

#advanced set methods
#subset and superet checks
#issubset() and issuperset()
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))  # True
print(set_b.issuperset(set_a))  # True

#comapring sets
set1 = {'basketball', 'soccer', 'tennis'}
set2 = {'basketball', 'soccer'}

print(set2.issubset(set1))  # Is set2 a subset of set1?
print(set1.issuperset(set2))  # Is set1 a superset of set2?

#Set Operations: Union, Intersection, Difference, and Symmetric Difference
#union
set_x = {'Alice', 'Bob', 'Charlie'}
set_y = {'David', 'Eve', 'Frank', 'Charlie'}
union_set = set_x.union(set_y)
print("Union:", union_set)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}
#intersection
set_x = {'Alice', 'Bob', 'Charlie'}
set_y = {'David', 'Eve', 'Frank', 'Charlie'}
union_set = set_x.intersection(set_y)
print("Union:", union_set)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}
#difference
set_x = {'Alice', 'Bob', 'Charlie'}
set_y = {'David', 'Eve', 'Frank', 'Charlie'}
union_set = set_y.difference(set_x)
print("Union:", union_set)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}
#symmetric difference
set_x = {'Alice', 'Bob', 'Charlie'}
set_y = {'David', 'Eve', 'Frank', 'Charlie'}
union_set = set_x.symmetric_difference(set_y)
print("Union:", union_set)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}

#Final Challenge: Email list duplication removal
def clean_email_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    # Remove duplicates and merge
    all_unique = set1.union(set2)
    print("All unique emails:", all_unique)
    
    # Common emails
    common_emails = set1.intersection(set2)
    print("Emails in both lists:", common_emails)
    
    # Emails unique to each list
    unique_emails = set1.symmetric_difference(set2)
    print("Emails unique to each list:", unique_emails)

email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)

