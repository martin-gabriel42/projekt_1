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



def user_verification():
    username = input("username:")
    password = input("password:")

    if username in registered_users.keys() and registered_users[username] == password:
        return username
    else:
        return False


def print_vertical_separator():
    print("----------------------------------------")


#removes all non-alnum characters from a string and removes duplicate whitespaces, returns result as list of words (or numeric strings)
def word_separator(text):
    new_string = ""
    for char in text:
        if char.isalnum() or char == " ":
            new_string += char
    
    list_of_words = [word for word in new_string.split(" ") if word != ""]

    return list_of_words


#returns the number of words in a list
def number_of_words(list_of_words):
    return len(list_of_words)


#returns the number of titlecase words in a list
def number_of_title_words(list_of_words):
    return len([word for word in list_of_words if word.istitle()])


#returns the number of uppercase words in a list
def number_of_uppercase_words(list_of_words):
    return len([word for word in list_of_words if word.isupper()])


#returns the number of lowercase words in a list
def number_of_lowercase_words(list_of_words):
    return len([word for word in list_of_words if word.islower()])


#returns the number of numeric strings in a list
def number_of_numeric_strings(list_of_words):
    return len([word for word in list_of_words if word.isnumeric()])


#returns the sum of all numeric strings (after conversion to float) in a list
def sum_of_numeric_strings(list_of_words):
    numbers = [word for word in list_of_words if word.isnumeric()]
    sum_of_numbers = sum([float(number) for number in numbers])

    if int(sum_of_numbers) == float(sum_of_numbers):
        return int(sum_of_numbers)
    else:
        return sum_of_numbers


#analyses text and prints the statistcs in correct format
def text_analyser(text):
    list_of_words = word_separator(text)

    words = number_of_words(list_of_words)
    title_words = number_of_title_words(list_of_words)
    uppercase_words = number_of_uppercase_words(list_of_words)
    lowercase_words = number_of_lowercase_words(list_of_words)
    numeric_strings = number_of_numeric_strings(list_of_words)
    sum_of_numbers = sum_of_numeric_strings(list_of_words)

    print("There are ", words, " words in the selected text.")
    print("There are ", title_words, " titlecase words.")
    print("There are ", uppercase_words, " uppercase words.")
    print("There are ", lowercase_words, " lowercase words.")
    print("There are ", numeric_strings, " numeric strings.")
    print("The sum of all the numbers is ", sum_of_numbers)
    print_vertical_separator()


#graphs word length and occurences in given text
def word_length_graph(text):
    list_of_words = word_separator(text)
    lengths_of_words = dict()

    #creates the dictionary and assigns number of occurences to lengths
    for word in list_of_words:
        length = len(word)

        if length not in lengths_of_words.keys():
            lengths_of_words[length] = 1
        else:
            lengths_of_words[length] += 1

    #sorts the keys of the dictionary in ascending order
    sorted_dict = {key: lengths_of_words[key] for key in sorted(lengths_of_words.keys())}

    #prints the graph
    print("LEN|  OCCURENCES|  NR.")
    print_vertical_separator()

    max_occurence = max(sorted_dict.values())
    max_digits_of_length = len(str(max(sorted_dict.keys())))

    for length, occurence in sorted_dict.items():
        line = ""
        line += (" " * (max_digits_of_length - len(str(length)))) + str(length) + "|"
        line += occurence * "*" + ((max_occurence - occurence + 5) * " ") + "|" + str(occurence)
        print(line)


    



def main():

    #user verification
    user = user_verification()
    if user:
        print_vertical_separator()
        print("Welcome to the app,", user, "\nWe have 3 texts to be analyzed.")
    else:
        print("unregistered user, terminating the program..")
        quit()

    #text selection
    print_vertical_separator()
    option = input("Enter a number btw. 1 and 3 to select: ")
    print_vertical_separator()

    #text analysis
    if option not in "123" or option == "": 
        print("nonexistent option, terminating the program.. ")
    else:
        text_analyser(TEXTS[(int(option)) - 1])

    #word length graph
    word_length_graph(TEXTS[(int(option)) - 1])

main()