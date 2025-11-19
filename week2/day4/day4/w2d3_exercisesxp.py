import os 
import random
import json
#Exercises XP
# Exercise 1: Random Sentence Generator

#Goal: Create a program that generates a random sentence of a specified length from a word list.
print('Exercise 1: Random Sentence Generator')
print('')

def get_words_from_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "word.txt")

    with open(file_path, "r") as f:
        words = f.readlines()

    # Remove newline characters
    words = [word.strip() for word in words]

    return words

def get_random_sentence(length):
    words = get_words_from_file()

    # Choose "length" random words (with repetition allowed)
    random_words = [random.choice(words) for _ in range(length)]

    # Create a lowercase sentence
    sentence = " ".join(random_words).lower()

    return sentence

def main():
    print("This program generates a random sentence based on words from a file.")

    user_input = input("Enter desired sentence length (2–20): ")

    # Validate: Check if integer
    if not user_input.isdigit():
        print("Error: You must enter a number.")
        return

    length = int(user_input)

    # Validate range
    if length < 2 or length > 20:
        print("Error: Number must be between 2 and 20.")
        return

    # Input is valid → generate sentence
    sentence = get_random_sentence(length)
    print("\nGenerated sentence:")
    print(sentence)


# Run main
if __name__ == "__main__":
    main()

print('')
print('-----------')
# Exercise 2: Working with JSON
print('Exercise 2: Working with JSON')

sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
#Access the nested "salary" key
salary = sampleJson["company"]["employee"]["payable"]["salary"]
print("Employee Salary:", salary)

#Add the birthday to employee
sampleJson["company"]["employee"]["birth_date"] = '1995-04-08'

#Get directory path of this script
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "sampleJson.json")

#Save dictionary to JSON file
with open(file_path, "w") as f:
    json.dump(sampleJson, f, indent=2)
    print("JSON file was created at:", file_path)

#Convert dict → JSON string
json_string = json.dumps(sampleJson, indent=2)
print("\nJSON as string:")
print(json_string)

#Load JSON back from file
with open(file_path, "r") as f:
    sampleJson_from_file = json.load(f)
print("\nLoaded from file:")
print(sampleJson_from_file)

#Convert JSON string → dict
data_from_string = json.loads(json_string)
print("\nLoaded from string:")
print(data_from_string)