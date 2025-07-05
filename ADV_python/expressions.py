# Finding all matches with re.findall()

import re
# Example: coubting "and" in Sentence
text = "Hi my name is Travis, and I like to go and do things and stuff"
ands = re.findall(
    r"and", text
)  # re.findall() returns a list of all occurrances of the given regex pattern within the text.
print(ands)  # Output: ['and', 'and', 'and']
print(
    len(ands)
)  # Output: 3 	Here we use the len() function to get the number of items in the list that was returned to us

# Example: Extracting Hashtags
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Code"
tags = re.findall(r"#\w+", post)
print(tags)  # Output: ['#Python_is_lyfe', '#Regex', '#Code']

# Extracting Email Addressess Video

import re 
text = "Contact us at support@example.com or sales@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
print(emails)

# Engage & Apply (Mid-Lesson Exercise)
tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax",
]

# Write your code to extract hashtags below
import re
hashtags = []
for tweet in tweets:
    hashtags.extend(re.findall(r"#\w+", tweet))
print(hashtags)

# Searching for Patterns with re.search()

# Example: Validating an Email input
email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
if found:
    print(f"{found.group()} is a valid email! Please click continue!")
# Output: kareem33-34-28@gmail.com is a valid email! Please click continue!

# Example: Finding All Email Addresseing Using re.findall
text = "You can contact me at t.p@gmail.com or travis-p2@codingtemple.com, traviscpeck@email.com"
emails = re.findall(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", text)
print(
    emails
)  # Output: ['t.p@gmail.com', 'travis-p2@codingtemple.com', 'traviscpeck@email.com']

# Example: Finding phone numbers in text
import re
text = "Contact us at 123-456-7890."
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print("Phone number found:",  match.group())

# Matching Patterns at the Start of a String with re.match()
# Example: Checking for htpps

url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print(
        "This link goes to a secure website!"
    )  # Output: This link goes to a secure website!

# Extracting Specific Info from Text
import re
url1 = "https://www.example.com"
secure = re.match(r"^(https|http)", url1)
if secure:
    print("Protocol found:", secure.group())

# Splitting Text with re.split()
# Example: Splitting Text on Multiole Delimiters
import re
text = "Python,Regex;Splitting-Example. Fun, right!"
words = re.split(r"[,.;\s!-]+", text)
print(words)
# Output: ['Python', 'Regex', 'Splitting', 'Example', 'Fun', 'right', '']

# Separating Data in CSV String

import re 
csv_data = "Name,Age,Ocupation"
fields = re.split(r",", csv_data)
print(fields)

# Substituting Text with re.sub(pattern, replacer, text)
# Example: Formatting phone numbers
number = "(770) 888-1180"
formatted_number = re.sub(r"\D", "", number)
print(formatted_number)  # Output: 7708881180

# Example: Anonymizing chat user mentions
chat = """
@Yve-bee123 : "I think I love Regex"
@Travis : "Aren't you married?"
@Yve_bee123 : "It's just not the same"
@Travis : "They better not see this!"
"""

anon_chat = re.sub(r"@[\w-]+", "@user-anon", chat)
print(anon_chat)

# Text formatting: standardizing phomne numbers

import re
phone = "Phone: +1 (123) 456 7890"
standard_phone = re.sub(r"\D", "", phone)
print(standard_phone) 

# Grouping with Regex
text = "123-456"
pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, text)
if thematch:
    print(f"Group 1: {thematch.group(1)}")  # Output: 123
    print(f"Group 2: {thematch.group(2)}")  # Output: 456

# Final Challenge (End of Lesson Exercise)
emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org",
]

# Write your code below to validate the emails using re.search()


for email in emails:
    # Implement regex search here
    if re.search(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")
