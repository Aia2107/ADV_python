# Opening & Writing to Files
# Open a file in 'w' mode to write data
file = open("new_file.txt", "w")
file.write("Writing to a file from Python!\n")
file.close()  # Always close the file after writing

# Appending data to the file without overwriting
file = open("new_file.txt", "a")
file.write('Adding more content with "a" mode\n')
file.close()


# Reading Files
# Reading the file with 'r' mode
with open("new_file.txt", "r") as file:
    content = file.read()  # Read the entire file content
    print(content)


# Engage & Apply: Mid-Lesson Exercise
# Example solution for managing a list of favorite foods
def write_foods(foods):
    with open("foods.txt", "w") as file:
        for food in foods:
            file.write(food + "\n")


def read_foods():
    foods_list = []
    with open("foods.txt", "r") as file:
        for line in file:
            foods_list.append(line.strip())
    return foods_list


def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == "1":
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == "2":
            print("Your favorite foods:")
            for food in foods:
                print(food)
        elif action == "3":
            idx = int(input("Which food to remove? "))
            foods.pop(idx - 1)
            write_foods(foods)
        elif action == "4":
            break


main()

# Storing Lists
flowers = ["Wysteria", "Sunflowers", "Orchids", "Marigolds"]

with open("garden.txt", "w") as file:
    for flower in flowers:
        file.write(flower + "\n")

# Extracting Lists
flowers = []

with open("garden.txt", "r") as file:
    for line in file:
        flowers.append(line.strip())
print(flowers)


# Storing and Extracting Dictionaries:
clubs = {
    'Driver': 'Cobra',
    'Irons': 'Sirixion',
    'Hybrid': 'Callaway',
    'Putter': 'Ping'
}

with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f"{club}: {brand}\n")

# Extracting dictionary data
golf_clubs = {}

with open('golf_bag.txt', 'r') as file:
    for line in file:
        club, brand = line.strip().split(': ')
        golf_clubs[club] = brand
print(golf_clubs)


# Managing Data Interactively: TV Show Manager
# Writing, Reading, and Removing TV Shows:
import re


# Function to write TV shows to a file
def write_show(shows):
    with open("shows_list.txt", "w") as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")


# Function to add a show to our shows list in dictionary format, and write it to our file with the write_show function
def add_show(shows):
    title = input("What is the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("what is the genre? ")
    shows.append({"Title": title, "Platform": platform, "Genre": genre})
    write_show(shows)  # write to shows file


# Function to read TV shows from a file
def read_shows():
    shows_list = []
    with open("shows_list.txt", "r") as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.append(
                {
                    "Title": data.group(1),
                    "Platform": data.group(2),
                    "Genre": data.group(3).strip(),
                }
            )
    return shows_list
# Function to print the list of shows for the user in a formatted way
def view(shows):
    print("Shows List")
    print("-----------------------")
    for idx, show in enumerate(shows):
        vowels = ["a", "e", "i", "o", "u"]
        a_or_an = "an" if show["Genre"][0].lower() in vowels else "a"
        print(
            f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}"
        )
# Function to show our current list of shows and allow the user to choose which to remove
def remove_show(shows):
    view(shows)
    option = int(input("\n\nChoose a number for the show you'd like to remove: "))
    show = shows.pop(option - 1)  # index - 1
    print(f"\n{show['Title']} was sucessfully removed!")
    write_show(shows)


# Building the Interactive program
# Main function to run the TV show manager
def main():
    while True:
        shows_list = read_shows()  # Read the current list of shows from the file
        action = input(
            """
Options
-----------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Quit
"""
        )
        if action == "1":
            add_show(shows_list)  # Add a new show
        elif action == "2":
            remove_show(shows_list)  # Remove a show
        elif action == "3":
            view(shows_list)  # View the list of shows
        elif action == "4":
            print("Thanks for using this app!")
            break


main()

#Final Challenge
#Scenario: Modify the TV show manager program to allow the user to edit the platform or genre of an existing TV show.

def edit_show(shows):
    view(shows)
    try:
        idx = int(input("\nEnter the number of the show you want to edit: ")) - 1
        if idx < 0 or idx >= len(shows):
            print("Invalid selection.")
            return
        show = shows[idx]
        print(f"Editing '{show['Title']}'")
        field = input("Edit (1) Platform or (2) Genre? Enter 1 or 2: ")
        if field == "1":
            new_platform = input("Enter new platform: ")
            show["Platform"] = new_platform
        elif field == "2":
            new_genre = input("Enter new genre: ")
            show["Genre"] = new_genre
        else:
            print("Invalid choice.")
            return
        write_show(shows)
        print("Show updated successfully.")
    except ValueError:
        print("Invalid input.")

# Update the main function to include the edit option
def main():
    while True:
        shows_list = read_shows()  # Read the current list of shows from the file
        action = input(
            """
Options
-----------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Edit a TV Show
5 - Quit
"""
        )
        if action == "1":
            add_show(shows_list)  # Add a new show
        elif action == "2":
            remove_show(shows_list)  # Remove a show
        elif action == "3":
            view(shows_list)  # View the list of shows
        elif action == "4":
            edit_show(shows_list)  # Edit a show
        elif action == "5":
            print("Thanks for using this app!")
            break

# Uncomment the following line to run the updated main function
# main()
