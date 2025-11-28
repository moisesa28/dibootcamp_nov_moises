#Exercises XP Ninja

# Exercise 1 : Use the terminal
#  Replace python3 with python for Windows

# Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.

#Exercise 2 : Alias
#Read about alias, and try to open a python console with the command:
#py

# Exercise 3 : Outputs
# Instructions
# Predict the output of the following code snippets:

3 <= 3 < 9
3 == 3 == 3
bool(0)
bool(5 == "5")
bool(4 == 4) == bool("4" == "4")
bool(bool(None))
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#Exercise 4

my_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'

print(len(my_text))

#exercise 5

longest_sentence = ""
max_length = 0

print("Let's play a game! Try to input the longest sentence you can without the character 'A'.")
print("Type 'exit' to quit the game.")

while True:
    user_input = input("Enter your sentence: ")
    
    if user_input.lower() == 'exit':
        print(f"Game over! The longest valid sentence you entered was: '{longest_sentence}' ({max_length} characters).")
        break

    if 'a' in user_input.lower():
        print("Sorry, your sentence contains the character 'A'. Please try again.")
    else:
        current_length = len(user_input)
        if current_length > max_length:
            max_length = current_length
            longest_sentence = user_input
            print(f"Congratulations! '{longest_sentence}' ({max_length} characters) is the new longest sentence without 'A'!")
        else:
            print(f"Not the longest this time. Your current longest is '{longest_sentence}' ({max_length} characters).")

