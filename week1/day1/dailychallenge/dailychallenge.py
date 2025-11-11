#. **Ask for User Input:**
#- The string **must be exactly 10 characters long**.
#2. **Check the Length of the String:**
#- If the string is **less than 10 characters**, print: `"String not long enough."`
#- If the string is **more than 10 characters**, print: `"String too long."`
#- If the string is **exactly 10 characters**, print: `"Perfect string"`
#  and proceed to the next steps.

import random


user_info = input('Please type your name ')
len(user_info)

if len(user_info) < 10:
    print("String not long enough.")

if len(user_info) > 10:
    print('String too long.')

if len(user_info) == 10:
    print('Perfect string.')


#3. **Print the First and Last Characters:**
#- Once the string is validated, print the **first** and **last** characters
first_char = user_info[0]
last_char = user_info[-1]
print(first_char)
print(last_char) 

#4. **Build the String Character by Character:**
#- Using a `for` loop, construct and print the string
# **character by character**. Start with the first character, 
#then the first two characters, and so on, until the entire string is printed.

for i in range(len(user_info)):
  print(user_info[:i+1])

#. **Bonus: Jumble the String (Optional)**
#As a bonus, try **shuffling** the characters in the string and print the newly jumbled string.
 #**Hint:** You can use the `random.shuffle` function to shuffle a list of characters.

