# 1. Classes & Objects
# Let's take a look and create a few instances of data types we're already familiar with to prove that they're all classes of their own:
str1 = str()
list1 = list()
dictionary1 = dict()

print(type(str1))  # Output: <class 'str'>
print(type(list1))  # Output: <class 'list'>
print(type(dictionary1))  # Output: <class 'dict'>


# Python naming convention: Classes we make ourselves are always created in title case
# note how Car is in title case
class Car:
    pass


my_car = Car()
print(type(my_car))  # Output: <class '__main__.Car'>


# 2. Attributes
class Car:
    # Class Attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance Attributes
        self.make = make
        self.model = model


# Creating instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4
print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Civic

# Syntax of the __init__ Method
# The __init__ method is defined inside of a class with the following syntax:


def __init__(self, parameter1, parameter2):
    # Initialization code
    self.attribute1 = parameter1
    self.attribute2 = parameter2


# How __init__ works
class Car:
    def __init__(self, make, model, year):
        # Instance Attributes
        self.make = make  # The make of the car (e.g., 'Toyota')
        self.model = model  # The model of the car (e.g., 'Corolla')
        self.year = year  # The year of manufacture (e.g., 2020)


# Creating instances of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Accessing the instance attributes
print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Corolla
print(car1.year)  # Output: 2020

print(car2.make)  # Output: Honda
print(car2.model)  # Output: Civic
print(car2.year)  # Output: 2018


# Example with Default Values
class Car:
    def __init__(self, make, model, year=2021):
        self.make = make
        self.model = model
        self.year = year


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic", 2018)

print(car1.year)  # Output: 2021 (default value used)
print(car2.year)  # Output: 2018 (provided value)


# Example of Instance Method
class Car:
    def __init__(self, make, model, mileage=0):
        # Instance attributes
        self.make = make
        self.model = model
        self.mileage = mileage

    # Instance method to display car information
    def display_info(self):
        return f"{self.make} {self.model}, Mileage: {self.mileage} miles"

    # Instance method to update the mileage
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total mileage is now {self.mileage} miles."


# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 10000)

# Calling instance methods
print(my_car.display_info())  # Output: Toyota Corolla, Mileage: 10000 miles
print(my_car.drive(150))  # Output: Drove 150 miles. Total mileage is now 10150 miles


# Example: Defining Classes in python
class OfficeBuilding:
    def __init__(self, floors, offices):
        self.floors = floors
        self.offices = offices

    def open_doors(self):
        print(f"{self.offices} offices are open for business!")

    # creating object from classes


building1 = OfficeBuilding(
    10, 200
)  # 10 and 200 are the arguments of floors and offices
building2 = OfficeBuilding(20, 400)

building1.open_doors()
building2.open_doors()


# Engage & Apply: Mid Lesson Exercise
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method to greet the person
    def greet(self):
        return f"Hello, mu name is {self.name}"

    # method to simulate a birthday
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."


# Creating an instance of Person
person1 = Person("Alice", 25)

# Using the methods
print(person1.greet())  # Output: Hello, my name is Alice!
print(person1.have_birthday())  # Output: Happy Birthday! You are now 26 years old.


# Final Challenge
# Challenge: Create a BankAccount Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount."

    # Method to check the balance
    def get_balance(self):
        return f"Current balance: ${self.balance}"


# Creating an instance of BankAccount
account = BankAccount("Alice", 100)

# Testing the methods
print(account.get_balance())  # Output: Current balance: $100.00
print(account.deposit(50))  # Output: Deposited $50.00. New balance: $150.00
print(account.withdraw(30))  # Output: Withdrew $30.00. New balance: $120.00
print(account.withdraw(200))  # Output: Insufficient funds or invalid amount.


# Private, Public and Protected Attributes
# Example of Public Attributes (BankAccount):
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.balance = balance  # Public attribute


# Create a new bank account
account = BankAccount("Alice", 1000)
# Accessing and modifying public attributes
print(account.account_holder)  # Output: Alice
account.balance += 500  # Directly modifying the balance
print(account.balance)  # Output: 1500


# Example of Public Attributes (Video Game Character):
class Character:
    def __init__(self, name, health, level):
        self.name = name  # Public attribute
        self.health = health  # Public attribute
        self.level = level  # Public attribute


