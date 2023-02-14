# Update 31.01 02:50:
# Sorry, I know it's too late but I was so busy at work
# And I still want to take a RED DIPLOMA)

import re


def first_five():

    print('1. You can add apostrophe to str by using backslash: \\\'\nor by using another type of quotes: print("some text, now apostrophe:\', some text")\n')

    print("2. For our comfort to print text in multiple lines \
we can use backslash: \\ to continue write your text \
from new line, but in terminal it returns a one line string)\n")

    string1 = input(
        "3. To calculate length of string we can use len() function.\nPlease, type your string: ")
    print("Length of your string is", len(string1))

    string2 = input(
        "\n4. Here we have concatenation previous string and new one.\nPlease, type one more: ")
    print(string1 + string2)

    print("\n5. Now you can see previous strings with space between them:",
          string1, string2)


def user_info():
    name = input("What is your name?: ")
    age = int(input("Please, enter your age: "))
    print("Nise to meet you," + name +
          "! I show you? how in Python we can formating text by 3(4) different ways:")
    print("a) Your name is", name, "and you're", age, "years old")
    print(f"b) Your name is {name} and you're {age} years old")
    print("c) Your name is {0} and you're {1} years old".format(name, age))


def format_string():
    string_1 = "Bear"
    string_2 = "bear"
    string_3 = "BEAR"
    string_4 = "bEar"
    string = "     the Quick Brown Fox Jumps ovEr the Lazy Dog   "
    print("First of all we have this string:", string, "as our object.")
    print(f'''
1. {string.lower()}
2. {string.upper()}
3. {string.title()}
4.  a) {string.lstrip()}
    b) {string.rstrip()}
    c) {string.strip()}
5. Checking if stings starts with some prefix:
    - string_1 = "{string_1}": {string_1.startswith("Be")}
    - string_2 = "{string_2}": {string_2.startswith("Be")}
    - string_3 = "{string_3}": {string_3.startswith("Be")}
    - string_4 = "{string_4}": {string_4.startswith("Be")}
6. Converting prev strings to have a positive results:
    - string_1 = "{string_1}": {string_1.replace(string_1[0], "B").replace(string_1[1], "e").startswith("Be")}
    - string_2 = "{string_2}": {string_2.replace(string_2[0], "B").replace(string_2[1], "e").startswith("Be")}
    - string_3 = "{string_3}": {string_3.replace(string_3[0], "B").replace(string_3[1], "e").startswith("Be")}
    - string_4 = "{string_4}": {string_4.replace(string_4[0], "B").replace(string_4[1], "e").startswith("Be")}
7. Find and replace all letters ‘e’ with the letter ‘x’:
    - string_1 = "{string_1}": {string_1.replace("e", "x").replace("E", "x")}
    - string_2 = "{string_2}": {string_2.replace("e", "x").replace("E", "x")}
    - string_3 = "{string_3}": {string_3.replace("e", "x").replace("E", "x")}
    - string_4 = "{string_4}": {string_4.replace("e", "x").replace("E", "x")}
''')


def format_numbers():
    string = '12345!,_6--'
    # I don't know how to make it w-out .replace() repeating, w-out regex or w-out loop
    # think that this way is mach better than flood by .replace()
    clean_string = re.sub(r'[^0-9]', '', string)
    print(f'''Ok, in this task we need to modify "{string}" \
only by string methods and replace all not numeric elements: {clean_string}
''')


def asterlink():
    string = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'
    clean_string = string.replace('X', '').replace('x', '')
    print(f"Here, I think we need to replace all 'x':", clean_string)
    reversed_string = clean_string[::-1]
    print("And I reverse it, so...\nVoilà! I found a secret message:", reversed_string)


def main_function():
    print("Welcome back, my friend. Glad to see you again!\nToday I would like to introduce you a \"Console Homework Program 3.0\"!\nOk, Let's get started from first five tiny exercises.\n")
    first_five()
    print("Ok, now we can move on with more interestinng things)")
    print("Let's move on, next exercises made me sweat but there are solutions:")
    format_string()
    format_numbers()
    print("And the last one, but not the least, 9 task with asterlink.")
    asterlink()
    print("Ok, and that's all!\nIt was pretty cool, thank you for your attention!\nHave a great time and see ya!")


main_function()
