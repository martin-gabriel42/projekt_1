"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Gabriel
email: gabmar@post.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
    ]


registered_users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass1230"
    }

vertical_separator = "----------------------------------------"

#user verification
username = input("username:")
password = input("password:")

print(vertical_separator)

if username in registered_users.keys() and registered_users[username] == password:
    print("Welcome to the app,", username, "\nWe have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    quit()

print(vertical_separator)


#text selection
option = input("Enter a number btw. 1 and 3 to select: ")

if option not in ["1", "2", "3"]:
    print("nonexistent option, terminating the program.. ")
    quit()
text = TEXTS[int(option) - 1]

print(vertical_separator)


#text analysis
new_string = ""
for char in text:
    if char.isalnum() or char == " ":
        new_string += char

list_of_words = [word for word in new_string.split(" ") if word != ""]

number_of_words = len(list_of_words)
number_of_title_words = len([word for word in list_of_words if word.istitle()])
number_of_uppercase_words = len([word for word in list_of_words if word.isupper()])
number_of_lowercase_words = len([word for word in list_of_words if word.islower()])
number_of_numeric_strings = len([word for word in list_of_words if word.isnumeric()])

numbers = [word for word in list_of_words if word.isnumeric()]
sum_of_numeric_strings = sum(float(number) for number in numbers)
if sum_of_numeric_strings == int(sum_of_numeric_strings):
    sum_of_numeric_strings = int(sum_of_numeric_strings)


#printing the statistics
print("There are ", number_of_words, " words in the selected text.", sep = "")
print("There are ", number_of_title_words, " titles.", sep = "")
print("There are ", number_of_uppercase_words, " uppercase words.", sep = "")
print("There are ", number_of_lowercase_words, " lowercase words.", sep = "")
print("There are ", number_of_numeric_strings, " numeric strings.", sep = "")
print("The sum of all the numbers is ", sum_of_numeric_strings, ".", sep = "")

print(vertical_separator)


#printing the graph
lengths_of_words = dict()

for word in list_of_words:
        length = len(word)

        if length not in lengths_of_words.keys():
            lengths_of_words[length] = 1
        else:
            lengths_of_words[length] += 1

sorted_lengths_of_words = {key: lengths_of_words[key] for key in sorted(lengths_of_words.keys())}
print("LEN|  OCCURENCES|  NR.")

print(vertical_separator)

max_occurence = max(sorted_lengths_of_words.values())
max_digits_of_length = len(str(max(sorted_lengths_of_words.keys())))

for length, occurence in sorted_lengths_of_words.items():
    line = ""
    line += (" " * (max_digits_of_length - len(str(length)))) + str(length) + "|"
    line += occurence * "*" + ((max_occurence - occurence + 5) * " ") + "|" + str(occurence)
    print(line)