# Creating a new character
player1 = Character("Archer", 100, 1)
# Accessing and modifying public attributes
print(player1.name)  # Output: Archer
player1.level += 1  # Leveling up
print(player1.level)  # Output: 2


# Example of Protected Attributes (BankAccount):
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance  # Protected attribute

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def add_interest(self, interest_rate):
        self._balance += self._balance * interest_rate


# Create a savings account
savings = SavingsAccount("Bob", 2000)
savings.add_interest(0.05)
print(savings.get_balance())  # Output: 2100


# Example of Private Attributes (BankAccount):
class BankAccount:
    def __init__(self, account_holder, balance, password):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute
        self.__password = password  # Private attribute

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Access denied"


# Create a bank account with a private balance and password
account = BankAccount("Charlie", 5000, "mypassword")

# Accessing balance with the correct password
print(account.get_balance("mypassword"))  # Output: 5000

# Trying to access private attribute directly (will raise an AttributeError)
# print(account.__balance)  # Raises AttributeError

# Accessing private attribute via name mangling (not recommended)
print(account._BankAccount__balance)  # Output: 5000


# Example of Private Attributes (Social Media Profile):
class SocialMediaProfile:
    def __init__(self, username, email, password):
        self.username = username  # Public attribute
        self.__email = email  # Private attribute
        self.__password = password  # Private attribute

    def verify_password(self, input_password):
        if input_password == self.__password:
            return "Password verified"
        else:
            return "Invalid password"

    def get_email(self, input_password):
        if input_password == self.__password:
            return self.__email
        else:
            return "Access denied"


# Create a social media profile
profile = SocialMediaProfile("user123", "user@example.com", "securepassword")

# Accessing private email with correct password
print(profile.get_email("securepassword"))  # Output: user@example.com

# Accessing private attribute directly (raises AttributeError)
# print(profile.__email)  # Raises AttributeError

# Accessing private attribute via name mangling (not recommended)
print(profile._SocialMediaProfile__email)  # Output: user@example.com


# 🧠📓Engage & Apply (Mid Lesson Exercise): Fitness Tracker
class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name  # Public attribute
        self.__steps = 0  # Private attribute
        self.__calories_burned = 0.0  # Private attribute

    def add_steps(self, steps):
        if steps > 0:
            self.__steps += steps
            print(f"{steps} steps added. Total steps: {self.__steps}.")
        else:
            print("Steps must be positive.")

    def get_steps(self):
        return self.__steps

    def add_calories(self, calories):
        if calories > 0:
            self.__calories_burned += calories
            print(
                f"{calories} calories burned. Total calories burned: {self.__calories_burned}."
            )
        else:
            print("Calories must be positive.")

    def get_calories_burned(self):
        return self.__calories_burned

    def reset_tracker(self):
        self.__steps = 0
        self.__calories_burned = 0.0
        print("Tracker reset to 0 steps and 0.0 calories burned.")


# Create an instance of FitnessTracker
tracker = FitnessTracker("John")

# Track steps and calories
tracker.add_steps(5000)  # Output: 5000 steps added. Total steps: 5000.
tracker.add_calories(300)  # Output: 300 calories burned. Total calories burned: 300.0.

# Display current progress
print(f"Steps: {tracker.get_steps()}")  # Output: Steps: 5000
print(f"Calories: {tracker.get_calories_burned()}")  # Output: Calories: 300.0

# Reset the tracker
tracker.reset_tracker()  # Output: Tracker reset to 0 steps and 0.0 calories burned.


# Understanding Inheritance and Polymorphism
# Example: Inheritance in a Video Game character System
# Parent class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def move(self):
        print(f"{self.name} is moving!")

    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")


# Subclass: Warrior
class Warrior(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(
            name, health, attack_power
        )  # Call the parent class constructor
        self.armor = armor

    def use_shield(self):
        print(f"{self.name} blocks the attack with a shield!")


# Subclass: Mage
class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name} casts a powerful spell!")


# Creating instances
warrior = Warrior("Conan", 100, 20, "Iron Armor")
mage = Mage("Gandalf", 80, 25, 100)

