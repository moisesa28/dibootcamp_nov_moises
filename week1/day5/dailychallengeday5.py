#Challenge 1: Sorting
#Write a Python program that takes a single string of
# words as input, where the words are separated by commas
# (e.g., ‘apple,banana,cherry’). The program should output
# these words sorted in alphabetical order, with the sorted
# words also separated by commas.

# Step 1: Get Input

input_string = input("Enter words separated by commas: ")

# Step 2: Split the String
words_list = input_string.split(',')

# Step 3: Sort the List
sorted_words = sorted(words_list)

# Step 4: Join the Sorted List
output_string = ','.join(sorted_words)

#Step 5: Print the Result

print("Sorted words:", output_string)
    
print('')
print('--------------------------------')
print('')

#Challenge 2: Longest Word
#Write a function that takes a sentence as input and
# returns the longest word in the sentence. If there are
# multiple longest words, return the first one encountered.
# Characters like apostrophes, commas, and periods should
# be considered part of the word.

#define the function
def longest_word(sentence):
    input_sentence = sentence


#Step 2: Split the Sentence into Words
    words = input_sentence.split()

#Initialize Variables
    max_length = 0
    longest = ""

#Iterate Through the Words
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest = word

#Compare Word Lengths
    return longest

# Return the Longest Word
#Get user input
user_sentence = input("Enter a sentence: ")
print("Longest word:", longest_word(user_sentence))