# Calling methods
warrior.move()  # Output: Conan is moving!
warrior.attack()  # Output: Conan attacks with 20 power!
warrior.use_shield()  # Output: Conan blocks the attack with a shield!

mage.move()  # Output: Gandalf is moving!
mage.attack()  # Output: Gandalf attacks with 25 power!
mage.cast_spell()  # Output: Gandalf casts a powerful spell!

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")

class Warrior(Character):
    def attack(self):
        # Override the parent class method
        print(f"{self.name} slashes with a sword, dealing {self.attack_power} damage!")

class Mage(Character):
    def attack(self):
        # Override the parent class method
        print(f"{self.name} casts a fireball, dealing {self.attack_power} damage!")

# Creating instances
warrior = Warrior("Conan", 100, 20)
mage = Mage("Gandalf", 80, 25)

# Calling the overridden methods
warrior.attack()   # Output: Conan slashes with a sword, dealing 20 damage!
mage.attack()      # Output: Gandalf casts a fireball, dealing 25 damage!


# Overriding  in Inheritance
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")


class Warrior(Character):
    def attack(self):
        # Override the parent class method
        print(f"{self.name} slashes with a sword, dealing {self.attack_power} damage!")


class Mage(Character):
    def attack(self):
        # Override the parent class method
        print(f"{self.name} casts a fireball, dealing {self.attack_power} damage!")


# Creating instances
warrior = Warrior("Conan", 100, 20)
mage = Mage("Gandalf", 80, 25)

# Calling the overridden methods
warrior.attack()  # Output: Conan slashes with a sword, dealing 20 damage!
mage.attack()  # Output: Gandalf casts a fireball, dealing 25 damage!

# Example: Polymorphism with Game Characters

from abc import ABC, abstractmethod


class Character:
    @abstractmethod
    def attack(self):
        print("This method should be overridden by subclasses.")


class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword!")


class Mage(Character):
    def attack(self):
        print("Mage casts a fireball!")


class Archer(Character):
    def attack(self):
        print("Archer shoots an arrow!")


# Using polymorphism in a function
def perform_attack(character):
    character.attack()  # Calls the correct method based on the object's class


# Cannot instantiate Character directly:
# character = Character() # Raises TypeError

# Creating instances of different character types
warrior = Warrior()
mage = Mage()
archer = Archer()

# Using polymorphism
perform_attack(warrior)  # Output: Warrior attacks with a sword!
perform_attack(mage)  # Output: Mage casts a fireball!
perform_attack(archer)  # Output: Archer shoots an arrow!
# Polymorphism allows us to call the attack() method on any character type (Warrior, Mage, Archer) without knowing the specific class in advance.
# Each character type provides its own implementation of attack(), but the function perform_attack() treats them all the same. This makes the code more flexible and extendable.
# New character types can easily be added in the future, and the perform_attack() function will work with them without modification.


# Example: Polymorphism in a Social Media Platform
class User:
    def post_content(self):
        print("Posting generic content.")


class RegularUser(User):
    def post_content(self):
        print("Posting a photo as a regular user.")


class Influencer(User):
    def post_content(self):
        print("Posting a sponsored video as an influencer.")


class Brand(User):
    def post_content(self):
        print("Posting an ad as a brand.")


# Polymorphic behavior
def publish_post(user):
    user.post_content()


# Creating instances
default_user = User()
user1 = RegularUser()
user2 = Influencer()
user3 = Brand()

# Using polymorphism
publish_post(default_user)  # Output: "Posting generic content"
publish_post(user1)  # Output: Posting a photo as a regular user.
publish_post(user2)  # Output: Posting a sponsored video as an influencer.
publish_post(user3)  # Output: Posting an ad as a brand.


# Advanced Concepts in Inheritance and Polymorphism
# Multiple Inheritance
class Flyer:
    def fly(self):
        print("Flying high!")


class Swimmer:
    def swim(self):
        print("Swimming fast!")


class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")


# Creating an instance of Duck
duck = Duck()
duck.fly()  # Output: Flying high!
duck.swim()  # Output: Swimming fast!
duck.quack()  # Output: Quack!

#You can view the MRO of a class using the __mro__ attribute or the mro() method:
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()  # Output: Hello from B
print(D.mro())

# Output [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]